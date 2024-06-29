
import { createClient, print } from 'redis';
var client = createClient()

client.on('connect', () => {
    console.log('Redis client connected to the server')
    client.hset('HolbertonSchools',
        'Portland', 50,
        'Seattle', 80,
        'New York', 20,
        'Bogota', 20,
        'Cali', 40,
        'Paris', 2, (err, reply) => {
            if (err) {
                console.error(`Error occures: ${err}`)
            } else {
                console.log(`Reply: ${reply}`)

            }
            client.hgetall('HolbertonSchools', function (err, object) {
                console.log(object);
            });
            client.quit();
        }
    );
});
