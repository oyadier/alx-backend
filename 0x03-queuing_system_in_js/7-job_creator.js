import { createQueue } from "kue";
const queue = createQueue()

const jobs = [
    {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
    },
    {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
    },
    {
        phoneNumber: '4153518743',
        message: 'This is the code 4321 to verify your account'
    },
    {
        phoneNumber: '4153538781',
        message: 'This is the code 4562 to verify your account'
    },
    {
        phoneNumber: '4153118782',
        message: 'This is the code 4321 to verify your account'
    },
    {
        phoneNumber: '4153718781',
        message: 'This is the code 4562 to verify your account'
    },
    {
        phoneNumber: '4159518782',
        message: 'This is the code 4321 to verify your account'
    },
    {
        phoneNumber: '4158718781',
        message: 'This is the code 4562 to verify your account'
    },
    {
        phoneNumber: '4153818782',
        message: 'This is the code 4321 to verify your account'
    },
    {
        phoneNumber: '4154318781',
        message: 'This is the code 4562 to verify your account'
    },
    {
        phoneNumber: '4151218782',
        message: 'This is the code 4321 to verify your account'
    }
];

for (let i = 0; i < jobs.length; i++) {
    const push_notification = queue.create('push_notification_code_2', jobs[i])
    push_notification.on('enqueue', () =>{
        console.log(`Notification hob created: ${push_notification}`)
    }).on('complete', () => {
        console.log(`Notification job ${push_notification.id} completed`)
    }).on('failed', (err) => {
        console.log(`Notification job JOB_ID failed: ${err}`)
    }).on('progress', (done) =>{
        console.log(`otification job ${push_notification.id} ${done}% complete`)
    })
}
