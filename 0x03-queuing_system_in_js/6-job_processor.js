import kue from 'kue'

function sendNotification(phoneNumber, message) {
    console.log(`Sending nofication to ${phoneNumber}, with message: ${message}`)
}
var queue = kue.createQueue()
    queue.process('push_notification_code', (job, done) =>
{
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message)
    done()
});
sendNotification('11123423', 'This is my new contacts')