#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Txema Vicente"
__license__ = "MIT"
__version__ = "0.0.1"

import sys
import argparse
import paho.mqtt.client as mqtt


class Broker(object):

    def __init__(self, host, port=1883):
        self.host = host
        self.port = port
        self.client = mqtt.Client()
        

    def auth(self, user, password):
        self.client.username_pw_set(user, password)


    def connect(self, on_connect=None, on_message=None):

        def on_disconnect(client, userdata, rc):
            if rc != 0: print("Error: %s" % rc)

        self.client.on_disconnect = on_disconnect

        if on_connect: self.client.on_connect = on_connect
        if on_message: self.client.on_message = on_message

        self.client.connect(self.host, self.port, 60)
        
        
    def subscribe(self, topic="#"):

        def on_connect(client, userdata, flags, rc):
            if rc==0:
                print("Connected to %s:%s/%s" % (self.host, self.port, topic))
                print("Use CTRL+C to exit")
            else:
                print("Error %s" % rc)
            self.client.subscribe(topic)

        def on_message(client, userdata, msg):
            try:
                print("%s %s" % (msg.topic, repr(msg.payload)))
            except Exception as e:
                print("Error: %s" % e)

        self.connect(on_connect, on_message)
        try:
            self.client.loop_forever()
        except KeyboardInterrupt:
            self.client.disconnect() 

    
    def publish(self, topic, payload):

        def on_connect(client, userdata, flags, rc):
            if rc!=0:
                print("Error %s" % rc)
                sys.exit(rc)
            client.publish(topic, payload=payload)
            self.sent = True

        self.sent = False
        self.connect(on_connect)
        while not self.sent: self.client.loop()
        self.client.disconnect()




def main():

    parser = argparse.ArgumentParser(description="Simple MQTT publish/subscribe tool", add_help=False)
    parser.add_argument('--help', action='help', help="show this help message and exit.")
    parser.add_argument("--sub", dest="subscribe", help="Subscribe and listen topic, use CTRL+C to exit", action='store_true')
    parser.add_argument("-h", dest="host",     help="host name or IP address")
    parser.add_argument("-p", dest="port",     help="set port number, default is 1883", type=int, default=1883)
    parser.add_argument("-t", dest="topic",    help="set topic")
    parser.add_argument("-m", dest="message",  help="message to publish")
    parser.add_argument("-u", dest="user",     help="set user")
    parser.add_argument("-P", dest="password", help="password")
    
    args = parser.parse_args()

    if args.host is None:
        print "Error: Please provide a MQTT server host to connect to.\n"
        parser.print_help()
        sys.exit(10)
  
    if args.topic is None:
        print "Error: Please provide a MQTT topic.\n"
        parser.print_help()
        sys.exit(11)

    broker = Broker(args.host, args.port)

    if args.user is not None:
        broker.auth(args.user, args.password)
        
    if args.subscribe:
        broker.subscribe(args.topic)
    else:
        broker.publish(args.topic, args.message)

  

if __name__ == "__main__": main()
