import pika

# Establish a connection to the RabbitMQ server
credentials = pika.PlainCredentials('TMDG2022', 'TMDG2022')
connection = pika.BlockingConnection(
    pika.ConnectionParameters('rmq2.pptik.id', 5672, '/', credentials)
)
channel = connection.channel()

queue = 'rmqlatihan'

# Function to send a message to the queue
def send_message():
    msg = input('Enter a message to send: ')
    channel.queue_declare(queue=queue, durable=False)
    channel.basic_publish(exchange='', routing_key=queue, body=msg)
    print(f" [x] Sent {msg}")

    answer = input('Do you want to send another message? (yes/no): ')
    if answer.lower() == 'yes':
        send_message()
    else:
        connection.close()

send_message()  # Start the process by sending the first message