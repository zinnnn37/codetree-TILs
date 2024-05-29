const fs = require('fs');
const [input, ...queries] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let [s, q] = input.split(' ');

for (let query of queries) {
    if (query === '1') {
        s = s.slice(1) + s.slice(0, 1);
    } else if (query === '2') {
        s = s.slice(-1) + s.slice(0, -1);
    } else {
        let strToArr = [...s];
        strToArr.reverse();
        s = strToArr.join('');
    }
    
    console.log(s);
}