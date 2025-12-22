# utils.py

import logging
from typing import Optional

class ConfigError(Exception):
    """Raised when config is invalid"""
    pass

def get_config_property(config: dict, section: str, property: str, default: Optional[str] = None) -> str:
    """Get config property from specified section"""
    try:
        return config.get(section, {}).get(property, default)
    except KeyError:
        logging.error(f"Invalid config: {config}, section: {section}, property: {property}")
        raise ConfigError(f"Invalid config: {config}, section: {section}, property: {property}")

def get_redis_config(config: dict) -> dict:
    """Get Redis config from config dict"""
    redis_config = {
        'host': get_config_property(config, 'redis', 'host'),
        'port': get_config_property(config, 'redis', 'port'),
        'db': get_config_property(config, 'redis', 'db'),
        'password': get_config_property(config, 'redis', 'password'),
        'max_connections': get_config_property(config, 'redis', 'max_connections')
    }
    return redis_config