const fs = require("fs");

const data = fs.readFileSync("day8.txt", "utf8")

function parseData(data) {
    // Extract moves as string and nodes as {node: [left, right]}
    const [moves, nodes] = data.split("\n\n");
    const nodesGraph = {};
    for (const line of nodes.split("\n")) {
        const [node, children] = line.split(" = ");
        const leftChild = children.slice(1).split(", ")[0];
        const rightChild = children.split(", ")[1].slice(0, -1);
        nodesGraph[node] = [leftChild, rightChild];
    }
    return [moves, nodesGraph];
}

function gcd(a, b) {
    if (b === 0) {
        return a;
    }
    return gcd(b, a % b);
}

function lcm(nums) {
    let lcmVal = 1;
    for (let num of nums) {
        lcmVal = lcmVal * num / gcd(lcmVal, num);
    }
    return lcmVal;
}

function solve(data) {
    const [moves, nodesGraph] = parseData(data);
    // Extract all nodes ending with A
    const aNodes = Object.keys(nodesGraph).filter(node => node.endsWith("A"));
    let nodesSteps = {};
    
    // Take aNodes one by one and cycle until every one gets to Z node
    for (let node of aNodes) {
        nodesSteps[node] = 0;
        let currentNode = node;

        let i = 0;
        while (!currentNode.endsWith("Z")) {
            if (i == moves.length) i = 0;
            let move = moves[i] == "L" ? 0 : 1;
            currentNode = nodesGraph[currentNode][move];
            nodesSteps[node]++;
            i++;
        }
    }
    return [nodesSteps["AAA"], lcm(Object.values(nodesSteps))];
}

console.log(solve(data));
