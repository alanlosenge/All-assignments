print("Welcome to my factorial calculation program")
n = int(input("Which factorial do you want to calculate: "))

factorial = 1
if (n < 0):
  print("Invalid input")

for i in range(1, n + 1):
  factorial *= i

print(factorial)
