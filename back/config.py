class Config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@db:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_RESULT_BACKEND = 'amqp://rabbitmq:rabbitmq@rabbitmq:5672/'
    CELERY_BROKER_URL = 'amqp://rabbitmq:rabbitmq@rabbitmq:5672/'
    CELERY_IMPORTS = ('__main__', )


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = True
