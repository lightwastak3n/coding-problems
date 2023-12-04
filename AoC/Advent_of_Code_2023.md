# Advent of Code 2023
List of problems: https://adventofcode.com/2023/

You can get the problem input data directly into your Python code with [get_data.py](2022_problems/get_data.py). Create a `config.json` file in problems folder and add cookie session to it or just configure it for yourself.
```json
{
	"cookie": "92d5eea06bd8a2c14a......."
}
```
This will also save the input data as a txt file for future reference. Python files are run from the problems folder.

I try to write the first solution as fast as I can, so whatever first comes to mind. After I get the stars I might try to write shorter code for the second solution. 

| Day | Problem link                                                         | Solution                         | Cleaner                          |
| --- | -------------------------------------------------------------------- | -------------------------------- | -------------------------------- |
| 1   | [Day 1 - Advent of Code 2023](https://adventofcode.com/2023/day/1)   | [Python](2023_problems/day1.py)  |                                  |
| 2   | [Day 2 - Advent of Code 2023](https://adventofcode.com/2023/day/2)   | [Python](2023_problems/day2.py)  | [Python](2023_problems/day2_b.py)|
| 3   | [Day 3 - Advent of Code 2023](https://adventofcode.com/2023/day/3)   | [Python](2023_problems/day3.py)  |                                  |
| 4   | [Day 4 - Advent of Code 2023](https://adventofcode.com/2023/day/4)   | [Python](2023_problems/day4.py)  | [Python](2023_problems/day4b.py) [Javascript](2023_problems/day4.js) |


## Logs
### Day 2
We are looking for the largest number in both parts not sure why I stored all of them in the first part.
Made a cleaner solution that doesn't import anything and is about 3x faster than original.

### Day 3
Looked worst than it is when reading it. Forgot to terminate numbers at the end of the line. 
Would have probably been easier to pad the entire thing with ".".

### Day 4
Did extra loop over everything in the first solution. Added JS solution as a practice. Same as Python basically.S