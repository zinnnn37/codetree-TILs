const fs = require('fs');
const [year, month, day] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

function isLeafYear(year) {
    if (year % 4 === 0) {
        if (year % 100 === 0) {
            if (year % 400 === 0) {
                return true;
            }
            return false ;
        }
        return true;
    }
    return false;
}

function checkValid(year, month, day) {
    let res = -1;
    const div = month / 3;

    switch (month) {
        case 1, 3, 5, 7, 8, 10, 12:
            console.log('31');
            if (div === 0 || month === 12) res = 'Winter';
            else if (div === 1) res = 'Spring';
            else if (div === 2) res = 'Summer';
            else if (div === 3) res = 'Fall';
            break;
        case 4, 6, 9, 11:
            if (day <= 30) {
                if (div === 1) res = 'Spring';
                else if (div === 2) res = 'Summer';
                else res = 'Fall';
            }
            break;
        case 2:
            if ((isLeafYear(year) && day === 29) || day <= 28) {
                res = 'Winter'
            };
            break;
        default:
            res = -1;
    }
    return res;
}

console.log(checkValid(year, month, day));