#!/usr/bin/env python
# -*- coding:utf-8 -*-

from websocket_server import WebsocketServer

#def new_client(client, server):
#    server.send_mesage_to_all("messege to all")

def send_msg_allclient(client,server,message):
    print message
    server.send_message_to_all(message)

server = WebsocketServer(9999,host="192.168.122.252")
#server.set_fn_new_client(new_client)
server.set_fn_message_received(send_msg_allclient)
server.run_forever()

