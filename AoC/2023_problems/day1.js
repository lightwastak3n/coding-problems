const fs = require("fs");

const data = fs.readFileSync("AoC/2023_problems/day1.txt", "utf8");

// Gets the two digit number from a line by finding first and last digit
function getNumber(line) {
    let nums = [];
    for (const char of line) {
        if (!isNaN(char)) {
            nums.push(char);
        }
    }
    if (nums.length > 1) {
        return parseInt(nums[0] + nums[nums.length - 1]);
    }
    return parseInt(nums[0] + nums[0]);
}

// Replaces name of a number with a string containg that number.
// We avoid chaning first and last letter since it can be a part of another number
// oneight
function replaceWords(line) {
    const numMap = {
        "one": "o1e",
        "two": "t2o",
        "three": "thr3e",
        "four": "fo4r",
        "five": "fi5e",
        "six": "s6x",
        "seven": "se7en",
        "eight": "ei8ht",
        "nine": "ni9e"
    };
    for (const [key, value] of Object.entries(numMap)) {
        line = line.replaceAll(key, value);
    }
    return line;
}

function solution(data) {
    const lines = data.split("\n");
    let part1 = 0;
    let part2 = 0
    for (const line of lines) {
        part1 += getNumber(line);
        part2 += getNumber(replaceWords(line));
    }
    return [part1, part2];
}

console.log(solution(data));
