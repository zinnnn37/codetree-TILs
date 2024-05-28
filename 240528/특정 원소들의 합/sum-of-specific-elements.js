const fs = require('fs');

let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let arr2d = []

// 2차원 배열 만들기
for (let i = 0; i < input.length; i++) {
    arr2d.push(input[i].split(' ').map(Number));
}

// 계산
let res = 0;
for (let i = 0; i < arr2d.length; i++) {
    for (let j = 0; j <= i; j++) {
        res += arr2d[i][j];
    }
}

console.log(res);