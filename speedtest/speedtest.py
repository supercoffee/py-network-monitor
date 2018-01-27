import argparse
import json
import sqlite3
import subprocess

def run_test():
    # run speed test command
    cmd_output = subprocess.run(['speedtest-cli', '--json'], stdout=subprocess.PIPE)
    results = json.loads(cmd_output.stdout)
    import_results(results)


def import_from_file(f):
    results = json.load(f)
    import_results(results)


def import_results(results_dict):

    server = results_dict['server']
    del results_dict['server']
    del results_dict['share']

    results_dict['server'] = server['id']

    conn = sqlite3.connect('speed-test-results.db')
    conn.execute("""INSERT INTO servers VALUES (:id, :latency, :name, :url, :country, :lon, :lat, :cc, :host, :sponsor, :url2, :d)""", server)
    conn.execute("""INSERT INTO test_results VALUES (:bytes_sent, :download, :timestamp, :bytes_received, :ping, :upload, :server)""", results_dict)
    conn.commit()
    conn.close()



def prepare_db():
    conn = sqlite3.connect('speed-test-results.db')

    conn.execute("""
        CREATE TABLE test_results (bytes_sent REAL, download REAL, timestamp DATETIME, bytes_received REAL, ping REAL, upload REAL, server INTEGER)
        """)
    conn.execute("""
        CREATE TABLE servers (id INTEGER, latency REAL, name TEXT, url TEXT, country TEXT, longitude REAL, latitude REAL, country_code TEXT,
                                host TEXT, sponsor TEXT, url2 TEXT, d_what_is_this REAL)
        """)
    conn.commit()
    conn.close()



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