const new_kue = require('kue')
const process = new_kue.createQueue()

const sendNotification = (phoneNumber, message) => {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
} 
//The `push notification is the name of the job` 
 process.process('push notification',(job, done) => {
    if(job) {
            sendNotification(job.data.phoneNumber, job.data.message, done)
           // done()
    }
});
