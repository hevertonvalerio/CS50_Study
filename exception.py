try:
  x = int(input("Whatz's X?"))
except ValueError:
  print("x is not an integer")

print(f"X is {x}")