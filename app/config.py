from os import environ as env


class Config:
    MONGODB_URL = env["MONGODB_URL"]
