const testInput = `3   4
4   3
2   5
1   3
3   9
3   3`;

const fs = require("fs");
const data = fs.readFileSync("AoC/2024_problems/day1.txt", encoding="utf8");

function solve(data) {
    const lines = data.split("\n");
    let listA = [];
    let listB = [];
    for (let line of lines) {
        let [a, b] = line.split(/\s+/);
        listA.push(parseInt(a));
        listB.push(parseInt(b));
    }
    listA.sort((a, b) => a - b);
    listB.sort((a, b) => a - b);
    let part1 = listA.reduce((acc, val, i) => acc + Math.abs(val - listB[i]), 0);
    console.log(part1);
    let part2 = listA.reduce((acc, val) => acc + val * listB.filter(x => x == val).length, 0); 
    console.log(part2);
}

solve(data);
