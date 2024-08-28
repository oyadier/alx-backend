// Description: Redis publisher
import { createClient } from 'redis';

// Create a publisher client
const email_pub = createClient();
email_pub.on('connect', () => {
    console.log('Redis connected to the server');
    
}).on('error', (error) => { console.log('Redis client not connected to the server: ', error)});

// Publish a message to the redis channel
function publishMessage (message, time) {
 
    setTimeout(() => {
        console.log(`About to send ${message}`);
        email_pub.publish('holberton school channel', message, (error) => {
            if (error) {
                console.error(error);
                return;
            }
        })
    }, time);
};
publishMessage("Holberton Student #1 starts course", 1000);
publishMessage("Holberton Student #2 starts course", 2000);
publishMessage("KILL_SERVER", 3000);
publishMessage("Holberton Student #3 starts course", 4000);
