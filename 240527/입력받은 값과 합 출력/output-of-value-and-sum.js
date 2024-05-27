const fs = require('fs');

const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

console.log(input[0], input[1], Number(input[0]) + Number(input[1]));