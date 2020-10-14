# -*- coding: utf-8 -*-

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid
from pythinkutils.aio.common.aiolog import g_aio_logger

class ThinkWSController(tornado.websocket.WebSocketHandler):

    g_setConn = set()
    g_dictConn = {}

    def get_compression_options(self):
        # Non-None enables compression with default options.
        return {}

    def open(self):
        ThinkWSController.g_setConn.add(self)

    def on_close(self):
        ThinkWSController.g_setConn.remove(self)

    async def on_message(self, message):
        await g_aio_logger.info(message)
        for conn in ThinkWSController.g_setConn:
            try:
                conn.write_message(message)
            except Exception as ex:
                await g_aio_logger.info(ex)