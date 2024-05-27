const fs = require("fs");

const a = fs.readFileSync(0).toString();
const res = Number(a) * 2 + 3;

console.log(res);