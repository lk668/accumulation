#!/usr/bin/env python
#coding=utf8
import pika

class Receiver(object):
	def __init__(self, host):
		"""
        self.connnection:连接rabbitmq服务器
        self.channel:定义队列
        self.result:定义返回队列
        """
		self.connection =  pika.BlockingConnection(pika.ConnectionParameters(host=host))
		self.channel = self.connection.channel()
		self.channel.queue_declare(queue="test")
		self.channel.basic_qos(prefetch_count=1)
		self.channel.basic_consume(self.request, queue='test')

	def request(self, ch, method, properties, body):
		print "Receive %s"%body
		response = "success"
		ch.basic_publish(exchange='',
						routing_key=properties.reply_to,
                    	body=response)
		ch.basic_ack(delivery_tag = method.delivery_tag)

receiver = Receiver("127.0.0.1")
receiver.channel.start_consuming()
