import pika
import os

# from dotenv import load_dotenv

# load_dotenv()
# want to read .env


def produce(host, body):

    rabbitmq_username = os.getenv("RABBITMQ_USER")
    rabbitmq_password = os.getenv("RABBITMQ_PASS")
    print(rabbitmq_username, rabbitmq_password)

    credentials = pika.PlainCredentials(rabbitmq_username, rabbitmq_password)

    parameters = pika.ConnectionParameters(host=host, credentials=credentials)

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.exchange_declare(exchange="jobs", exchange_type="direct")
    channel.queue_declare(queue="router_jobs")
    channel.queue_bind(
        queue="router_jobs", exchange="jobs", routing_key="check_interfaces"
    )
    channel.basic_publish(exchange="jobs", routing_key="check_interfaces", body=body)
    connection.close()


if __name__ == "__main__":
    produce("localhost", "192.168.1.44")
# this ip is string
