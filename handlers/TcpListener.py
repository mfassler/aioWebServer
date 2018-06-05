
import logging
import asyncio
import config

app = None


def setup(_app):
    global app
    app = _app
    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)


#allTcpConnections = []

class TCP_Connections(asyncio.Protocol):
    def connection_made(self, transport):
        logging.debug('connection_made: %s' % (transport))
        self.transport = transport

    # def connection_lost()

    def data_received(self, data):
        print('   Received data: %s' % (data))

    def eof_received(self):
        print(' eof, mofos!')


async def start_background_tasks(app):
    logging.debug('this is TCP: start_background_tasks()')
    t = app.loop.create_server(TCP_Connections, host=config.TCP_LISTEN_HOST, 
                                                port=config.TCP_LISTEN_PORT)
    app['tcp_server'] = app.loop.create_task(t)


async def cleanup_background_tasks(app):
    app['tcp_server'].cancel()
    await app['tcp_server']


