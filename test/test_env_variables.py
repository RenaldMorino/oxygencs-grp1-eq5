import os
from unittest import TestCase, mock
from src.env_variables import EnvVariables


@mock.patch.dict(
    os.environ,
    {
        "HOST": "TEST_HOST_VALUE",
        "TOKEN": "TEST_TOKEN_VALUE",
        "T_MAX": "TEST_T_MAX_VALUE",
        "T_MIN": "TEST_T_MIN_VALUE",
        "DATABASE_URL": "TEST_DATABASE_URL_VALUE",
    },
)
class TestEnvVariables(TestCase):
    def test_env_variables_host_value(self):
        host = EnvVariables.get_host()
        self.assertEqual(host, "TEST_HOST_VALUE")

    def test_env_variables_token_value(self):
        token = EnvVariables.get_token()
        self.assertEqual(token, "TEST_TOKEN_VALUE")

    def test_env_variables_tmax_value(self):
        tmax = EnvVariables.get_t_max()
        self.assertEqual(tmax, "TEST_T_MAX_VALUE")

    def test_env_variables_tmin_value(self):
        tmin = EnvVariables.get_t_min()
        self.assertEqual(tmin, "TEST_T_MIN_VALUE")

    def test_env_variables_database_url_value(self):
        db_url = EnvVariables.get_db_url()
        self.assertEqual(db_url, "TEST_DATABASE_URL_VALUE")
