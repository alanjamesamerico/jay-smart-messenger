#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bottle import debug, run
import os
from application import app
   
debug(True)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8082))
    run(app, reloader=True, host='localhost', port=port)
