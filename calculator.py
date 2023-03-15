#Building a simple calculator to excercise my knowledge on python programming
#look into the code again and make it recursive
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

should_continue =  True
while should_continue:

  num1 = int(input("What is the first number?: ").title())
  num2 = int(input("What is the second number?: ").title())

  for symbols in operation:
    print(symbols)
  operation_symbols = input("Pick an operation from the line above")
  calculation_function = operations[operation_symbols]
  answer = calculation_function(num1, num2)
  print(answer)
