const testInput = `....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...`


const fs = require("fs");
const data = fs.readFileSync("AoC/2024_problems/day6.txt", encoding="utf8");

const guards = ["^", ">", "v", "<"];
const move = {
    "^": [-1, 0],
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1]
}

function walk(table, startPos, currentGuard) {
    const rows = table.length;
    const cols = table[0].length;
    let guardPos = startPos;
    let visited = {};
    let escaped = true;
    while (true) {
        let coord = JSON.stringify(guardPos);
        if (!visited[coord]) {
            visited[coord] = [currentGuard];
        } else if (visited[coord].includes(currentGuard)) {
            // Found a loop
            escaped = false;
            break
        } else {
            visited[coord].push(currentGuard);
        }
        let currentDir = move[currentGuard];
        let nextPos = [guardPos[0] + currentDir[0], guardPos[1] + currentDir[1]];
        if (nextPos[0] < 0 || nextPos[0] >= rows || nextPos[1] < 0 || nextPos[1] >= cols) {
            // we escaped outside the table
            break;
        }
        if (table[nextPos[0]][nextPos[1]] === "#") {
            currentGuard = guards[(guards.indexOf(currentGuard) + 1) % 4];
        } else {
            guardPos = nextPos;
        }
    }
    return [visited, escaped];
}


function solve(data) {
    const table = data.split("\n").map(x => x.split(""));
    const rows = table.length;
    const cols = table[0].length;
    // Find guard
    let startPos = [];
    for (let row = 0; row < rows; row++) {
        for (let col = 0; col < cols; col++) {
            if (guards.includes(table[row][col])) {
                startPos = [row, col];
                break;
            }
        }
        if (startPos.length > 0) {
            break;
        }
    }
    let currentGuard = table[startPos[0]][startPos[1]];
    let guardPos = startPos;
    let [visited, escaped] = walk(table, guardPos, currentGuard);
    let partTwo = 0;
    let visitedCoords = Object.keys(visited);
    for (let i = 0; i < visitedCoords.length; i++) {
        let newObstacle = JSON.parse(visitedCoords[i]);
        table[newObstacle[0]][newObstacle[1]] = "#";
        let [visited, escaped] = walk(table, guardPos, currentGuard);
        if (!escaped) {
            partTwo++;
        }
        table[newObstacle[0]][newObstacle[1]] = ".";
    }

    let partOne = visitedCoords.length;
    console.log(partOne);
    console.log(partTwo);
}


solve(data);