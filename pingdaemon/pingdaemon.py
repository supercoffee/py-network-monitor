import sys
sys.path.append('framework')
import pingparsing
from framework import Application, Plugin
from sqlite3 import Connection
from pingparsing import PingResult


class PingPlugin(Plugin):

    name = 'ping'

    def prepare_db(self, db: Connection):

        db.execute("""
            CREATE TABLE IF NOT EXISTS ping_results (id INTEGER PRIMARY KEY, destination TEXT, packet_transmit INTEGER,
              packet_receive INTEGER, packet_loss_rate REAL, packet_loss_count INTEGER, rtt_min REAL, rtt_avg REAL,
              rtt_max REAL, packet_duplicate_rate REAL,packet_duplicate_count INTEGER, timestamp DATETIME)
        """)

    def run(self, app: Application):
        """
        PingResult(destination='8.8.8.8', packet_transmit=10, packet_receive=10, packet_loss_rate=0.0,
            packet_loss_count=0, rtt_min=7.881, rtt_avg=8.76, rtt_max=9.856, rtt_mdev=0.7, packet_duplicate_rate=None,
            packet_duplicate_count=None)

        :return:
        """
        transmitter = pingparsing.PingTransmitter()
        transmitter.destination_host = "8.8.8.8"
        transmitter.waittime = 10
        raw_output = transmitter.ping()
        parser = pingparsing.PingParsing()
        ping_results = parser.parse(raw_output)
        app.in_db_transaction(lambda db: insert_result(db, ping_results))

def insert_result(db: Connection, results: PingResult):
    print(results)
    # db.execute("""
    #     INSERT INTO ping_results
    # """)

if __name__ == '__main__':
    app = Application()
    app.register_module(PingPlugin())
    app.run()
