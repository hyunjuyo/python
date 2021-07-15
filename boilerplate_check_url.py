import os
import requests

def do_check(str):
  for s in str:
    i = str.index(s)
    if s.count('.') == 0:
      print(f"{s} is not a valid URL.")
      return
    if "http://" not in s:
      s = "http://" + s
      str[i] = s

  for s in str:
    try:
      r = requests.get(s)
      if int(r.status_code) == 200:
        print(f"{s} is up!")
      else:
        print(f"{s} is down!")
    except:
      print(f"{s} is down!")

while(1):
  print("Welcome to IsItdown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")

  input_str = input()

  input_str = input_str.lower()
  input_str = input_str.replace(" ","")
  split_str = input_str.split(',')

  do_check(split_str)

  flag = 0
  while(1):
    r = input("Do you want to start over? y/n ")
    if r == "y":
      flag = 1
      os.system('clear')
      break
    elif r == "n":
      flag = 0
      break
    else:
      print ("That's not a valid answer")

  if flag == 1:
    continue
  else:
    break

print("k. bye!")