const testInput = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))";
const testInput2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


const fs = require("fs");
const data = fs.readFileSync("AoC/2024_problems/day3.txt", encoding="utf8");

function solve(data) {
    const text = data.split("\n").join("");
    const mulPattern = /mul\((-?\d+),(-?\d+)\)/g;
    const doPattern = /do\(\)/g;
    const dontPattern = /don't\(\)/g;
    let part1 = 0;
    let part2 = 0;
    let found = [];
    let mulMatch;
    let doMatch;
    let dontMatch;
    while ((mulMatch = mulPattern.exec(text)) !== null) {
        found.push([mulMatch.index, parseInt(mulMatch[1]), parseInt(mulMatch[2])]);
    }
    while ((doMatch = doPattern.exec(text)) !== null) {
        found.push([doMatch.index, "do"]);
    }
    while ((dontMatch = dontPattern.exec(text)) !== null) {
        found.push([dontMatch.index, "don't"]);
    }
    found.sort((a, b) => a[0] - b[0]);
    console.log(found);
    let status = 1;
    for (let i = 0; i < found.length; i++) {
        if (found[i][1] == "do") {
            status = 1;
        }
        else if (found[i][1] == "don't") {
            status = 0;
        }
        else {
            let val = found[i][1] * found[i][2];
            part1 += val;
            if (status == 1) {
                part2 += val;
            }
        }
    }
    console.log(part1);
    console.log(part2);
}

solve(data);

