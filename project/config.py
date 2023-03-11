import os


class Server():

    BASE_PATH = "/"
    MYSQL_HOST = os.getenv("MYSQL_HOST", default="mysql")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", default="db_bibliotec")
    MYSQL_USER = os.getenv("MYSQL_USER", default="root")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", default="123456")
    MYSQL_PORT = os.getenv("MYSQL_PORT", default=3307)

    def get_base_path(self):
        return self.BASE_PATH
