import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';


const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);


const queue = kue.createQueue();

let reservationEnabled = true;

// Functions to manage the number of available seats
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats, 10);
}

// Initialization number of available seats
reserveSeat(50);

// Configuration Serveur Express
const app = express();
const port = 1245;

// Road to get the number of available seats
app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seats });
});

// Road to reserve a seat
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservations are blocked' });
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });
});

// Road to process the queue
app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    let seats = await getCurrentAvailableSeats();
    if (seats <= 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      await reserveSeat(seats - 1);
      if (seats - 1 === 0) {
        reservationEnabled = false;
      }
      done();
    }
  });
  res.json({ status: 'Queue processing' });
});

// Manage the end of a job
queue.on('job complete', (id) => {
  console.log(`Seat reservation job ${id} completed`);
}).on('job failed', (id, errorMessage) => {
  console.log(`Seat reservation job ${id} failed: ${errorMessage}`);
});

// Start server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
