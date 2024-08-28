import { createClient } from 'redis';

// Create a subscriber client
const email_sub = createClient();
email_sub.on('connect', () => {
    console.log('Redis connected to the server');
    
}).on('error', (error) => { console.log('Redis client not connected to the server: ', err)}).connected;

//Defining the Subscription class
email_sub.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        email_sub.unsubscribe('holberton school channel');
        email_sub.quit();
    }
});

// Subscribe to the redis channel
email_sub.subscribe('holberton school channel', (message, channel) => {
     if (message){
     console.log(message);
    }
});
