#!/usr/bin/env python3

import sys
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

#import os
import logging
import asyncio
import aiohttp
from aiohttp import web
import aiohttp_jinja2
import jinja2

import config
import handlers


logging.basicConfig(level=logging.DEBUG)


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

handlers.udp_setup(app)
handlers.tcp_setup(app)

app.router.add_static('/static/', path='static')

app.router.add_get('/', handlers.Index)
app.router.add_get('/ws', handlers.WebSocket)

web.run_app(app, host=config.HTTP_LISTEN_HOST, port=config.HTTP_LISTEN_PORT)


