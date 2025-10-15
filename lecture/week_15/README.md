<h3>Hafta 15: Rasgele Sayı Üreteci ile Simülasyon</h3>

<p align="justify"><b>Soru:</b> Bölüm öğrencilerinden Patrick, Abdullah, Sefa, Cindy, Furkan ve Safa beraber resim çekilecekler. Resimde rasgele biçimde yanyana duracaklar. Öğrencilerden Sefa ile Safa'nın resimde yanyana gelme olasılığı nedir?</p>

<p align="justify"><b>Analitik (Matematiksel Çözüm):</b> Bu sorunun çözümünü hem permütasyon yoluyla hem de koşullu ve toplan olasılık formülleriyle derste yaparak cevabı 1/3 bulduk.</p>

<p align="justify"><b>Nümerik Çözüm (Simülasyon):</b> EEM 215 Mühendislikte Programlama dersinde öğrendiğimiz rasgele sayı üretecini kullanarak burada bu altı kişiyi toplam <b>n</b> defa rasgele yanyana dizelim ve her sıralama için Sefa ile Safa'nın yanyana gelip gelmediğini kontrol ederek ihtimal hesabını bu sefer sayarak bulalım.</p>

<b>sefa_safa.py</b>

```
import numpy as np

students = ["Patrick", "Abdullah", "Sefa", "Cindy", "Furkan", "Safa"]
n = 1000
count = 0

for i in range(n):
    np.random.shuffle(students)
    print(i+1, students, end=" ")
    found = False
    for j in range(len(students)-1):
        if (students[j] == "Sefa" and students[j+1] == "Safa") or (students[j] == "Safa" and students[j+1] == "Sefa"):
            count += 1
            print(1)
            found = True
            break
    if not found:
        print(0)

probability = count / n
print(f"Sefa and Safa are next to each other {count} times out of {n} shuffles.")
print(f"Probability: {probability}")
```

<p align="justify"><b>Soru:</b> Aynı okulda farklı sınıflarda okuyan iki arkadaş gizlice sigara içmek için öğlen teneffüsünde okulun arkasında gizli bir yerde buluşacaklar. Arkadaşların birisinde sigara öbüründe ateş var. Ancak derse girmeden birbirleriyle sözleşmediklerinden dolayı 1 saatlik (yâni 60dk'lık) öğlen molasının hangi kısmında gizli yerlerinde olacaklarını birbirlerine söylemeyi unutmuşlar. Her ikisi de buluşma yerine gittiklerinde öbür arkadaşı en fazla 20dk bekleyip sınıfına dönmek zorunda. Bu iki arkadaşın teneffüste sigara içme olasılığı nedir? (5 Puan) Bu sorudaki rasgele değişkenler nelerdir? (Bonus +10 Puan) Derste bu sorunun nümerik çözümünü (simülasyonunu) Python’da numpy paketinden random sınıfından rand rasgele sayı üreticisini kullanarak toplam beş satırda yapmıştık. Simülasyonun parametreleri örnek sayısı n ve dakika cinsinden zaman penceresi büyüklüğü w idi. Burada aynı kodu yazınız. 
</p>

<p align="justify">Not: Her iki arkadaşın kullanabilecekleri 20dk'lık maksimum vakti x ve y eksenleri üzerinde inceleyerek soruya grafiksel olarak yaklaşabilirsiniz.</p>