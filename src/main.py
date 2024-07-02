import json
import logging
import time
from urllib.parse import urlparse
import requests
import psycopg2
from psycopg2 import OperationalError, DatabaseError
from signalrcore.hub_connection_builder import HubConnectionBuilder
from env_variables import EnvVariables


class App:
    def __init__(self):
        self._hub_connection = None
        self.ticks = 10

        # To be configured by your team
        self.host = EnvVariables.get_host()
        self.token = EnvVariables.get_token()
        self.t_max = EnvVariables.get_t_max()
        self.t_min = EnvVariables.get_t_min()
        self.database_url = EnvVariables.get_db_url()

        self.connection = None
        self.connect_to_database()

    def connect_to_database(self):

        parsed_url = urlparse(self.database_url)
        db_username = parsed_url.username
        db_password = parsed_url.password
        db_name = parsed_url.path[1:]
        db_hostname = parsed_url.hostname
        db_port = parsed_url.port

        try:
            self.connection = psycopg2.connect(
                user=db_username,
                password=db_password,
                host=db_hostname,
                port=db_port,
                database=db_name,
            )
            print("Connection to the database established successfully.")
        except (OperationalError, DatabaseError) as error:
            print(f"Error connecting to the database: {error}")

    def __del__(self):
        if self._hub_connection is not None:
            self._hub_connection.stop()
        if self.connection is not None:
            self.connection.close()
            print("PostgreSQL connection is closed.")

    def start(self):
        """Start Oxygen CS."""
        self.setup_sensor_hub()
        self._hub_connection.start()
        print("Press CTRL+C to exit.")
        while True:
            time.sleep(2)

    def setup_sensor_hub(self):
        """Configure hub connection and subscribe to sensor data events."""
        self._hub_connection = (
            HubConnectionBuilder()
            .with_url(f"{self.host}/SensorHub?token={self.token}")
            .configure_logging(logging.INFO)
            .with_automatic_reconnect(
                {
                    "type": "raw",
                    "keep_alive_interval": 10,
                    "reconnect_interval": 5,
                    "max_attempts": 999,
                }
            )
            .build()
        )
        self._hub_connection.on("ReceiveSensorData", self.on_sensor_data_received)
        self._hub_connection.on_open(lambda: print("||| Connection opened."))
        self._hub_connection.on_close(lambda: print("||| Connection closed."))
        self._hub_connection.on_error(
            lambda data: print(f"||| An exception was thrown closed: {data.error}")
        )

    def on_sensor_data_received(self, data):
        """Callback method to handle sensor data on reception."""
        try:
            print(data[0]["date"] + " --> " + data[0]["data"], flush=True)
            timestamp = data[0]["date"]
            temperature = float(data[0]["data"])
            self.take_action(temperature)
            self.save_event_to_database(timestamp, temperature)
        except Exception as err:
            print(err)

    def take_action(self, temperature):
        """Take action to HVAC depending on current temperature."""
        if float(temperature) >= float(self.t_max):
            self.send_action_to_hvac("TurnOnAc")
        elif float(temperature) <= float(self.t_min):
            self.send_action_to_hvac("TurnOnHeater")

    def send_action_to_hvac(self, action):
        """Send action query to the HVAC service."""
        r = requests.get(f"{self.host}/api/hvac/{self.token}/{action}/{self.ticks}")
        details = json.loads(r.text)
        print(details, flush=True)

    def save_event_to_database(self, timestamp, temperature):
        """Save sensor data into database."""
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO hvac_data (date_received, temperature)
                VALUES (%s, %s);
            """
            cursor.execute(query, (timestamp, temperature))
            self.connection.commit()
            cursor.close()
            print(f"Data saved to database: {timestamp} - {temperature}")
        except (OperationalError, DatabaseError) as error:
            print(f"Error saving data to the database: {error}")


if __name__ == "__main__":
    app = App()
    app.start()
