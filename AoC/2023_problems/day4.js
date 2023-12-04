const fs = require("fs");

const data = fs.readFileSync("AoC/2023_problems/day4.txt", encoding="utf8");

function solution(data) {
	const lines = data.split("\n");
	let p1 = 0;
	let p2 = Array.from({length: lines.length}, () => 1);
	for (let i = 0; i < lines.length; i++) {
		const nums = lines[i].split(":")[1];
		const wins = new Set(nums.split("|")[0].split(" ").filter(x => x));
		const draw = new Set(lines[i].split("|")[1].split(" ").filter(x => x));
		const found = new Set([...wins].filter(x => draw.has(x)));
		p1 += Math.floor(2 ** (found.size - 1));
		for (let j = i+1; j < i + found.size + 1; j++) {
			p2[j] += p2[i];
		} 
	}
	return [p1, p2.reduce((x, val) => x + val, 0)];
}

console.log(solution(data));

