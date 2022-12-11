# Advent of Code 2022
List of problems: https://adventofcode.com/2022/

You can get the problem input data directly into your Python code with [get_data.py](problems/get_data.py). Create a `config.json` file in problems folder and add cookie session to it or just configure it for yourself.
```json
{
	"cookie": "92d5eea06bd8a2c14a......."
}
```
This will also save the input data as a txt file for future reference. Python files are run from the problems folder.

I try to write the first solution as fast as I can, so whatever first comes to mind. After I get the stars I might try to write shorter code for the second solution. 

| Day | Problem link                                                         | Solution                    | Cleaner                     |
| --- | -------------------------------------------------------------------- | --------------------------- | --------------------------- |
| 1   | [Day 1 - Advent of Code 2022](https://adventofcode.com/2022/day/1)   | [Python](problems/day1.py)  |                             |
| 2   | [Day 2 - Advent of Code 2022](https://adventofcode.com/2022/day/2)   | [Python](problems/day2.py)  |                             |
| 3   | [Day 3 - Advent of Code 2022](https://adventofcode.com/2022/day/3)   | [Python](problems/day3.py)  |                             |
| 4   | [Day 4 - Advent of Code 2022](https://adventofcode.com/2022/day/4)   | [Python](problems/day4.py)  |                             |
| 5   | [Day 5 - Advent of Code 2022](https://adventofcode.com/2022/day/5)   | [Python](problems/day5.py)  | [Python](problems/day5b.py) |
| 6   | [Day 6 - Advent of Code 2022](https://adventofcode.com/2022/day/6)   | [Python](problems/day6.py)  |                             |
| 7   | [Day 7 - Advent of Code 2022](https://adventofcode.com/2022/day/7)   | [Python](problems/day7.py)  |                             |
| 8   | [Day 8 - Advent of Code 2022](https://adventofcode.com/2022/day/8)   | [Python](problems/day8.py)  |                             | 
| 9   | [Day 9 - Advent of Code 2022](https://adventofcode.com/2022/day/9)   | [Python](problems/day9.py)  |                             |
| 10  | [Day 10 - Advent of Code 2022](https://adventofcode.com/2022/day/10) | [Python](problems/day10.py) |                             |
| 11  | [Day 11 - Advent of Code 2022](https://adventofcode.com/2022/day/11) | [Python](problems/day11.py) |                             |


## Logs
Writing this as notes for myself.
### Day 9
This problem, sheesh. For the first part I just wrote a simple algorithm that has the tail moving to heads previous place once head gets too far. Then, for the second part, the moving pattern in the example was completely different from what I imagined (something similar to a classical snake game).

### Day 10
Started counting cycles from 1 instead of 0 for the first part since then I can just use numbers provided in the problem to get the X. 
This really screwed up my visualization in the second part and I spent way too much time debugging it.

### Day 11
Me: Oh lets just make a monkey class
Also me: Nah let's turn everything into arrays
Not that hard of a problem but managed to make quite the spaghetti code. Math background probably helped for the part 2.

