import sqlite3


class Plugin(object):

    @property
    def name(self):
        return self.__name__

    def prepare_db(self, connection):
        """
        Create database tables for this plugin
        :param connection:
        :return:
        """
        pass

    def run(self, app):
        """
        Run the main command and do something useful with the output
        :param app:
        :return:
        """
        pass

class Application(object):

    def __init__(self):
        super().__init__()
        self.plugins = []

    def register_module(self, plugin: Plugin):
        self.plugins.append(plugin)

    def run(self):

        for plugin in self.plugins:
            self.in_db_transaction(plugin.prepare_db)

        for plugin in self.plugins:
            plugin.run(self)


    def db_connection(self):
        conn = sqlite3.connect('speed-test-results.db')
        return conn

    def in_db_transaction(self, func: sqlite3.Connection):
        conn = self.db_connection()
        func(conn)
        conn.commit()
        conn.close()

