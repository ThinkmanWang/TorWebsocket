# -*- coding: utf-8 -*-

import logging
import tornado.escape
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket
import os.path
import uuid

class MainController(tornado.web.RequestHandler):
    # def get(self):
    #     self.write("Hello, world")

    def get(self):
        self.render("index.html")