0x03. Queuing System in JS
Description
This project focuses on implementing a queuing system using Node.js, Redis, Kue, and Express. It covers Redis client operations, async operations, pub/sub messaging, job queues, and building a basic Express app interacting with Redis and a queue system.
Requirements

Ubuntu 18.04
Node.js 12.x
Redis 5.0.7 or higher
All files must end with a new line
A README.md file is mandatory
Code must use .js extension
Install dependencies with npm install

Setup

Install Redis:wget http://download.redis.io/releases/redis-6.0.10.tar.gz
tar xzf redis-6.0.10.tar.gz
cd redis-6.0.10
make
src/redis-server &


Verify Redis:src/redis-cli ping
# Should return PONG


Set initial Redis value:src/redis-cli
set ALX School
get ALX
# Should return "School"


Copy dump.rdb from redis-6.0.10 to project root:cp redis-6.0.10/dump.rdb .


Install Node dependencies:npm install



Tasks

Node Redis Client: Connect to Redis server (0-redis_client.js).
Basic Operations: Set and get values in Redis (1-redis_op.js).
Async Operations: Use async/await with Redis (2-redis_op_async.js).
Advanced Operations: Store and retrieve hash values (4-redis_advanced_op.js).
Publisher/Subscriber: Implement pub/sub messaging (5-subscriber.js, 5-publisher.js).
Job Creator: Create jobs using Kue (6-job_creator.js).
Job Processor: Process jobs with Kue (6-job_processor.js).
Track Progress: Create and track multiple jobs (7-job_creator.js, 7-job_processor.js).
Job Creation Function: Modular job creation (8-job.js).
Job Creation Tests: Test job creation (8-job.test.js).
Stock Management: Build Express app with Redis for stock (9-stock.js).
Seat Reservation: Build Express app with Redis and Kue for seat reservations (100-seat.js).

Repository

GitHub: alx-backend
Directory: 0x03-queuing_system_in_js

