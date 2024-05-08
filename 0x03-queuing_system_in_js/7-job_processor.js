const kue = require('kue');

const queueName = 'push_notification_code_2';
const concurrency = 2;

const blacklistedNumbers = ['4153518780', '4153518781'];

const queue = kue.createQueue();

queue.process(queueName, concurrency, (job, done) => {
  const { phoneNumber, message } = job.data;
  let progress = 0;

  if (blacklistedNumbers.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  job.on('progress', (p) => {
    progress = p;
    console.log(`Notification job #${job.id} ${progress}% complete`);
  });

  job.progress(50);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  job.progress(100);
  done();
});
