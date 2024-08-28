var kue = require('kue');
var push_notification_code = kue.createQueue();

var jobData = {
    phoneNumber: String,
    message: String,
}

push_notification_code.create('push_notification', jobData)
    .save((err) => {
        if (!err) console.log(`Notification job created: ${push_notification_code.id}`);
    });

push_notification_code.on('complete', () => console.log('Notification job completed'))
    .on('fail', () => console.log('Notification job fail'))
