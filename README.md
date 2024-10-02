<h2>EEM 217 Olasılık (Probability) Kuramı</h2>
<h3>Hafta 1-2: Permütasyon ve Kombinasyon</h3>
<p align="justify">İlk derslerimizde bugüne kadar ortaokul ve lisede en çok karşımıza çıkan permütasyon ve kombinasyon konularını hatırlayacağız. Yalnız burada karşılaştığımız soruları sadece bu metotlarla değil, aynı zamanda gelecek haftalarda öğreneceğimiz toplam olasılık ve koşullu olasılık kavramlarını kullanarak da çözeceğiz. Bu bize güzel bir başlangıç olacak. Analitik (matematiksel) çözümünü farklı yollardan yaptığımız bu soruları ayrıca bilgisayar ortamında bir programlama diliyle rasgele sayı üreteci (random number generator) kullanarak nümerik olarak da çözüp teorik olarak elde ettiğimiz çözümlerin doğruluklarını test edeceğiz.</p>

<p align="justify"><b>Soru 1:</b> Bir sınıfta altı öğrenci vardır. Öğrencilerden ikisi kızdır. Öğrenciler sınıfın önde yer alan sıralarına yanyana rasgele oturduklarında kız öğrencilerin yanyana gelme olasılığı nedir?</p>

<p align="justify"><b>Çözüm 1:</b> Burada sıraları görselleştirip de "bir sıraya kaç kişi oturabilir" diye düşünerek sayıları tahtaya yazarsak altı öğrencinin sıralara toplam kaç farklı biçimde oturabileceğini hesaplarız. İlk sıraya 6 öğrenci oturabilirken ikinci sıraya doğal olarak 5 kişi oturabilecek ve bu şekilde son sıraya tek öğrenci kalacak biçimde devam edecektir.</p>

| 1. sıra | 2. sıra | 3. sıra | 4. sıra | 5. sıra | 6. sıra |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
| 6 | 5 | 4 | 3 | 2 | 1 |

<p align="justify">Sıralara yazdığımız bu sayılar çarpım ile bize</p>

$$6 x 5 x 4 x 3 x 2 x 1 = 6!$$

<p align="justify">değerini verir. Yâni altı öğrenci yanyana 120 farklı biçimde oturabilmekte. Bizden istenen bu kadar farklı oturma düzeninin hangilerinde iki kız arkadaşın yanyana düştükleri. Burada biraz düşünürsek iki kız arkadaşı tek bir insan gibi kabul edip toplamda 5 kişiyinin yanyana toplam</p>

$$5!$$

<p align="justify">biçimde oturabileceğini buluruz. A olayını aşağıdaki gibi tanımlarsak</p>

$$A: \text{İki kızın yanyana gelmesi}$$

<p align="justify">o zaman, iki kızın yanyana gelme olasılığı</p>

$$P(A) = \frac{5!}{6!}$$

<p align="justify">olarak bulunur. Yalnız buraya kadar olan mantığımızda birşeyi atladık: Kızları tek bir insan gibi düşünüp de $5!$ değerini elde etmemiz mantıklıydı ama kız öğrenciler kendi aralarında yer değiştirebilirler. Bu durumu da hesaba katmalıyız. İki kız kendi aralarında</p>

$$2!$$

<p align="justify">şekilde oturabilir. Daha önceden elde ettiğimiz çözümü bu durumu da hesaba katarak güncellersek</p>

$$P(A) = \frac{5! 2!}{6!}= \frac{1}{3} = 0.33$$

<p align="justify">olasılığını buluruz.</p>

<p align="justify"><b>Çözüm 2:</b> Şimdi bu soruya başka bir açı olan <b>koşullu olasılık</b> ve <b>toplam olasılık</b> kavramları üzerinden yaklaşalım ve ikinci bir teorik yaklaşımla aynı sonucu elde etmeye çalışalım. Kafamızda durumu canlandıralım diye erkeklere E kızlara K diyerek örnek bir sıralamayı aşağıda görselleştirelim.</p>

| 1. sıra | 2. sıra | 3. sıra | 4. sıra | 5. sıra | 6. sıra |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
| E | E | K | E | K | E |

<p align="justify">Aynen yukarıdaki sıralama gibi $6!=120$ farklı oturma düzeneği olabileceğini daha önceden bulmuştuk. Şimdi sıralara kimseyi yerleştirmeden önce iki kız arkadaştan birisini alıp bu sıralara ilk önce onu rasgele yerleştirmeyi düşünelim. Zaten rasgele oturmalarda da aynı anda herkes farklı bir yere oturamayacak, herkes bir sekans (sequence) olarak oturmak zorunda kalacaktır. Bunu biraz düşünürsek anlarız. Boş altı sırayı kafamızda hayal edip iki kız arkadaşımızdan birini boş yerlerden birine koymayı düşündüğümüzde karşımıza iki durum çıkacaktır. İlk durumda kız arkadaşımızın kenar sıralara değil de orta sıralara oturma ihtimali, ikincisi de bunun tamamlayıcısı (complementary) olan kenardaki sıralara oturma ihtimali. Örneklem uzay $S$ (sample space) diye burada tanıttığımız olasılıklar uzayının bu şekilde ikiye bölünmesinin sebebi ilk yerleşen kız arkaşımızın ortaya oturduğu takdirde her iki yanına da kız arkadaşının gelebilem ihtimalinin, kenara oturduğu zaman değişmesi. Mesela aşağıki görselde ilk oturan kız arkadaşımızın 3. sıraya oturduğunu farz edelim. Bu durumda ilk oturan kızın arkadaşı olan kız geri kalan beş sıradan ikisine oturabilir</p>

