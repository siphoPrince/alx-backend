import { createClient } from 'redis';
const { promisify } = require('util');

const client = createClient();

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

(async () => {
  await client.connect();

  const getAsync = promisify(client.get).bind(client);

  async function displaySchoolValue(schoolName) {
    try {
      const reply = await getAsync(schoolName);
      console.log(reply);
    } catch (err) {
      console.error('Error getting school value:', err.message);
    }
  }

  function setNewSchool(schoolName, value, callback) {
    client.set(schoolName, value, callback);
  }

  setNewSchool('HolbertonSanFrancisco', '100', (reply) => {
    console.log(`Reply: ${reply}`);
  });

  await displaySchoolValue('Holberton');
  await displaySchoolValue('HolbertonSanFrancisco');

  await client.quit();
})();
