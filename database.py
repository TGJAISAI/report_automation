import os
import pandas as pd
import pymysql

from dotenv import load_dotenv
from sshtunnel import SSHTunnelForwarder

load_dotenv()


class DatabaseHelper():
    """Provides the database connection.
    """

    def __init__(self):

        self.ssh_host = os.getenv('SSH_HOST')
        self.ssh_username = os.getenv('SSH_USERNAME')
        self.ssh_password = os.getenv('SSH_PASSWORD')
        self.db_host = os.getenv('DB_HOST')
        self.dbb_host = os.getenv('DBB_HOST')
        self.db_user = os.getenv('DB_USERNAME')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_name = os.getenv('DB_NAME')

    def __connect__(self):

        # self.tunnel = SSHTunnelForwarder(
        #     (self.ssh_host, 22),
        #     ssh_username=self.ssh_username,
        #     ssh_password=self.ssh_password,
        #     remote_bind_address=(self.db_host, 3306)
        # )

        # self.tunnel.start()

        self.ssh_connection = pymysql.connect(
            host=self.db_host,
            user=self.db_user,
            passwd=self.db_password,
            db=self.db_name,
            port=3306
        )

        self.cur = self.ssh_connection.cursor()

    def __disconnect__(self):
        self.cur.close()
        self.ssh_connection.close()
        # self.tunnel.stop()
        # self.tunnel.close()

    def fetch(self, sql):
        """Returns the result in a dataframe.
        """

        self.__connect__()
        result = pd.read_sql(sql, self.ssh_connection)
        self.__disconnect__()
        return result