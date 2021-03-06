import argparse
import json
import sqlite3

import speedtest


def run_test():
    servers = []
    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()
    import_results(s.results.dict())


def import_from_file(f):
    results = json.load(f)
    import_results(results)


def import_results(results_dict):
    server = results_dict['server']
    del results_dict['server']
    del results_dict['share']

    results_dict['server'] = server['id']

    conn = sqlite3.connect('speed-test-results.db')
    conn.execute(
        """INSERT INTO servers VALUES (:id, :latency, :name, :url, :country, :lon, :lat, :cc, :host, :sponsor, :url2, :d)""",
        server)
    conn.execute("""INSERT INTO test_results  (bytes_sent, download, timestamp, bytes_received, ping, upload, server)
                    VALUES (:bytes_sent, :download, :timestamp, :bytes_received, :ping, :upload, :server)""",
                 results_dict)
    conn.commit()
    conn.close()


def prepare_db():
    conn = sqlite3.connect('speed-test-results.db')

    conn.execute("""
        CREATE TABLE test_results (id INTEGER PRIMARY KEY , bytes_sent REAL, download REAL, timestamp DATETIME,
        bytes_received REAL, ping REAL, upload REAL, server INTEGER)
        """)
    conn.execute("""
        CREATE TABLE servers (id INTEGER, latency REAL, name TEXT, url TEXT, country TEXT, longitude REAL, latitude REAL, country_code TEXT,
                                host TEXT, sponsor TEXT, url2 TEXT, d_what_is_this REAL)
        """)

    conn.commit()
    conn.close()


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def get_all_speedtest_results():
    conn = sqlite3.connect('speed-test-results.db')
    conn.row_factory = dict_factory
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM test_results""")
    results = [dict(r) for r in cursor]
    cursor.close()
    conn.close()
    return results


def run():
    parser = argparse.ArgumentParser(description='Run a speed test using speedtest-cli and log the results to sqlite')
    parser.add_argument('action', choices=['init', 'run', 'import'])
    parser.add_argument('--file', type=argparse.FileType('rb'))
    args = parser.parse_args()

    if args.action == 'init':
        prepare_db()
    elif args.action == 'run':
        run_test()
    elif args.action == 'import':
        import_from_file(args.file)


if __name__ == '__main__':
    run()
