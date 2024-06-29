import { createClient } from "redis";
const pub = createClient()

pub.on('connect', () => {
    console.log('Publisher: Redis client connected to the server');
});
pub.on('error', (error) => console.log('Redis client not connected to the server: ', error));

//Defining the publisher
function publishMessage(message, time) {
    connectTimeout: time
    console.log(`About to send ${message}`);
    pub.publish('holberton school channel',
        message,
        (err) => {
            if (err) {
                console.error(err)
                return
            };
        });
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);