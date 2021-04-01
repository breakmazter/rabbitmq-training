import os

# why do you need base_dir?
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# pgbouncer)))?
db_environment = os.environ.get('oc_db_environment', 'pgbouncer-dev')

# CONFIGS FOR RABBITMQ
QUEUE_DRIVER = 'rabbitmq'
RABBITMQ_HOST = '34.94.7.254'
RABBITMQ_PORT = 5672
RABBITMQ_VHOST = '/'
RABBITMQ_LOGIN = 'mazan'
# security you know
RABBITMQ_PASSWORD = 'mazan'

RABBITMQ_URL = f'''amqp://{RABBITMQ_LOGIN}:{RABBITMQ_PASSWORD}@{RABBITMQ_HOST}:{RABBITMQ_PORT}'''
# No usage for socket_timeout
RABBITMQ_SCOCKET_TIMEOUT = 10
# No usage for heartbeat
RABBITMQ_HEARTBEAT = 0
