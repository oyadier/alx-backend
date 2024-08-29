var kue = require('kue');
var queue = kue.createQueue();

var jobData = {
    phoneNumber: '04343334433',
    message: 'This is the code to verify your account',
}

const job = queue.create('push_notification_code', jobData);
    job.save((err) => {
        if (!err){ console.log(`Notification job created: ${queue.id.slice(14, -1)}`);
    }
    });

job.on('complete', () => console.log('Notification job completed'))
    .on('fail', () => console.log('Notification job fail'))
