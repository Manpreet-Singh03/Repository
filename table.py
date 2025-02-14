number = int(input("Enter a number whose table is to be printed: "))
print(f"Multiplication Table of {number}")

for i in range(1, 11):
  print(f"{number} * {i} = {i*number}")
  