const kue = require('kue');
const { expect } = require('chai'); // Assuming Chai for assertions

const createPushNotificationsJobs = require('./8-job');

describe('createPushNotificationsJobs function', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue({ redis: { testMode: true } }); // Enter test mode
  });

  afterEach(() => {
    return new Promise((resolve) => {
      queue.inactive((err, jobs) => {
        if (err) throw err;

        jobs.forEach((job) => job.remove((err) => {
          if (err) throw err;
        }));

        queue.shutdown(() => resolve(), true); // Clear queue and exit test mode
      });
    });
  });

  it('should display an error message if jobs is not an array', () => {
    const invalidJobs = 'not an array';
    expect(() => createPushNotificationsJobs(invalidJobs, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('should create two new jobs to the queue', async () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Test message 1' },
      { phoneNumber: '9876543210', message: 'Test message 2' },
    ];

    await createPushNotificationsJobs(jobs, queue);

    const activeJobs = await new Promise((resolve) => {
      queue.active((err, jobs) => {
        if (err) throw err;
        resolve(jobs);
      });
    });

    expect(activeJobs).to.have.lengthOf(2);
  });
});
