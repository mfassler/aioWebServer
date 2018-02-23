
import logging
from aiohttp import web
import aiohttp_jinja2
#import config


@aiohttp_jinja2.template('index.html')
async def Index(request):
    logging.info('This is Index...')

    myVars = {
        'line_a': 'this is line A',
        'line_b': '   *THIS* is Ceti Alpha FIVE!!!!  ',
        'line_c': 'this is line,... uh,  wait, what?',
    }

    return myVars


