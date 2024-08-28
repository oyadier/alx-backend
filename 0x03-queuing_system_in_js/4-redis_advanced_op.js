import { createClient } from 'redis';
import redis from 'redis'
const client = createClient()
client.on('error', err => console.log('Redis client not connected to the server: ', err));
client.on('connect', () => console.log('Redis client connected to the server'))
    .connected;


client.hset('HolbertonSchools', 'Portland', '50', () => redis.print("Reply: " + 1));
client.hset('HolbertonSchools', 'Seattle', '80', () => redis.print("Reply: " + 1));
client.hset('HolbertonSchools', 'New York', '20', () => redis.print("Reply: " + 1));
client.hset('HolbertonSchools', 'Bogota', '20', () => redis.print("Reply: " + 1));
client.hset('HolbertonSchools', 'Cali', '40', () => redis.print("Reply: " + 1));
client.hset('HolbertonSchools', 'Paris', '2', () => redis.print("Reply: " + 1));

client.hgetall('HolbertonSchools', (_, reply) => {
    console.log(reply);
})
client.quit();