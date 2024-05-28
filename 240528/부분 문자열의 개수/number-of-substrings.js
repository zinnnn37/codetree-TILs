const fs = require('fs');
const [haystack, needle] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let cnt = 0;
for (let i = 0; i < haystack.length - 1; i++) {
    if (haystack.slice(i, i+2) === needle) {
        cnt++;
    }
}

console.log(cnt);