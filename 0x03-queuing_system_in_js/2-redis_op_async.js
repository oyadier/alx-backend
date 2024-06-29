_

import redis from 'redis';


const client = redis.createClient()
client.on('connect', () => {
    console.log('Redis client connected to the server')
});
client.on('error', (err) => { console.error('Redis client not connected to the server: ', err) }).connected

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, function (err, reply) {
        if (err) {
            console.error('Error setting value in Redis:', err);
            return;
        }
        redis.print(`Reply: ${reply}`)
        client.quit(); // Close Redis connection after operation if needed
    });
}

async function displaySchoolValue(schoolName) {
    try{
        await client.get(schoolName, function (err, reply) {
        if (err) {
            return err
        };
        console.log(reply)
    })

    }catch{

    }
  
}
displaySchoolValue('Holberton')
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
