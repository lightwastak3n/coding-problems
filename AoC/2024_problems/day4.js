const testInput = `MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX`;


const fs = require("fs");
const data = fs.readFileSync("AoC/2024_problems/day4.txt", encoding="utf8");


// Create table, pad from all sides to avoid caring about edges
function cleanInputData(data) {
    let cleanData = [];
    for (const line of data.split("\n")) {
        cleanData.push(`.${line}.`.split(""));
    }
    cleanData.unshift(Array(cleanData[0].length).fill("."));
    cleanData.push(Array(cleanData[0].length).fill("."));
    return cleanData;
}
let cleanData = cleanInputData(data);
let cleanTestData = cleanInputData(testInput);


const chars = {
    1: "X",
    2: "M",
    3: "A",
    4: "S",
}

const directions = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1],
    "UL": [-1, -1],
    "UR": [-1, 1],
    "DL": [1, -1],
    "DR": [1, 1],
}

const partTwoPattern = [
    ["M", ".", "M"],
    [".", "A", "."],
    ["S", ".", "S"],
]

function rotateRight(table) {
    let rotated = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
    ];
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            rotated[i][j] = table[3-j-1][i];
        }
    }
    return rotated;
}

function sameTable(table) {
    for (let row = 0; row < 3; row++) {
        for (let col = 0; col < 3; col++) {
            if (table[row][col] != partTwoPattern[row][col]) {
                return false;
            }
        }
    }
    return true;
}


function equivalentTable(table) {
    for (let i = 0; i < 4; i++) {
        if (sameTable(table)) {
            return true
        }
        table = rotateRight(table);
    }
    return false;
}


function buildXmas(pos, row, col, table, found, direction=null) {
    let currentChar = table[row][col];
    if (pos === 4 && currentChar === "S") {
        found.push(true);
    }
    if (pos === 1 && currentChar === "X") {
        for (const dir in directions) {
            let [newRow, newCol] = [row + directions[dir][0], col + directions[dir][1]];
            let targetChar = chars[pos+1];
            if (table[newRow][newCol] === targetChar) {
                buildXmas(pos + 1, newRow, newCol, table, found, dir);
            }
        }
    } else if (pos > 1 && currentChar === chars[pos]) {
        // Continue in the same direction
        let [newRow, newCol] = [row + directions[direction][0], col + directions[direction][1]];
        buildXmas(pos+1, newRow, newCol, table, found, direction);
    }
    found.push(false);
}

function solvePartOne(data) {
    let found = [];
    for (let row = 1; row < data.length - 1; row++) {
        for (let col = 1; col < data[0].length - 1; col++) {
            buildXmas(1, row, col, data, found)
        }
    }
    console.log(found.filter(x => x === true).length);
}

function solvePartTwo(data) {
    let count = 0;
    for (let row = 1; row < data.length - 3; row++) {
        for (let col = 1; col < data[0].length - 3; col++) {
            let box = [
                [data[row][col], ".", data[row][col+2]],
                [".", data[row+1][col+1], "."],
                [data[row+2][col], ".", data[row+2][col+2]]
            ]
            if (equivalentTable(box)) {
                count++;
            }

        }
    }
    console.log(count);
}

solvePartOne(cleanData);
solvePartTwo(cleanData);
