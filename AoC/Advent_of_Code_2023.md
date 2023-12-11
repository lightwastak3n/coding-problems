# Advent of Code 2023
List of problems: https://adventofcode.com/2023/

Python files are run from the problems folder or just change the input data path.
First solution is the original so it might be messy. After I get the stars I might try to write cleaner/shorter code for the second solution. 

| Day | Problem link                                                         | Solution                         | Cleaner                          |
| --- | -------------------------------------------------------------------- | -------------------------------- | -------------------------------- |
| 1   | [Day 1 - Advent of Code 2023](https://adventofcode.com/2023/day/1)   | [Python](2023_problems/day1.py)  |  [Javascript](2023_problems/day1.js)      |
| 2   | [Day 2 - Advent of Code 2023](https://adventofcode.com/2023/day/2)   | [Python](2023_problems/day2.py)  | [Python](2023_problems/day2_b.py)|
| 3   | [Day 3 - Advent of Code 2023](https://adventofcode.com/2023/day/3)   | [Python](2023_problems/day3.py)  | [Javascript](2023_problems/day3.js) |
| 4   | [Day 4 - Advent of Code 2023](https://adventofcode.com/2023/day/4)   | [Python](2023_problems/day4.py)  | [Python](2023_problems/day4b.py) [Javascript](2023_problems/day4.js) |
| 5   | [Day 5 - Advent of Code 2023](https://adventofcode.com/2023/day/5)   | [Python](2023_problems/day5.py)  |                                  |
| 6   | [Day 6 - Advent of Code 2023](https://adventofcode.com/2023/day/6)   | [Python](2023_problems/day6.py)  | [Python](2023_problems/day6b.py) [Javascript](2023_problems/day6.js)|
| 7   | [Day 7 - Advent of Code 2023](https://adventofcode.com/2023/day/7)   | [Python](2023_problems/day7.py)  |                                  |
| 8   | [Day 8 - Advent of Code 2023](https://adventofcode.com/2023/day/8)   | [Python](2023_problems/day8.py)  | [Python](2023_problems/day8b.py) [Javascript](2023_problems/day8.js) |
| 9   | [Day 9 - Advent of Code 2023](https://adventofcode.com/2023/day/9)   | [Python](2023_problems/day9.py)  | [Python](2023_problems/day9b.py) |
| 10  | [Day 10 - Advent of Code 2023](https://adventofcode.com/2023/day/10)   | [Python](2023_problems/day10.py)  | [Python](2023_problems/day10b.py) |
| 11  | [Day 11 - Advent of Code 2023](https://adventofcode.com/2023/day/11)   | [Python](2023_problems/day11.py)  | [Javascript](2023_problems/day11.js) |


## Logs
### Day 2
We are looking for the largest number in both parts not sure why I stored all of them in the first part.
Made a cleaner solution that doesn't import anything and is about 3x faster than original.

### Day 3
Looked worst than it is when reading it. Forgot to terminate numbers at the end of the line. 
Would have probably been easier to pad the entire thing with ".".

### Day 4
Did extra loop over everything in the first solution. Added JS solution as a practice. Same as Python basically.

### Day 5
So much harder than the previous day. Took me hours to solve. It's messy but I'm not sure I can make it much shorter.
It's also a bit weird with ranges order being one way in the text and the other in the actual data. Really hard to keep track of what I was doing.

### Day 6
Easiest day so far. First solution is already clean. Second solution just does both parts at once and I tried to make it more compact.

### Day 7
Hard coded all the card values basically -.-.

### Day 8
Pretty straightforward. Should have done both parts at the same time. Small input so just store all ..A elements in a dict and output both parts at the end.
`day8b.py` - both parts at the same time, math apparently has lcm method, ~30% faster than the first solution.

### Day 9
Mistakes: checked the input data but didn't saw negative numbers, that in turn caused a bug since I was checking the sum of the array to be 0 instead of all the numbers in it to be zero, 
Easiest second part of the problem so far, basically the same as first part.

### Day 10
Took me hours. You need some theory for this. Looked at visualizations and read a bit about this. Tried the shoelace algorithm, didn't work. Tried to do the flood fill before realizing that "squeezing between pipes is also allowed". Blowing up the grid by x2 so x4 elements was just too complicated together with pipes duplication. In the end I did what most people did and used up/down parity to determine if it's in or out. What goes up must come down, if it hasn't it means we are inside. It's slow though (~2s).
Redid the solution in [Python](2023_problems/day10b.py) using Shoelace + Pick's. Runtime went from ~2s to 7 ms.

### Day 11
Changed a multiplier for part 1 a few times and got the answer before realizing how it works. Increasing by n means adding n-1 colums/rows.
