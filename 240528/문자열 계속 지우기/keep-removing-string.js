const fs = require('fs');
let [haystack, needle] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const needleLength = needle.length;

for (let i = 0; i < haystack.length; i++) {
    if (haystack.slice(i, i+needleLength) === needle) {
        haystack = haystack.slice(0, i) + haystack.slice(i+needleLength);
        i -= 2;
    }
}

console.log(haystack);