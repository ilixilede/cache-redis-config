# cache-redis-config
======================

## Description
-------------
cache-redis-config is a Node.js module that provides a simple way to configure and manage Redis cache settings in a Node.js application.

## Features
-----------
* Lightweight and efficient Redis cache management
* Easy configuration through a simple API
* Support for various Redis data types, including strings, hashes, lists, sets, and zsets
* Automatic cache expiration and invalidation
* Integration with popular Node.js frameworks, including Express.js and Koa.js

## Technologies Used
--------------------
* Node.js (>= 14.17.0)
* Redis (>= 6.2.4)
* ES6+ JavaScript
* Jest (>= 27.4.7) for unit testing

## Installation
--------------

### Prerequisites
* Install Node.js (>= 14.17.0) on your system
* Install Redis (>= 6.2.4) on your system
* Install a package manager, such as npm or yarn, to install dependencies

### Installation Steps
1. Clone the repository: `git clone https://github.com/username/cache-redis-config.git`
2. Change into the project directory: `cd cache-redis-config`
3. Install dependencies: `npm install` or `yarn install`
4. Link the module: `npm link` or `yarn link`
5. Require the module in your Node.js application: `const cache = require('cache-redis-config');`

## Usage
-----

### Configuration
To use the cache-redis-config module, first create a configuration file, such as `config.js`, with the following content:
```javascript
const config = {
  redis: {
    host: 'localhost',
    port: 6379,
    db: 0,
  },
  cache: {
    ttl: 3600, // 1 hour
    max: 100,
  },
};

module.exports = config;
```
### API
The cache-redis-config module provides the following API:
* `cache.set(key, value, [ttl])`: Set a cache value
* `cache.get(key)`: Get a cache value
* `cache.delete(key)`: Delete a cache value
* `cache.hget(key, field)`: Get a hash field value
* `cache.hset(key, field, value)`: Set a hash field value
* `cache.hdel(key, field)`: Delete a hash field value

## Contributing
--------------

Contributions are welcome! Please submit a pull request with a clear description of the changes made.

## License
---------

cache-redis-config is released under the MIT License.

## Acknowledgments
-----------------

cache-redis-config is built on top of the excellent Redis Node.js client.