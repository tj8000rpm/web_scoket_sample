#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from websocket import create_connection

ws = create_connection("ws://192.168.122.252:9999/")

for i in range(100):
    ws.send(str(i)+":hoge")
    time.sleep(1)

ws.close()
