const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim();
const res = Number(input).toFixed(2);

console.log(res);