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

  function publishMessage(message, time) {
    return new Promise((resolve) => {
      setTimeout(() => {
        console.log(`About to send ${message}`);
        client.publish('holberton school channel', message, () => {
          resolve();
        });
      }, time);
    });
  }

  await publishMessage('Holberton Student #1 starts course', 100);
  await publishMessage('Holberton Student #2 starts course', 200);
  await publishMessage('KILL_SERVER', 300);
  await publishMessage('Holberton Student #3 starts course', 400);

  await client.quit();
})();

