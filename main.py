# -*- coding: utf-8 -*-

import sys
import os
import asyncio

import tornado.ioloop
import tornado
import tornado.process
import tornado.web

from tornado.tcpserver import TCPServer
from tornado.iostream import StreamClosedError
from tornado import gen
from tornado.platform.asyncio import AsyncIOMainLoop
from tornado.netutil import *

class MyApp(tornado.web.Application):
    def __init__(self):
        from controller.MainController import MainController
        from controller.ThinkWSController import ThinkWSController

        handlers = [(r"/", MainController), (r"/gameserver", ThinkWSController)]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates")
            # cookie_secret="2hcicVu+TqShDpfsjMWQLZ0Mkq5NPEWSk9fi0zsSt3A=",
            # xsrf_cookies=True,
        )
        super().__init__(handlers, **settings)


def main():
    app = MyApp()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()