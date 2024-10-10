import numpy as np

# Parametreler (parameters)
n = 10000  # örnek sayısı (number of samples (trials))
k = 6    # öğrenci sayısı - number of students
students = np.array(['E', 'E', 'E', 'E', 'K', 'K'])  # başlangıç dizilimi
count = 0  # kızlar yanyana geldiği durumları say

for _ in range(n):
    shuffled_students = np.random.permutation(students) # öğrencileri rasgele sırala
    girl_indices = np.where(shuffled_students == 'K')[0] # kız öğrencilerin index'lerini al
    if abs(girl_indices[0] - girl_indices[1]) == 1: # kızlar yanyanaysa sayıcıyı artır
        count += 1

print(f'Toplam {n} örnekle yapılan denemede olasılık {count/n:.3f} bulundu.')