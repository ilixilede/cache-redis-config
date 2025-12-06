import os
import sys
import redis
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up Redis client
redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST', 'localhost'),
    port=int(os.getenv('REDIS_PORT', 6379)),
    db=int(os.getenv('REDIS_DB', 0))
)

# Check if Redis is up and running
if not redis_client.ping():
    print("Error: Unable to connect to Redis")
    sys.exit(1)

# Print Redis version
print("Redis Version:", redis_client.info()['redis_version'])