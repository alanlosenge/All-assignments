print("Welcome to my fibonnaci sequence program")
n = int(input("How many Fibonnaci terms (n) do you want to generate: "))

if (n <= 0):
  print("Invalid input")


def fibonnaci(n):
  """
  A simple pythom script to print out the fibonnaci sequence up to a given n-th term provided by a user input
  """


fib = [0, 1]
for i in range(2, n):
  fib.append(fib[i - 1] + fib[i - 2])

print(fib)
