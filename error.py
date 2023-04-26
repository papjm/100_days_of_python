try
except
else
finally

try:
  file = open("a_file.txt")
  a_dictionary = {"key": "value"}
  print(a_dictionary[asdg])
  
except FileNotFoundError:
  file = open("a_file.txt", "w")
  file.write("Something")

except KeyError:
  print("That key does not exist")
  
