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

    // slice 이용해도 됨(exchange도 마찬가지)
    /*
    const tmp = s[a];

    s = s.slice(0, a) + s[b] + s.slice(a+1);
    s = s.slice(0, b) + tmp + s.slice(b+1);
    */
}

function exchange(cur, toChange) {
    // 여기서 includes로 확인해서 시간복잡도 n^3 된 듯
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