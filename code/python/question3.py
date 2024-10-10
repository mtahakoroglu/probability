from itertools import combinations

# Define the list of fruits
fruits = ['Elma', 'Muz', 'Portakal', 'Ananas', 'Üzüm']

# Generate all combinations of 3 fruits
comb = combinations(fruits, 3)

# Convert to list and print
comb_list = list(comb)
for c in comb_list:
    print(c)