import os
import yaml
import logging

class Config:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = self.load_config()

    def load_config(self):
        if not os.path.exists(self.config_path):
            logging.error(f"Config file not found at {self.config_path}")
            return {}
        with open(self.config_path, 'r') as f:
            return yaml.safe_load(f)

    def get_config(self):
        return self.config

class CacheConfig:
    def __init__(self, config):
        self.config = config
        self.redis_config = self.load_redis_config()

    def load_redis_config(self):
        if 'redis' not in self.config:
            logging.error("Redis config not found in config file")
            return {}
        return self.config['redis']

    def get_redis_config(self):
        return self.redis_config

class RedisConfig:
    def __init__(self, config):
        self.config = config
        self.host = self.get_host()
        self.port = self.get_port()
        self.db = self.get_db()
        self.password = self.get_password()

    def get_host(self):
        return self.config.get('host', 'localhost')

    def get_port(self):
        return self.config.get('port', 6379)

    def get_db(self):
        return self.config.get('db', 0)

    def get_password(self):
        return self.config.get('password', None)

class Cache:
    def __init__(self, config):
        self.config = config
        self.redis_config = RedisConfig(self.config.get_redis_config())
        self.client = self.create_client()

    def create_client(self):
        # Assuming you are using redis-py
        import redis
        return redis.Redis(host=self.redis_config.host, port=self.redis_config.port, db=self.redis_config.db, password=self.redis_config.password)

    def get_client(self):
        return self.client