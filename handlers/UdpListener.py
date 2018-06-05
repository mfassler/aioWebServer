
import logging
import asyncio
import config

app = None


def setup(_app):
    global app
    app = _app
    app.on_startup.append(start_background_tasks)
    app.on_cleanup.append(cleanup_background_tasks)


class UDP_Receiver(asyncio.DatagramProtocol):
    def connection_made(self, transport):
        logging.debug('connection_made: %s' % (transport))
        self.transport = transport

    def datagram_received(self, data, addr):
        global app
        logging.debug('rx UDP: %s' % (data))
        if 'websockets' in app:
            for _ws in app['websockets']:
                logging.debug('_ws:  %s' % (_ws))
                asyncio.ensure_future(_ws.send_str(str(data, 'utf-8')))


async def start_background_tasks(app):
    logging.debug('this is start_background_tasks()')
    t = app.loop.create_datagram_endpoint(UDP_Receiver, 
                                          local_addr=(config.UDP_LISTEN_HOST, config.UDP_LISTEN_PORT))
    app['udp_listener'] = app.loop.create_task(t)


async def cleanup_background_tasks(app):
    app['udp_listener'].cancel()
    await app['udp_listener']