| 1. sıra | 2. sıra | 3. sıra | 4. sıra | 5. sıra | 6. sıra |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
|  |  | <b>K</b> | K |  |  |

| 1. sıra | 2. sıra | 3. sıra | 4. sıra | 5. sıra | 6. sıra |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
|  | K | <b>K</b> |  |  |  |

<p align="justify">ki bu yanyana oturma ihtmallerini $\frac{2}{5}$ yapar. Öte yandan aşağıdaki örnek sıralamadaki gibi ilk oturan kız kenara oturursa<p>

| 1. sıra | 2. sıra | 3. sıra | 4. sıra | 5. sıra | 6. sıra |
|  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |  :---:  |
|  |  |  |  | K | <b>K</b> |

<p align="justify">o zaman da arkadaşının onun yanına oturma ihtimali $\frac{1}{5}$ olur. Şimdi burada ilk oturan kızın ortaya ve kenara oturma durumlarını sembolik olarak olaylar şeklinde tanımlayalım.<p>

$$O: \text{İlk oturan kızın ortaya oturması}$$

$$O': \text{İlk oturan kızın kenara oturması}$$

<p align="justify">Eğer bir üçüncü durum söz konusu olsaydı onu da hesaba katmalıydık ama burada örneklem uzay ikiye bölünmüş halde. İlgilendiğimiz olay olan "iki kızın yanyana gelmesi" durumunu yukarıda $A$ olarak tanımlamıştık. O zaman örneklem uzayın Venn şeması hâlinde temsili aşağıdaki gibi olur.</p>

<img src="resim/question1.jpg" alt="yanyana oturma sorusu örneklem uzay" width="400" height=auto>

<p align="justify">Uzayda koşullu olasılıklara bakmaya başlıyoruz.</p>

$$ A | O: \text{İlk oturan kız ortaya oturduğunda yanyana gelmeleri}$$

$$ A | O': \text{İlk oturan kız kenara oturduğunda yanyana gelmeleri}$$

<p align="justify">Burada ilk önce "ilk kızın ortaya oturması ve o ortaya oturduğunda arkadaşının onun yanına gelmesi ihtimalini" hesap edecek, hemen ardından yaptığımız işlemin örneklem uzayda tamamlayıcısı olan "ilk kızın kenara oturması ve o kenara oturduğunda arkadaşının onun yanına gelmesi" ihtimalini de bulacağız. Son olarak da elde edilen ihtimalleri toplayıp bütün durumlar için "iki arkadaşın yanyana gelme" olasılığını göreceğiz.</p>

$$P(A) = P(A|O)P(O)+P(A|O')P(O')$$

<p align="justify">İlk oturan kızın sıraların ortasına denk gelmesi ihtimali $P(O) = \frac{4}{6}$ iken tamamlayıcısı olan kenara denk gelme durumu da $P(O) = \frac{2}{6}$ olarak bulunur. $P(A|O)$ ve $P(A|O)$ ifadelerini de yukarıda hesap ettiğimizden, herşeyi yerine koyarsak</p>

$$P(A) = \frac{2}{5}\frac{4}{6}+\frac{1}{5}\frac{2}{6}$$

<p align="justify">olur. Devam edersek yukarıda ilk yolla bulduğumuz değerin aynısını buluruz.</p>

$$P(A) = \frac{1}{3}=0.33$$

<p align="justify"><b>Çözüm 3:</b> Şu ana kadar izlediğimiz yolların hepsi matematiksel çözüm denilen analitik çözümlerdi. Burada bilgisayarlarda yer alan sayıcıları (counter) ve zamanlayıcıları (timer) kullanarak rasgele sayı üreten (random number generation) algoritmalar ile çözümü simüle edeceğiz. Bunu yapmak için istatistikteki <b>büyük sayılar kanunu</b>ndan (the law of large numbers) faydalanacağız. Sonuçta çözümü bir de nümerik olarak bulmaya çalışacağız.</p>

<p align="justify">Aşağıdaki kodları değişik seferlerde koşturduğumuzda kız arkadaşların yanyana denk gelme olasılığının teoride hesaplanan değere yakın olduğunu, özellikle $n$ parametresi olan örnek sayısı (number of samples) değişkenini büyüttükçe her denemede olasılığın iyice $0.33$'e yaklaştığını görebiliriz.</p>

<h5><b>question1.py</b></h5>

```
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
```

<h5><b>question1.m</b></h5>

```
n = 10000; % örnek sayısı (number of samples)
k = 6; % öğrenci sayısı
student = ['E','E','E','E','K','K']; % başlangıç durumu, istenildiği gibi olabilir
count = 0; % kızların yanyana geldiği durumlar
for i=1:n
    girl_index = find(student(randperm(k)) == 'K');
    if abs(girl_index(1)-girl_index(2)) == 1 % yanyana iseler sıra numaraları farkı 1 olmalı
        count = count+1;
    end
end
fprintf('Toplam %i örnekle yapılan denemede olasılık %.3f bulundu.\n', n, count/n);
```