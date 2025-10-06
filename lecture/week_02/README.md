<h3>Hafta 2 Özhazırlık: Kombinasyon ve Koşullu/Toplam Olasılık - devam</h3>

<p align="justify"><b>Soru 2:</b> İki arkadaş sinemaya gidiyorlar. Girdikleri sinema salonu 5 x 10 kapasitelik. Yani 5 sıra var ve her bir sırada 10 koltuk var. Arkadaşlar birbirlerinden habersiz bilet alıyorlar. Koşullu Olasılık ve Toplam Olasılık kavramlarını kullanarak iki arkadaşın filmi yan yana izleme olasılıklarını bulunuz.</p>

<img src="../../image/sinema salonu koşullu ve toplam olasılık.jpg" alt="5x10 boyutunda bir sinema salonu" width=400 height=auto>

<p align="justify"><b>Çözüm 2:</b> Bu sorunun çözümü ikinci hafta derste yapılmıştır. Bu sorunun benzeri sınavlarda (hem ara sınavda hem finalde) karşımıza çıkacaktır.</p>

<p align="justify"><b>Soru 3: (Kombinasyon)</b> Evde meyve olarak Elma, Muz, Portakal, Ananas ve Üzüm var. Gelen misafire meyve ikram edilecek. Ev sahipleri yukarıda sayılan beş çeşit meyveden üç tanesini beraber ikram etmeye karar veriyor.</p>

<ul>
<li>Kaç farklı meyve tabağı hazırlanabilir?</li>
<li>İkram edilen tabaklarda elma ve portakal bulunma olasılığı nedir?</li>
</ul>

<p align="justify">Not: Kombinasyon ile yapamazsanız sayarak yapabilirsiniz. Mesela bütün kombinasyonların bulunduğu küme</p>

<p>S = { EMP, EMA, EMÜ, … }</p>

<p align="justify">şeklinde devam etmektedir. Kendiniz bu kümeyi tamamen oluşturup sonra ilgili kombinasyonları sayarak cevabı bulabilirsiniz.</p>

<p align="justify"><b>Çözüm 3:</b> Beş çeşit meyveden üç tanesini seçmeyi kombinasyon (combination) ile yapacağız.</p>

$$\binom{5}{3} = \frac{5!}{3!(5-3)!}=\frac{5!}{3!2!}=\frac{5x4}{2}=10$$

<p align="justify">Toplam 10 farklı meyve tabağı hazırlanabilir. Bu tabakları aşağıdaki Python koduyla ekrana basarak görebiliriz.</p>

<b>question3.py</b>

```
from itertools import combinations

# Meyve listesini tanımlayalım
fruits = ['Elma', 'Muz', 'Portakal', 'Ananas', 'Üzüm']

# 3'lü bütün kombinasyonları oluşturalım
comb = combinations(fruits, 3)

# Listeye dönüştürüp ekrana basalım
comb_list = list(comb)
for c in comb_list:
    print(c)
```

<ol>
<li>('Elma', 'Muz', 'Portakal')</li>
<li>('Elma', 'Muz', 'Ananas')</li>
<li>('Elma', 'Muz', 'Üzüm')</li>
<li>('Elma', 'Portakal', 'Ananas')</li>
<li>('Elma', 'Portakal', 'Üzüm')</li>
<li>('Elma', 'Ananas', 'Üzüm')</li>
<li>('Muz', 'Portakal', 'Ananas')</li>
<li>('Muz', 'Portakal', 'Üzüm')</li>
<li>('Muz', 'Ananas', 'Üzüm')</li>
<li>('Portakal', 'Ananas', 'Üzüm')</li>
</ol>

<p align=justify>İkram edilen tabaklarda elma ve portakal bulunma olasılığı sorulmuştu. Bu iki meyvenin tabaktaysa o zaman bir meyvelik boş yer var demektir. Buraya da üç meyveden birisi gelebilir.</p>

$$\frac{\binom{3}{1}}{\binom{5}{3}} = \frac{3}{10} = 0.3$$

<p align=justify>Yâni %30 ihtimalle tabaklarda elma ve portakal birlikte yer alırlar. Bu sonucun aynısını yukarıda Python kodunda yazdırdığımız listeden de sayarak bulabiliriz.</p>

<ol>
<li><b>('Elma', 'Muz', 'Portakal') <=== Elma ve Portakal beraber</b></li>
<li>('Elma', 'Muz', 'Ananas')</li>
<li>('Elma', 'Muz', 'Üzüm')</li>
<li><b>('Elma', 'Portakal', 'Ananas') <=== Elma ve Portakal beraber</b></li>
<li><b>('Elma', 'Portakal', 'Üzüm') <=== Elma ve Portakal beraber</b></li>
<li>('Elma', 'Ananas', 'Üzüm')</li>
<li>('Muz', 'Portakal', 'Ananas')</li>
<li>('Muz', 'Portakal', 'Üzüm')</li>
<li>('Muz', 'Ananas', 'Üzüm')</li>
<li>('Portakal', 'Ananas', 'Üzüm')</li>
</ol>

<p align="justify"><b>Soru 4: (Kombinasyon)</b> Bir sepette 15 kahverengi ve 10 beyaz yumurta bulunmaktadır. Aynı anda 5 yumurta seçiliyor. Alınan yumurtalardan 3 tanesinin beyaz olma olasılığını bulunuz.</p>

<p align="justify"><b>Çözüm 4:</b></p>

$$\frac{\binom{15}{2} \binom{10}{3}}{\binom{25}{5}}=\frac{\frac{15!}{13!2!}\frac{10!}{7!3!}}{\frac{25!}{20!5!}}$$

<p align="justify">Burada işlemler uzayacağından dolayı elle hesaplama yerine Python'da <b>math</b> paketinin <b>comb()</b> komutundan faydalanarak bu değeri kolayca bulalım.</p>

```
import math
x = math.comb(15,2)*math.comb(10,3)/math.comb(25,5)
print(f"{x:.3f}")
```

$$\frac{\binom{15}{2} \binom{10}{3}}{\binom{25}{5}} = 0.237$$