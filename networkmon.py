from networkmonitor.framework import Application
from networkmonitor.pingdaemon import PingPlugin

if __name__ == '__main__':
    app = Application()
    app.register_module(PingPlugin())
    app.run()
