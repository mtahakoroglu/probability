import numpy as np

students = ["Patrick", "Abdullah", "Sefa", "Cindy", "Furkan", "Safa"]
n = 100
count = 0

for _ in range(n):
    np.random.shuffle(students)
    for i in range(len(students) - 1):
        print(students, end=" ")
        if (students[i] == "Sefa" and students[i + 1] == "Safa") or (students[i] == "Safa" and students[i + 1] == "Sefa"):
            count += 1
            print(1)
            break
        else:
            print(0)

probability = count / n
print(f"Sefa and Safa are next to each other {count} times out of {n} shuffles.")
print(f"Probability: {probability}")