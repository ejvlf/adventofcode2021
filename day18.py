from common.text_manipulations import TextParser

from functools import reduce
from itertools import permutations


def gen_flatlist(puzzle : list) -> list:
  flatlist = []

  for line in puzzle:
    flatline, depth = [], 0
    for c in line:

      if c == '[':
          depth += 1
      elif c == ']':
          depth -= 1
      elif c.isdigit():  flatline.append([int(c), depth])

    flatlist.append(flatline)

  return flatlist


def explode(x : list):

  for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(x, x[1:])):
    if depth1 < 5 or depth1 != depth2:
        continue
    if i > 0:
        x[i-1][0] += num1
    if i < len(x)-2: 
        x[i+2][0] += num2
    
    return True, x[:i] + [[0, depth1-1]] + x[i+2:] 
  
  return False, x


def split(x : list):

  for i, (num, depth) in enumerate(x):

    if num < 10:
        continue
    
    down = num // 2
    
    up = num - down
    
    return True, x[:i] + [[down, depth+1],[up, depth+1]] + x[i+1:]
  
  return False, x


def add(a : int, b : int):
  x = [[num, depth+1] for num,depth in a + b]
  
  while True:

    change, x = explode(x)
    if change:
        continue
    change,x = split(x)
    if not change:
        break
  
  return x


def magnitude(x : list):
  
  while len(x) > 1:
    
    for i, ((num1, depth1), (num2, depth2)) in enumerate(zip(x, x[1:])):
      
      if depth1 != depth2:
          continue
      
      val = num1 * 3 + num2 * 2

      x = x[:i]+[[val, depth1-1]]+x[i+2:]

      break

  return x[0][0]


def solve(puzzle):
  flatlist = gen_flatlist(puzzle)
  part1 = magnitude(reduce(add, flatlist))
  part2 = max(magnitude(add(a, b)) for a, b in permutations(flatlist, 2))
  return part1, part2


def run():

    source = TextParser("day18.txt").load_file_as_list()
    part1_res, part2_res = solve(source)

    # Part 1
    print(f"Part 1 result: {part1_res}")

    #Part 2
    print(f"Part 2 result: {part2_res}")

if __name__ == "__main__":

    run()