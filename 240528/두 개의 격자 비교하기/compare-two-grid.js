const fs = require('fs')
const [input, ...arr] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = input.split(' ').map(Number);

let arr1 = []
let arr2 = []
for (let i = 0; i < n; i++) {
    arr1.push(arr[i].split(' '));
    arr2.push(arr[i+n].split(' '));
}

let res = Array(n).fill(0).map(() => Array(m).fill(0));
for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
        if (arr1[i][j] != arr2[i][j]) {
            res[i][j] = 1;
        }
    }
}

for (let row of res) {
    let str = ''
    for (let e of row) {
        str += e + ' ';
    }
    console.log(str);
}