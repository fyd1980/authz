from os import environ


class Config:
    #### Global Configuration ####
    ENV = environ.get("SKOB_AUTZ_ENV", "production")
    DEBUG = int(environ.get("SKOB_AUTHZ_DEBUG", "0"))
    TESTING = int(environ.get("SKOB_AUTHZ_TESTING", "0"))

    #### DataBase Configuration ####
    SQLALCHEMY_DATABASE_URI = environ.get("SKOB_AUTHZ_DATABASE_URI", None)
    SQLALCHEMY_TRACK_MODIFICATION = TESTING

    #### User Configuration ####
    USER_DEFAULT_ROLE = environ.get("SKOB_AUTHZ_USER_DEFAULT_ROLE", "member")
    USER_DEFAULT_STATUS = environ.get("SKOB_AUTHZ_USER_DEFAULT_STATUS", "inactive")
