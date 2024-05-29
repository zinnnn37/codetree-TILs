const fs = require('fs');
const [year, month, day] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

function isLeapYear(year) {
    if (year % 4 === 0) {
        if (year % 100 === 0) {
            if (year % 400 === 0) {
                return true;
            }
            return false;
        }
        return true;
    }
    return false;
}

function checkValid(year, month, day) {
    let res = -1;
    const daysOfMonth = [31, isLeapYear(year) ? 29 : 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    if (day > daysOfMonth[month - 1]) return res;
    
    if (month === 1 || month === 2 || month === 12) {
        res = 'Winter';
    } else if (month >= 3 && month <= 5) {
        res = 'Spring';
    } else if (month >= 6 && month <= 8) {
        res = 'Summer';
    } else if (month >= 9 && month <= 11) {
        res = 'Fall';
    }
    
    return res;
}

console.log(checkValid(year, month, day));