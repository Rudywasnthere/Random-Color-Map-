##Rudy Garcia
import colored
from colored import stylize
import random
import time
import math


def colors_xD(u_range, minimum, num):
  final= ""
  line = ""
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
        line += str(stylize(f"{plc}{spaces} - ▮▮▮▮", colored.fg(random_num)) + " ")
      else:
        line += str(stylize(f"▮▮▮▮", colored.fg(random_num)) + " ")
    final += line + "\n"
  time.sleep(minimum/10)
  final.replace("�", "")
  return final

def range_input():
  play = False
  while play == False:
    usr_range = input("number or colors (? for range): ")
    if usr_range == "?":
      print("Range between 1 and 256, any number greater than 256 will be 256, any less than 1 will go to 1")
    try:
      usr_range = int(usr_range)
      if usr_range > 256:
        usr_range = 256
      if usr_range < 1:
        usr_range = 1
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

def main():
  print("I do colors :)\n")
  usr_range = range_input()
  nums = num()
  minimum = factorer(usr_range)
  color_map = colors_xD(usr_range, minimum, nums)
  poss = p
  print(f"\n{color_map}\n\nThere are {poss} possible permutations of this color map")

main()
