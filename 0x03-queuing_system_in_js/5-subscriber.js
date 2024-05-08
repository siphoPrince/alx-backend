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

  const channel = 'holberton school channel';
  await client.subscribe(channel, (err, count) => {
    if (err) {
      console.error('Error subscribing to channel:', err.message);
      return;
    }
    console.log(`Subscribed to ${count} channels`);
  });

  client.on('message', (channel, message) => {
    console.log(message.toString());
    if (message === 'KILL_SERVER') {
      client.unsubscribe(channel);
      client.quit();
    }
  });
})();
