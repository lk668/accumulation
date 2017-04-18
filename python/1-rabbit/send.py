#!/usr/bin/env python
#coding=utf8
import pika
 
class Sender(object):
    def __init__(self, host):
        """
        self.connnection:连接rabbitmq服务器
        self.channel:定义队列
        self.result:定义返回队列
        """
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = self.result.method.queue
        self.channel.basic_consume(self.on_response,no_ack=True,queue=self.callback_queue)
 
    def on_response(self, ch, method, props, body):
        self.response = "success"

    def request(self, body):
        self.response = None
        self.channel.basic_publish(exchange='',
                                   routing_key='test',
                                   properties=pika.BasicProperties(
                                         reply_to = self.callback_queue,
                                         ),
                                   body=body)
        #接收返回的数据
        while self.response is None:
            self.connection.process_data_events()
        return self.response
 
sender = Sender('127.0.0.1')
response = sender.request("request")
print " [x] Requesting request"
print " [.] Got %s"%response
