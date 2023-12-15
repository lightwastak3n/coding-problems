const fs = require("fs");

const data = fs.readFileSync("AoC/2023_problems/day15.txt", "utf8");

const hash = (text) => text.split("").reduce((acc, char) => ((acc + char.charCodeAt()) * 17) % 256, 0);

const part1 = (data) => data.split(",").reduce((acc, line) => (acc + hash(line)), 0);

function part2(data) {
    const lines = data.split(",");
    const boxes = Array.from({length: 256}, (x) => ({}));
    for (const line of lines) {
        if (line.includes("=")) {
            const [key, value] = line.split("=");
            boxes[hash(key)][key] = value;
        }
        else {
            const key = line.split("-")[0];
            delete boxes[hash(key)][key];
        }
    }
    const boxValue = (box, boxMulti) => Object.values(box).reduce((acc, val, index) => (acc + boxMulti * val * (index+1)), 0);
    return boxes.reduce((acc, box) => (acc + boxValue(box, boxes.indexOf(box)+1)), 0);
}

console.log(part1(data));
console.log(part2(data))
