from numpy.random import randint
import matplotlib.pyplot as plt
import numpy as np

def bilgi_olaylar_ihtimaller(ages, n):
    '''Bir sınıfta yer alan öğrencilerin yaşlarıyla ilgili çizdirilen histogramda tanımlanan olayların (events) 
    olasılıklarının simülasyonla bulunması ve ekrana yazdırılması'''
    print(f"A: Öğrencinin 21 yaşından büyük olması --> P(A): {sum(ages > 21)}/{n} = {sum(ages > 21) / n}")
    print(f"B: Öğrencinin 20 yaşında veya daha küçük olması --> P(B): {sum(ages <= 20)}/{n} = ", sum(ages <= 20) / n)
    print(f"C: Öğrencinin 20 yaşından daha küçük veya 21 yaşından daha büyük olması --> P(C): {sum(ages < 20) + sum(ages > 21)}/{n} = {sum((ages < 20) | (ages > 21)) / n}")
    print(f"D: Öğrencinin 20 yaşında olması --> P(D): {sum(ages == 20)}/{n} = {sum(ages == 20) / n}")
    print(f"E: Öğrencinin 18 yaşında olması --> P(E): {sum(ages == 18)}/{n} = {sum(ages == 18) / n}")
    print(f"F: Öğrencinin 20 yaşından küçük olması --> P(F): {sum(ages < 20)}/{numberOfStudents} = {sum(ages < 20) / numberOfStudents}")
    print(f"E|F: 20 yaşından küçük olan bir öğrencinin 18 yaşında olması --> P(E|F): {sum(ages == 18)}/{sum(ages < 20)} = {sum(ages == 18)/sum(ages < 20)}")
    print(f"F|B: 20 yaşında veya daha küçük olan bir öğrencinin 20 yaşından küçük olması --> P(F|B): {sum(ages < 20)}/{sum(ages <= 20)} = {sum(ages < 20) / sum(ages <= 20)}")

numberOfStudents = 25000 # öğrenci sayısı
minAge, maxAge = 18, 27 # yaş aralığı
ages = randint(minAge, maxAge+1, numberOfStudents) # rastgele yaşlar (tekdüze dağılım - uniform distribution)
# olaylar hakkında bilgi veren, ihtimalleri hesaplayan ve ekrana yazdıran fonksiyonu çağır
bilgi_olaylar_ihtimaller(ages, numberOfStudents)
# ages dizisinde yer alan yaşları histogramda göster
counts, bins, patches = plt.hist(
    ages,
    bins=np.arange(minAge-0.5, maxAge+0.5+1, 1),
    edgecolor='black',
    color='lightgray'
)
for i, patch in enumerate(patches):
    x = patch.get_x() + patch.get_width() / 2
    y = patch.get_height()
    plt.text(x, y, str(int(counts[i])), ha='center', va='bottom', fontsize=12)
plt.title('Öğrenci Yaş Histogramı'); plt.xlabel('Yaş'); plt.ylabel('Öğrenci Sayısı')
plt.show()