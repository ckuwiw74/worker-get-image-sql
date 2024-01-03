import pika

def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")

credentials = pika.PlainCredentials('TMDG2022', 'TMDG2022')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('rmq2.pptik.id', 5672, '/', credentials)
)

channel = connection.channel()

queue = 'rmqlatihan'
channel.queue_declare(queue=queue, durable=False)

print(f" [*] Waiting for messages in {queue}. To exit, press CTRL+C")

channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

try:
    channel.start_consuming()
except KeyboardInterrupt:
    connection.close()