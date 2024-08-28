import { createClient } from 'redis';
import redis from 'redis'

const client = createClient()
client.on('error', err => console.log('Redis client not connected to the server: ', err));
client.on('connect', () => console.log('Redis client connected to the server'))
    .connected;


const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, (_, reply) => {
        redis.print('Reply: ' + reply)
        client.quit();
    });
}

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (_, reply) => {
        console.log(reply)
    })
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
