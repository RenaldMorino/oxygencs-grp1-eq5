# LOG-680 : Template for Oxygen-CS

This Python application continuously monitors a sensor hub and manages HVAC (Heating, Ventilation, and Air Conditioning) system actions based on received sensor data.

It leverages `signalrcore` to maintain a real-time connection to the sensor hub and utilizes `requests` to send GET requests to a remote HVAC control endpoint.

This application uses `pipenv`, a tool that aims to bring the best of all packaging worlds to the Python world.

## Requierements

- Python 3.8+
- pipenv

## Getting Started

Install the project's development dependencies :

```bash
pipenv install -d
```

Install the pre-commit hook to lint and format commits :

```bash
pipenv run pre-commit install
```

if the `pipenv` command does not work, you can try with these commands instead :

```bash
python3 -m pipenv --python /the/python3/binary/location install -d

python3 -m pipenv --python /the/python3/binary/location run pre-commit install
```

On linux, the default python3 path is : `/usr/bin/python3`

> Note: If nothing worked, try to use `venv` to create a virtual environnement, install pipenv with `pip install pipenv`, then run `pipenv install -d`. <br><br>On Visual Studio code, using `Ctrl+shift+p`, you can find the command "Python: Select Interpreter" and create a new virtual environnement using venv or Conda.

## Setup

Create a `.env` file at the root of `oxygencs-grp1-eq5`

In this `.env` file, you need to setup the following variables:

- `HOST`: The host of the sensor hub and HVAC system.
- `TOKEN`: The token for authenticating requests.
- `T_MAX`:  maximum allowed temperature.
- `T_MIN`: The minimum allowed temperature.
- `DATABASE_URL`: The database connection URL.<br>It should be formatted like this: `postgresql://username:password@ip:port/db-name`

## Running the Program

After setup, you can start the program with the following command:

```bash
pipenv run start
```

## Logging

The application logs important events such as connection open/close and error events to help in troubleshooting.

## To Implement

There are placeholders in the code for sending events to a database and handling request exceptions. These sections should be completed as per the requirements of your specific application.

## License

MIT

## Contact

For more information, please feel free to contact the repository owner.
