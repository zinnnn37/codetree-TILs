const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());

let cnt = 1;
let res = Array(n).fill(0).map(() => Array(n).fill(0));
for (let j = n-1; j >= 0; j--) {
    for (let i = n-1; i >= 0; i--) {
        // odd column
        if (j % 2 == 1) {
            res[i][j] = cnt;
        } else {
            res[n-i-1][j] = cnt;
        }
        cnt++;
    }
}

for (let row of res) {
    let str = '';
    for (let e of row) {
        str += e + ' ';
    }
    console.log(str);
}