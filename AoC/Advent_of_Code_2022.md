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

| Day | Problem link                                                         | Solution                         | Cleaner                          |
| --- | -------------------------------------------------------------------- | -------------------------------- | -------------------------------- |
| 1   | [Day 1 - Advent of Code 2022](https://adventofcode.com/2022/day/1)   | [Python](2022_problems/day1.py)  |                                  |
| 2   | [Day 2 - Advent of Code 2022](https://adventofcode.com/2022/day/2)   | [Python](2022_problems/day2.py)  |                                  |
| 3   | [Day 3 - Advent of Code 2022](https://adventofcode.com/2022/day/3)   | [Python](2022_problems/day3.py)  |                                  |
| 4   | [Day 4 - Advent of Code 2022](https://adventofcode.com/2022/day/4)   | [Python](2022_problems/day4.py)  |                                  |
| 5   | [Day 5 - Advent of Code 2022](https://adventofcode.com/2022/day/5)   | [Python](2022_problems/day5.py)  | [Python](2022_problems/day5b.py) |
| 6   | [Day 6 - Advent of Code 2022](https://adventofcode.com/2022/day/6)   | [Python](2022_problems/day6.py)  |                                  |
| 7   | [Day 7 - Advent of Code 2022](https://adventofcode.com/2022/day/7)   | [Python](2022_problems/day7.py)  |                                  |
| 8   | [Day 8 - Advent of Code 2022](https://adventofcode.com/2022/day/8)   | [Python](2022_problems/day8.py)  |                                  |
| 9   | [Day 9 - Advent of Code 2022](https://adventofcode.com/2022/day/9)   | [Python](2022_problems/day9.py)  |                                  |
| 10  | [Day 10 - Advent of Code 2022](https://adventofcode.com/2022/day/10) | [Python](2022_problems/day10.py) |                                  |
| 11  | [Day 11 - Advent of Code 2022](https://adventofcode.com/2022/day/11) | [Python](2022_problems/day11.py) |                                  |
| 12  | [Day 12 - Advent of Code 2022](https://adventofcode.com/2022/day/12) | [Python](2022_problems/day12.py) |                                  |
| 13  | [Day 13 - Advent of Code 2022](https://adventofcode.com/2022/day/13) |                                  |                                  |
| 14  | [Day 14 - Advent of Code 2022](https://adventofcode.com/2022/day/14) | [Python](2022_problems/day14.py) |                                  |
| 15  | [Day 15 - Advent of Code 2022](https://adventofcode.com/2022/day/15) |                                  |                                  |
| 16  | [Day 16 - Advent of Code 2022](https://adventofcode.com/2022/day/16) |                                  |                                  |


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

### Day 12
Messy solution, will add a cleaner one later. The part 2 looked the same as part 1 except we don't know the exact start. So I just inverted everything, so that we have one start and multiple ends and checked if we reached the end.

### Day 13
Didn't have time and looked hard to parse. Will do it later.

### Day 14
Took me long time to do this one. All approaches were similar to the first working solution but somehow I was getting numbers that were 2-3% off.

### Day 15



