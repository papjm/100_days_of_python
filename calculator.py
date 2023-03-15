#Building a simple calculator to excercise my knowledge on python programming

#Add
def Add(n1, n2):
  return n1 + n2

#subtract
def Subtract(n1, n2):
  return n1 - n2

#multiply
def Multiply(n1, n2):
  return n1 * n2

#divide
def Divide(n1, n2):
  return n1 / n2

operations = {
  "-" : Subtract,
  "+" : Add,
  "*" : Multiply,
  "/" : Divide
}

num1 = int(input("What is the first number?: ").title())
num2 = int(input("What is the second number?: ").title())
