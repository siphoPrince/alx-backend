import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

(async () => {
  await client.connect();

  function createHash() {
    const schoolLocations = {
      Portland: 50,
      Seattle: 80,
      'New York': 20,
      Bogota: 20,
      Cali: 40,
      Paris: 2,
    };

    for (const [location, count] of Object.entries(schoolLocations)) {
      client.hset('HolbertonSchools', location, count, (err, reply) => {
        if (err) {
          console.error('Error setting school location:', err.message);
          return;
        }
        console.log(`Reply: ${reply}`); // redis.print for each hset
      });
    }
  }

  function displayHash() {
    client.hgetall('HolbertonSchools', (err, reply) => {
      if (err) {
        console.error('Error getting school locations:', err.message);
        return;
      }
      console.log(reply);
    });
  }

  createHash();
  displayHash();

  await client.quit();
})();
