import chai from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

const expect = chai.expect;
const queue = kue.createQueue();

describe('createPushNotificationsJobs', function() {
  before(function() {
    queue.testMode.enter();
  });

  afterEach(function() {
    queue.testMode.clear();
  });

  after(function() {
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', function() {
    expect(() => createPushNotificationsJobs({}, queue)).to.throw('Jobs is not an array');
  });

  it('should create jobs for each item in the array', function() {
    const jobs = [
      {
        phoneNumber: '1234567890',
        message: 'Message 1'
      },
      {
        phoneNumber: '0987654321',
        message: 'Message 2'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.include({ phoneNumber: '0987654321', message: 'Message 2' });
  });
});
