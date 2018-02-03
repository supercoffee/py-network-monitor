import sqlite3
import sched
import time


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



class PeriodicScheduler(object):
    def __init__(self):
        self.scheduler = sched.scheduler(time.time, time.sleep)

    def setup(self, interval, action, actionargs=()):
        action(*actionargs)
        self.scheduler.enter(interval, 1, self.setup,
                             (interval, action, actionargs))

    def run(self):
        self.scheduler.run()


class Application(object):
    def __init__(self):
        super().__init__()
        self.plugins = {}

    def register_module(self, plugin: Plugin):
        self.plugins[plugin.name] = plugin

    def run(self):

        for plugin in self.plugins.values():
            self.in_db_transaction(plugin.prepare_db)

        for plugin in self.plugins.values():
            plugin.run(self)

    def daemon(self):

        # create a scheduler
        scheduler = PeriodicScheduler()
        for name, plugin in self.plugins.items():
            scheduler.setup(60, plugin.run, (self,))
        scheduler.run()

    def db_connection(self):
        conn = sqlite3.connect('speed-test-results.db')
        return conn

    def in_db_transaction(self, func: sqlite3.Connection):
        conn = self.db_connection()
        func(conn)
        conn.commit()
        conn.close()
