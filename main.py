# How to find when to do that thing at that time
list = ["Dinner","Lunch","Breakfast"]
b = list.index(input("enter meal to tell the time:"))
if b == 0:
  print("You must eat at 8:30")
elif b == 1:
  print("You must eat at 2:00 to 2:30")
elif b == 2:
  print("Right after brushing your teeth")
