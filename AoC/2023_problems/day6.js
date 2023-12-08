const fs = require("fs");

const data = fs.readFileSync("day6.txt", "utf8")

function solve(data) {
    const [times, distances] = data.split("\n");
    const tArr = times.split(":")[1].split(" ").filter(Boolean);
    const dArr = distances.split(":")[1].split(" ").filter(Boolean);

    let p1 = 1;
    for (let i = 0; i < tArr.length; i++) {
        let possibleDistances = [];
        for (let j = 1; j < tArr[i]; j++) {
            possibleDistances.push(j * (tArr[i] - j));
        }
        p1 *= possibleDistances.filter(x => x > dArr[i]).length;
    }
    const totalTime = parseInt(tArr.join(""));
    const totalDistance = parseInt(dArr.join(""));
    const x1 = (totalTime + (totalTime ** 2 - 4 * totalDistance) ** 0.5) / 2;
    const x2 = (totalTime - (totalTime ** 2 - 4 * totalDistance) ** 0.5) / 2;
    return [p1, Math.floor(x1) - Math.floor(x2)];
}

console.log(solve(data))
