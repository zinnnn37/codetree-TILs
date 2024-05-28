const fs = require('fs');
const [haystack, needle] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

console.log(haystack.indexOf(needle));