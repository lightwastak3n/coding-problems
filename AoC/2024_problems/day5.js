const testInput = `47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47`


const fs = require("fs");
const data = fs.readFileSync("AoC/2024_problems/day5.txt", encoding="utf8");


function solve(data) {
    let [instructions, updates] = data.split("\n\n");
    instructions = instructions.split("\n");
    updates = updates.split("\n").map(x => x.split(","));
    let partOneUpdates = [];
    for (let i = 0; i < updates.length; i++) {
        let add = true;
        for (let j = 0; j < updates[i].length; j++) {
            for (let k = j+1; k < updates[i].length; k++) {
                let pair = updates[i][j] + "|" + updates[i][k];
                if (!instructions.includes(pair)) {
                    add = false;
                    let temp = updates[i][j];
                    updates[i][j] = updates[i][k];
                    updates[i][k] = temp;
                }
            }
        }
        if (add) {
            partOneUpdates.push(i);
        }
    }
    let partOneTotal = 0;
    let bothTotal = 0;
    for (const [index, update] of updates.entries()) {
        let middle = parseInt(update[Math.floor(update.length / 2)]);
        if (partOneUpdates.includes(index)) {
            partOneTotal += middle;
        }
        bothTotal += middle;
    }
    console.log(partOneTotal);
    console.log(bothTotal - partOneTotal);
}

solve(data);