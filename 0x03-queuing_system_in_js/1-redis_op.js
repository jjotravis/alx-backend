import redis from 'redis'

const client = redis.createClient();

client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));

client.on('connect', () => {
    console.log('Redis client connected to the server');
}).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    client.get(schoolName, redis.print);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFransisco', '100');
displaySchoolValue('HolbertonSanFransisco');