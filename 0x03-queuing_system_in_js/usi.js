const kue = require('kue');
const queue = kue.createQueue();

kue.app.listen(3000);
console.log('Kue UI listening on port 3000');
