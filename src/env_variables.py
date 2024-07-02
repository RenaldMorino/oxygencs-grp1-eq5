import os
from dotenv import load_dotenv


class EnvVariables:
    __singleton_instance = None

    def __init__(self):
        load_dotenv()
        self.host = os.getenv("HOST")
        self.token = os.getenv("TOKEN")
        self.t_max = os.getenv("T_MAX")
        self.t_min = os.getenv("T_MIN")
        self.db_url = os.getenv("DATABASE_URL")

    @staticmethod
    def __instance():
        if EnvVariables.__singleton_instance is None:
            EnvVariables.__singleton_instance = EnvVariables()

        return EnvVariables.__singleton_instance

    @staticmethod
    def get_host():
        return EnvVariables.__instance().host

    @staticmethod
    def get_token():
        return EnvVariables.__instance().token

    @staticmethod
    def get_t_max():
        return EnvVariables.__instance().t_max

    @staticmethod
    def get_t_min():
        return EnvVariables.__instance().t_min

    @staticmethod
    def get_db_url():
        return EnvVariables.__instance().db_url
