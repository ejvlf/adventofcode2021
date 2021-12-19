from common.text_manipulations import TextParser

def victory_condition(x: int, x0: int, x1: int, y: int, y0: int, y1: int) -> bool:
  return x0 <= x <= x1 and y0 <= y <= y1

def fire_probe(xs: int,ys: int,n: int, x0: int, x1: int, y0: int, y1: int) -> int:
  maxy = -999999
  x,y = 0,0
  xv,yv = xs,ys

  for i in range(n):
    x += xv
    y += yv
    if y>maxy: maxy=y
    if xv>0: xv-=1
    elif xv<0: xv+=1
    yv -= 1
  
    if victory_condition(x,y,x0, x1, y0, y1):
      return maxy,i
  
  return 0,-1

def part1(x0: int, x1: int, y0: int, y1: int):
  maxy = -999999
  andxy = 0,0
  andk = 0

  for xv in range(0,20):

    for yv in range(0,200):
      mxy,k = fire_probe(xv, yv, 400,x0, x1, y0, y1)

      if k>=0:

        if mxy>maxy:

          maxy=mxy
          andxy=xv,yv
          andk=k

  return maxy,andxy,andk

def part2(x0: int, x1: int, y0: int, y1: int ):
  xyk = []
  for xv in range(0,150):
    for yv in range(-200,200):
      _,k = fire_probe(xv,yv,400,x0, x1, y0, y1)
      if k>=0:
        xyk.append((xv,yv,k))
  return xyk

def run():

    source = TextParser("day17.txt").load_file_as_raw_string().replace(",","").split()
    x0,x1=int(source[2][2:source[2].index(".")]),int(source[2][source[2].index(".")+2:])
    y0,y1=int(source[3][2:source[3].index(".")]),int(source[3][source[3].index(".")+2:])

    # Part 1
    print(f"Part 1 result: {part1(x0, x1, y0, y1)[0]}")

    #Part 2
    print(f"Part 2 result: {len(part2(x0, x1, y0, y1))}")

if __name__ == "__main__":

    run()