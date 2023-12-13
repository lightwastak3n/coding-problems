const { count } = require("console");
const fs = require("fs")

const data = fs.readFileSync("AoC/2023_problems/day13.txt", "utf8")


let test_data = `#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#`


function transpose(grid) {
    return grid[0].map((col, i) => grid.map(row => row[i]));
}

function countDifferences(a, b) {
    let diff = 0
    if (a.length != b.length) {
        return false;
    }
    for (let i = 0; i < a.length; i++) {
        for (let j = 0; j < a[i].length; j++) {
            if (a[i][j] != b[i][j]) {
                diff++;
            }       
        }
    }
    return diff;
}

function findReflection(grid) {
    let p1 = 0;
    let p2 = 0;
    for (let i = 1; i < grid.length; i++) {
        let top = grid.slice(0, i).reverse();
        let bottom = grid.slice(i);
        top = top.slice(0, bottom.length);
        bottom = bottom.slice(0, top.length); 
        if (countDifferences(top, bottom) == 0) {
            p1 += i;
        }
        if (countDifferences(bottom, top) == 1) {
            p2 += i;
        }
    }
    return [p1, p2];
}

function solve(data) {
    const grids = data.split("\n\n");
    let part1 = 0;
    let part2 = 0;
    for (let g of grids) {
        let grid = []
        for (let line of g.split("\n")) {
            grid.push(line.split(""));
        }
        let p = findReflection(grid);
        let t = findReflection(transpose(grid));
        part1 += 100 * p[0] + t[0];
        part2 += 100 * p[1] + t[1];
    }
    return [part1, part2]
}

console.log(solve(data))
