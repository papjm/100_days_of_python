#learning object orientated programming
from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("pokemon name", ["pikachu", "squirtle", "charmander"])
table.add_column("Type", ["electric", "water", "fire"])
print(table)
