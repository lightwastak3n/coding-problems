const fs = require("fs");

const data = fs.readFileSync("AoC/2023_problems/day3.txt", "utf8");
const dataRows = data.split("\n");
// Pad the table around with dots for easier parsing later on
const pad = Array(dataRows[0].length + 2).fill(".");
let rows = [pad];
for (const row of dataRows) {
    rows.push([".", ...row, "."]);
}
rows.push(pad);

const ignoreList = ".0123456789";
const isDigit = (x) => ignoreList.slice(1).includes(x);
const isSymbol = (x) => !ignoreList.includes(x);

// Checks neighboring cells for symbols and gears and returns true if a symbol is found, false otherwise.
// Adds new gears to the set in the form of a string "i,j" coordinates
function checkNeighbors(row, col, gearsCoord) {
    let symbolFound = false;
    let neighbors = [
        [-1, -1], [0, -1], [1, -1],
        [-1, 0], [1, 0],
        [-1, 1], [0, 1], [1, 1] , 
    ];
    for (let [x, y] of neighbors) {
        if (isSymbol(rows[row + x][col + y])) {
            symbolFound = true;
        }
        if (rows[row + x][col + y] === "*") {
            gearsCoord.add(`${row + x},${col + y}`);
        }
    }
    return symbolFound;
}

function solve(rows) {
    let nums = [];
    let gears = {};
    for (let i = 1; i < rows.length - 1; i++) {
        let j = 1;
        while (j < rows[0].length) {
            if (isDigit(rows[i][j])) {
                let symbolChecks = [];
                let gearCoord = new Set();
                let num = "";
                // Collect all numbers that are next to each other
                while (isDigit(rows[i][j])) {
                    num += rows[i][j];
                    // Adding new gears to the set and checking for symbols next to the current i,j cell
                    symbolChecks.push(checkNeighbors(i, j, gearCoord));
                    j++;
                }
                // Check if any symbols were found and add num to the nums
                if (symbolChecks.some(Boolean)) {
                    nums.push(parseInt(num));
                }
                // Add collected gears to the set. If gear already exists, push to the array.
                for (let gc of gearCoord) {
                    if (gears.hasOwnProperty(gc)) {
                        gears[gc].push(parseInt(num));
                    }
                    else {
                        gears[gc] = [parseInt(num)];
                    }
                }
            }
            j++;
        }
    }
    let p1 = nums.reduce((acc,x) => acc + x, 0);
    let p2 = 0;
    for (let [k, v] of Object.entries(gears)) {
        if (v.length > 1) {
            p2 += v[0] * v[1];
        }
    }
    return [p1, p2];
}

console.log(solve(rows));
