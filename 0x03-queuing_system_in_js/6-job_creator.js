
import { createQueue } from 'kue';

var push_notification_code = createQueue()
var data = {
    
}
var job = push_notification_code.create('push_notification',data);

job.on('complete', (result) => {
    console.log(`Notification job completed: ${job.id} and it data: ${result}`)
}).on('failed', () => {
    console.log('Notification job failed')

}).on('enqueue', () => {

    console.log(`Notification job created: ${job.id}`)
}
);
job.save((err) => {
    if (err) {
        console.log(`Errors occured:  ${err}`)
    }
})


