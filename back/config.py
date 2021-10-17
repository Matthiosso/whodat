class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@127.0.0.1:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_RESULT_BACKEND = 'amqp://rabbitmq:rabbitmq@localhost:5672/'
    CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@localhost:5672/'
    CELERY_IMPORTS = ('__main__', )


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
