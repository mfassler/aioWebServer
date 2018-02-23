
import logging
import aiohttp
from aiohttp import web


async def WebSocket(request):

    logging.debug('This is websocket_handler()')
    logging.debug('app: ', request.app)

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    if 'websockets' not in request.app:
        request.app['websockets'] = []

    request.app['websockets'].append(ws)
    logging.info("There are %d connected websockets." % (len(request.app['websockets'])))

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            if msg.data == 'close':
                await ws.close()
            else:
                await ws.send_str(msg.data + '/answer')
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print('ws connection closed with exception %s' %
                  ws.exception())

    request.app['websockets'].remove(ws)
    logging.info('websocket connection closed')
    logging.info("There are %d connected websockets." % (len(request.app['websockets'])))


    return ws


