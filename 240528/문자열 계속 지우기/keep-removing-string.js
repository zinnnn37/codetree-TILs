const fs = require('fs');
let [haystack, needle] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const needleLength = needle.length;

let indexOfNeedle = haystack.indexOf(needle);
while (indexOfNeedle != -1) {
    haystack = haystack.slice(0, indexOfNeedle) + haystack.slice(indexOfNeedle + needleLength);
    indexOfNeedle = haystack.indexOf(needle);
}

console.log(haystack);