import os

class Environment:
    def __init__(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@localhost/dbname")

env = Environment()