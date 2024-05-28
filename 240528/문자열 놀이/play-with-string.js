const fs = require('fs');
const [input, ...inputQuery] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

let [s, q] = input.split(' ');
q = Number(q);
const len = s.length;
let query = [];
for (let i = 0; i < q; i++) {
    query.push(inputQuery[i].split(' '));
}

function swipe(a, b) {
    let strToArr = [...s];

    const tmp = strToArr[a];
    strToArr[a] = strToArr[b];
    strToArr[b] = tmp;

    s = strToArr.join('');
}

function exchange(cur, toChange) {
    for (let i = 0; i < len; i++) { 
        if (s[i] === cur) {
            let strToArr = [...s];
            strToArr[i] = toChange;
            s = strToArr.join('');
        }
    }
}

for (let q of query) {
    if (q[0] == 1) {
        const [a, b] = q.slice(1).map(x => Number(x) - 1);
        
        swipe(a, b);
    } else {
        const [cur, toChange] = q.slice(1);

        exchange(cur, toChange);
    }
    console.log(s);
}