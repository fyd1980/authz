from os import environ

class config:

    ENV = environ.get("SKOB_AUTZ_ENV", "production")
    DEBUG = int(environ.get("SKOB_AUTHZ_DEBUG", "0"))
    TESTING = int(environ.get("SKOB_AUTHZ_TESTING", "0"))