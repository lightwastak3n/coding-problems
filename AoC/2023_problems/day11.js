const fs = require("fs")

data = fs.readFileSync("AoC/2023_problems/day11.txt", "utf8")

const test_data = `...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....`


function solve(data) {
    const grid = [];
    for (const line of data.split("\n")) {
        grid.push(Array.from(line));
    }
    // Find empty rows, columns and galaxies coordinates.
    const allRows = new Set([...Array(grid.length).keys()]);
    const allCols = new Set([...Array(grid[0].length).keys()]);
    let foundRows = new Set();
    let foundCols = new Set();
    let galaxies = [];
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] == "#") {
                foundRows.add(i);
                foundCols.add(j);
                galaxies.push([i, j]);
            }
        }
    }
    const emptyCols = new Set([...allCols].filter(x => !foundCols.has(x)));
    const emptyRows = new Set([...allRows].filter(x => !foundRows.has(x)));

    // Solve part 1 and 2
    let p1 = 0;
    let p2 = 0;
    for (let i = 0; i < galaxies.length; i++) {
        for (let j = i; j < galaxies.length; j++) {
            const [x1, y1] = galaxies[i];
            const [x2, y2] = galaxies[j];
            const g1RowsOffset = [...emptyRows].filter(x => x < x1).length;
            const g1ColumnsOffset = [...emptyCols].filter(x => x < y1).length;
            const g2RowsOffset = [...emptyRows].filter(x => x < x2).length;
            const g2ColumnsOffset = [...emptyCols].filter(x => x < y2).length;

            // Manhattan distance = |x1 - x2| + |y1 - y2|
            p1 += Math.abs(x1 + g1RowsOffset - x2 - g2RowsOffset) + Math
            .abs(y1 + g1ColumnsOffset - y2 - g2ColumnsOffset);
            p2 += Math.abs(x1 - x2 + 999999* (g1RowsOffset - g2RowsOffset)) + Math
            .abs(y1 - y2 + 999999 * (g1ColumnsOffset - g2ColumnsOffset));
        }
    }
    return [p1, p2];
}

console.log(solve(data))
