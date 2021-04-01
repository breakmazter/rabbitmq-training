import pika
import math
from settings import *


def sqr_root(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        # TODO remove prints as that's bad idea to output info to stdout in docker (which runs on vm)
        print(f"x1 = {x1}, x2  = {x2}")
    elif discr == 0:
        x = -b / (2 * a)
        print(f"x1 = {x}, x2  = {x}")
    else:
        print(f"Not roots")


def main():
    credentials = pika.PlainCredentials(RABBITMQ_LOGIN, RABBITMQ_PASSWORD)
    # TODO add different connection parameters essential for stability like connection_attempts, heartbeat and others
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST, port=RABBITMQ_PORT, virtual_host=RABBITMQ_VHOST, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='mazan_green_queue', durable=True)
    print('[Consumer] Waiting for messages. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        mass_str = body.decode("utf-8")
        mass = mass_str.split(" ")
        a, b, c = int(mass[0]), int(mass[1]), int(mass[2])
        print(f"a = {a}, b = {b}, c = {c}")
        print(sqr_root(a, b, c))
        # use multiple=True param as it enables to ack many messages once speeding up performance
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    
    # better to put "consuming" in different method to separate development logic
    channel.basic_consume(on_message_callback=callback, queue='mazan_green_queue')
    channel.start_consuming()


if __name__ == "__main__":
    main()
# One blank line in the end)
