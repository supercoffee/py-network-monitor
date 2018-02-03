from networkmonitor.framework import Application
from networkmonitor.pingdaemon import PingPlugin
from networkmonitor.speedtest import SpeedTestPlugin


# TODO
# parse config file
# register application modules
# run modules, prepare db, or spin up daemon


if __name__ == '__main__':
    app = Application()
    app.register_module(PingPlugin())
    app.register_module(SpeedTestPlugin())
    app.run()


#
# def run():
#     parser = argparse.ArgumentParser(description='Run a speed test using speedtest-cli and log the results to sqlite')
#     parser.add_argument('action', choices=['init', 'run', 'import'])
#     parser.add_argument('--file', type=argparse.FileType('rb'))
#     args = parser.parse_args()
#
#     if args.action == 'init':
#         prepare_db()
#     elif args.action == 'run':
#         run_test()
#     elif args.action == 'import':
#         import_from_file(args.file)
#
#
# if __name__ == '__main__':
#     run()
