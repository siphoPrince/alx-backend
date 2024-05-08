const kue = require('kue');

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach(job => {
    const createdJob = queue.createJob('push_notification_code_3', job)
      .save((err) => {
        if (err) {
          console.error('Error creating job:', err);
        } else {
          console.log(`Notification job created: ${createdJob.id}`);
        }
      });

    createdJob.on('complete', () => {
      console.log(`Notification job ${createdJob.id} completed`);
    });

    createdJob.on('failed', (err) => {
      console.error(`Notification job ${createdJob.id} failed: ${err}`);
    });

    createdJob.on('progress', (progress) => {
      console.log(`Notification job ${createdJob.id} ${progress}% complete`);
    });
  });
}

module.exports = createPushNotificationsJobs;
