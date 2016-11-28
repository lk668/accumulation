#!/usr/bin/env python
import pika
import sys
import threading
import logging

logger = logging.getLogger("likai")
handler = logging.FileHandler("/home/ebupt1/rabbit/ofagent.txt")
logger.addHandler(handler)
logger.setLevel(logging.NOTSET)


class myThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.exchange_declare(exchange='ofagent',type='fanout')

        result = channel.queue_declare(exclusive=True)
        queue_name = result.method.queue

        channel.queue_bind(exchange='ofagent',queue=queue_name)

        print ' [*] Waiting for logs. To exit press CTRL+C'

        def callback(ch, method, properties, body):
            print " [x] %r" % (body,)
            function(body)
            #logger.error(body)
        channel.basic_consume(callback,queue=queue_name,no_ack=True)
        channel.start_consuming()
def function(message):
    logger.error(message)
thread = myThread()
thread.start()
