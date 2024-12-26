import numpy as np

students = ["Patrick", "Abdullah", "Sefa", "Cindy", "Furkan", "Safa"]
n = 10000
count = 0

for i in range(n):
    np.random.shuffle(students)
    for j in range(len(students) - 1):
        if (students[j] == "Sefa" and students[j + 1] == "Safa") or (students[j] == "Safa" and students[j + 1] == "Sefa"):
            count += 1
            print(i+1, end=" ")
            print(students, end=" ")
            print(1)
            break
        # else:
        #     print(0)

probability = count / n
print(f"Sefa and Safa are next to each other {count} times out of {n} shuffles.")
print(f"Probability: {probability}")