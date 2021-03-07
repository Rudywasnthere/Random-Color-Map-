##Rudy Garcia
import colored
from colored import stylize
import random
import time
import math

MENU = "\tChoices:\n1: rectangle of random colors\n2: rectangular permutation of all 256 colors"
symbol = "\u25AE"
symbol_2 = symbol + symbol
symbol_4 = symbol_2 + symbol_2

def colors_xD(u_range, minimum, num, s):
  final= ""
  line = ""
  space = " "
  if s == "n":
    space = ""
  lin_num = int(u_range/minimum)
  for x in range(0, lin_num):
    random_nums = []
    line = ""
    for y in range(1,minimum + 1):
      random_num = random.randint(0,255)
      while random_num in random_nums:
        random_num = random.randint(0,255)
      random_nums.append(random_num)
      plc = lin_num*(x) + y
      if plc < 10:
        spaces = "  "
      if plc >= 10 and plc < 100:
        spaces = " "
      if plc >= 100:
        spaces = ""
      if num == True:
        line += str(stylize(f"{plc}{spaces} - {symbol_4}", colored.fg(random_num)) + space)
      else:
        line += str(stylize(f"{symbol_4}", colored.fg(random_num)) + space)
    final += line + "\n"
  time.sleep(minimum/5)
  final.replace("�", "")
  return final

def nice_colors(u_range, minimum, num, s):
  final= ""
  line = ""
  space = " "
  if s == "n":
    space = ""
  rand_save = 0
  lin_num = int(u_range/minimum)
  for x in range(0, lin_num):
    random_nums = []
    line = ""
    for y in range(1,minimum + 1):
      random_num = random.randint(0,255)
      if y == 1:
        rand_save = random_num
      while random_num in random_nums:
        random_num = random.randint(0,255)
      random_nums.append(random_num)
      plc = lin_num*(x) + y
      if plc < 10:
        spaces = "  "
      if plc >= 10 and plc < 100:
        spaces = " "
      if plc >= 100:
        spaces = ""
      if x%2 == 1:
        if y == 1:
          line += str(stylize(f"{symbol_2}", colored.fg(random_num)) + space)
        elif y!= 1:
          line += str(stylize(f"{symbol_4}", colored.fg(random_num)) + space)
      else:
        if y == minimum:
          pass
        line += str(stylize(f"{symbol_4}", colored.fg(random_num)) + space)
    if x%2 == 1:
          line += str(stylize(f"{symbol}", colored.fg(rand_save)))
    final += line + "\n"
  time.sleep(minimum/5)
  final.replace("�", "")
  return final

def range_input(low, high, reason = ""):
  play = False
  while play == False:
    if reason == "":
      usr_range = input("number or colors (? for range): ")
    elif reason == "m":
       usr_range = input("Your choice: ")
    if usr_range == "?":
      print(f"Range between {low} and {high}, any number greater than {high} will be {high}, any less than {low} will go to {low}")
    try:
      usr_range = int(usr_range)
      if usr_range > high:
        usr_range = high
      if usr_range < low:
        usr_range = low
      return usr_range
    except:
      pass

def factorer(usr_range):
  minimum = 256
  low = 0
  floor = math.floor(usr_range**0.5) + 1
  for x in range(1, floor):
    if usr_range%x == 0:
      val = abs(usr_range//x - x)
      if val < minimum or val == 0:
        minimum = val
        low = x
  if minimum == 256:
   low = 1
  return low

def num():
  nums = False
  nums_t = input("Do you want the numbers showing? (yes or no): ").lower()
  if nums_t == "yes":
    nums = True
  return nums

def factorial(usr_range):
  poss = 1
  ten_count = 0
  for x in range(1, usr_range+1):
    poss *= x
  if poss > 1000000000:
    poss = str(poss)
    ten_count = len(poss)
    poss = poss[0:1] + "." + poss[1:5]
    poss = f"{poss} e{ten_count}"
  return poss

def p(usr_range):
  poss = 256
  for x in range(1,usr_range):
    poss *= (256-x)
  if poss > 1000000000:
    poss = str(poss)
    ten_count = len(poss)
    poss = poss[0:1] + "." + poss[1:5]
    poss = f"{poss} e{ten_count}"
  return poss

def int_input(reason):
  is_int = False
  while is_int == False:
    if reason == "h":
      integer = input("height: ")
    if reason == "w":
      integer = input("width: ")
    try:
      integer = int(integer)
      return integer
      is_int = True
    except:
      pass
  
def rectangle(height, width, spaces):
  for x in range(0,height):
    line = " "
    for y in range(0,width):
      rand_num = random.randint(0,255)
      line += str(stylize(f"{symbol_4}", colored.fg(rand_num)) + spaces)
    rand_time = width/random.randint(100,400)
    good_length = 5*width - 1
    print(line[0:len(line) -1])

def nice_rectangle(height, width, spaces):
  rand_save = 0
  for x in range(0,height):
    line = " "
    if x%2 == 0:
      for y in range(0,width):
        rand_num = random.randint(0,255)
        line += str(stylize(f"{symbol_4}", colored.fg(rand_num)) + spaces)
      rand_time = width/random.randint(100,400)
      time.sleep(rand_time)
      print(line)
    if x%2 ==1:
      for y in range(1,width+1):
        random_num = random.randint(0,255)
        if y == 1:
          rand_save = random_num
          line += str(stylize(f"{symbol_2}", colored.fg(random_num)) + spaces)
        elif y!= 1:
            line += str(stylize(f"{symbol_4}", colored.fg(random_num)) + spaces)
      line += str(stylize(f"{symbol}", colored.fg(rand_save)))
      print(line)


def main():
  print("I do colors :)\n")
  end_seq = ""
  while end_seq == "":
    space = " "
    print(MENU)
    main_choice = range_input(1,2, "m")
    if main_choice == 1:
      height = int_input("h")
      width = int_input("w")
      spaces = input("spaces (n for no):")
      if spaces == "n":
        space = ""
      if height%2 == 1:
        nice_rectangle(height, width, space)
      if height%2 == 0:
        rectangle(height, width, space)
    if main_choice == 2:
      usr_range = range_input(1, 256)
      spaces = input("spaces (n for no):")
      nums = num()
      minimum = factorer(usr_range)
      if usr_range/minimum%2 == 1 and minimum != 1:
        color_map = nice_colors(usr_range, minimum, nums, spaces)
      else:
        color_map = colors_xD(usr_range, minimum, nums, spaces)
      poss = p(usr_range)
      print(f"\n{color_map}\n\nThere are {poss} possible permutations of this color map\n\t\tHit Enter to continue\t\t\n")
    end_seq = input("\t\t\t\t")
  for x in range(0,6):
    end_of = "."*x
    print(end_of , end = "\r")
    time.sleep(1)

main()