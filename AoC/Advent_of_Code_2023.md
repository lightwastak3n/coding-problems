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
| 12  | [Day 12 - Advent of Code 2023](https://adventofcode.com/2023/day/12)   | [Python](2023_problems/day12.py)  |  |
| 13  | [Day 13 - Advent of Code 2023](https://adventofcode.com/2023/day/13)   | [Python](2023_problems/day13.py)  | [Javascript](2023_problems/day13.js) |
| 14  | [Day 14 - Advent of Code 2023](https://adventofcode.com/2023/day/14)   | [Python](2023_problems/day14.py)  | [Python](2023_problems/day14b.py) |
| 15  | [Day 15 - Advent of Code 2023](https://adventofcode.com/2023/day/15)   | [Python](2023_problems/day15.py)  |  |


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

### Day 12
Took a while. Done with brute force, not sure how to improve it.

### Day 13
Not a hard problem but the description was a bit confusing to me.

### Day 14
No idea how to do the part 2 in code. I did a couple of hundred of cycles and looked at the total load at the end of each and saw that first 125 cycles gave basically random numbers and then it started repeating in a cycle of length 21. Had to mod the total load since the numbers were 100k+ and hard to see. So the answer was (1b - 125) % 21 and then just find the correct load in that cycle.
Did it in a cleaner way. HyperNeutrino explained how to find the cycles for the part 2 here https://youtu.be/WCVOBKUNc38?t=544
Clean version is still really slow ~ 0.8 s.
Used cProfile for timing and it says:
```python
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   361905    0.020    0.000    0.020    0.000 {built-in method builtins.len}
    57300    0.005    0.000    0.005    0.000 {method 'reverse' of 'list' objects}
    14645    0.006    0.000    0.006    0.000 day14b.py:50(<genexpr>)
      572    2.000    0.003    2.003    0.004 day14b.py:17(move_rocks_left)
      572    0.072    0.000    0.077    0.000 day14b.py:35(rotate_right)
      286    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
      145    0.002    0.000    0.008    0.000 day14b.py:49(grid_hash)
      144    0.132    0.001    0.149    0.001 day14b.py:26(get_load)
      142    0.004    0.000    0.004    0.000 {method 'add' of 'set' objects}
```
so I guess `move_rocks` and `get_load` are major slowdowns.

### Day 15
One of the easiest days so far. Took way longer to read part 2 and understand it than to actually code it.
