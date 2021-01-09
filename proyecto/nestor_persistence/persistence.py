import pymongo
import os
import logging
import pika
import time

time.sleep(50)
DATABASE="nestor"
COLLECTION="mensajes"
HOST = os.environ['RABBITMQ_HOST']
MONGO_HOST = os.environ['MONGO_HOST']
PORT=os.environ["MONGO_PORT"]



def connect_database(database_name):
	myclient = pymongo.MongoClient(MONGO_HOST,int(PORT))

	db = myclient[database_name]
	return db

def write_message_in_database(message, database_name, collection_name):
	database=connect_database(database_name)
	my_doc = {"message":message}
	print("writing a new document in the database:"+str(my_doc))
	database[collection_name].insert_one(my_doc)



def connect_rabbitmq(exchange, queue, routing_key):

	connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
	channel = connection.channel()
	channel.exchange_declare(exchange=exchange, exchange_type='topic', durable=True)

	result = channel.queue_declare(queue=queue, exclusive=False, durable=True)
	queue_name=result.method.queue

	channel.queue_bind(exchange=exchange, queue=queue_name, routing_key=routing_key)
	
	return channel


def on_message(ch, method, properties, body):
	print("Message received:"+body.decode())
	message = body.decode()
	write_message_in_database(message, DATABASE, COLLECTION)

def consume_menssage(exchange, queue, routing_key):
	print(' [*] waiting for messages. to exit press ctrl+c')

	channel = connect_rabbitmq(exchange, queue, routing_key)

	channel.basic_consume(queue=queue, on_message_callback=on_message, auto_ack= True)

	channel.start_consuming()

	
consume_menssage("nestor","persistence","persistence")




