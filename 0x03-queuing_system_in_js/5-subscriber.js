import { createClient } from "redis";

const redis = createClient()

redis.on('connect', () => {
    console.log("Redis client connected to the server")
}
);

redis.on('error', (err) => {
    console.error('Redis client notubscription: connected to the server:', err)
})

//Defining the Subscription class
redis.on('message', (channel, message) => {
    console.log(message);
    if (message === 'KILL_SERVER') {
        redis.unsubscribe();
        redis.quit();
    }
});

redis.subscribe('holberton school channel', (err, message) => {
    if (err) {
        console.error('Subscription fail, Robert');
        return
    } else if (message === 'KILL_SERVER') {
        redis.quit()
    } else
        console.log(message)
});
