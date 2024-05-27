const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('-');

console.log([input[0], input[2], input[1]].join('-'));