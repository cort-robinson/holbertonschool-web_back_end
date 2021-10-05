import kue from 'kue';

const queue = kue.createQueue();
const jobObj = {
  phoneNumber: '918-234-5678',
  message: 'I am a message',
}

const job = queue.create('push_notification_code', jobObj).save();

job.on('enqueue', () => console.log(`Notification job created: ${job.id}`))
  .on('complete', () => console.log(`Notification job completed`))
  .on('failed', () => console.log(`Notification job failed`))
