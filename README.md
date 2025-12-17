<h2>EEM 217 Olasılık Kuramı</h2>

<h3>Normal Dağılım</h3>
<p align="justify">Normal dağılımın olasılık yoğunluk fonksiyonu (probability density function – pdf) aşağıdaki şekilde tanımlanır:</p>

$$
f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}}
e^{\displaystyle \frac{(x-\mu)^2}{2\sigma^2}}
$$

<p align="justify">Burada</p>
<ul>
    <li>μ dağılımın ortalamasını (mean),</li>
    <li>σ ise standart sapmasını (standard deviation) ifade eder.</li>
</ul>

<p align="justify">Bu iki parametre, normal dağılımın hem konumunu hem de yayılımını tamamen belirler. Aşağıdaki şekilde, farklı parametre değerleri için normal dağılımın tipik görünümü verilmiştir.<br>📌 Not: Normal dağılım sürekli bir dağılımdır ve olasılıklar, pdf’in belirli aralıklardaki integrali ile hesaplanır.</p>

<img src="image/normal_distribution_pdf.png" alt="Normal dağılım olasılık yoğunluk fonksiyonu" width=500>

<p align="justify">Normal dağılımın modellediği problemlerde doğrudan integral alarak olasılık hesaplamak genellikle zahmetlidir. Bu nedenle uygulamada:</p>

<ul>
    <li>Rastgele değişken standartlaştırılır</li>
    <li>Olasılıklar standart normal dağılımın kümülatif dağılım fonksiyonu (cdf) yardımıyla hesaplanır</li>
</ul>

<p align="justify">Bu yaklaşım hesaplamaları oldukça kolaylaştırır.</p>

<h4>Standard Normal Dağılım</h4>

<p align="justify">X rastgele değişkeninin ortalaması $\mu$, varyansı $\sigma^2$ olan bir normal dağılıma sahip olduğunu varsayalım:</p>

$$\displaystyle X\sim N(\mu ,\sigma ^{2})$$

<p align="justify">Bu değişkeni, ortalamasını çıkarıp standart sapmasına bölerek standartlaştırırsak:</p>

$$\displaystyle Z = \frac{X-\mu}{\sigma} \sim N(0, 1)$$

<p align="justify">elde edilir. Bu dönüşüm sayesinde, tüm olasılık hesapları tek bir tablo (standart normal dağılım cdf tablosu) kullanılarak yapılabilir.</p>

<p align="justify"><b>Soru:</b> Bir olasılık sınavında notların dağılımı, ortalaması 50 ve varyansı 25 olan bir normal dağılımla modellenmektedir.
Buna göre, bir öğrencinin<br><b>a)</b> 52'den daha düşük not alma olasılığı<br><b>b)</b> 49'dan daha düşük not alma olasılığı<br><b>c)</b> 48'den daha yüksek not alma olasılığı<br><b>d)</b> 53'ten daha yüksek not alma olasılığı<br>nedir?</p>

$$\displaystyle X \sim N(50, 25)$$

<p>Standartlaştırma işlemi uygulanır:</p>

$$\displaystyle P(X<52) = P \bigg (\frac{X-\mu}{\sigma} < \frac{52-50}{5} \bigg) = P(Z<0.4)$$

<p align="justify">Standart normal dağılım cdf tablosundan:</p>

$$P(Z<0.4) = \int_{-\infty}^{0.4}f_Z(z) = \Phi(0.4) \approx 0.6554$$

<p align="justify">sonucu elde edilir.</p>

<img src="image/exam_grades_distribution.png" alt="Sınav notları dağılımı" width=500>

<h3>Ders Önhazırlık</h3>

<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_01">Hafta 1: Permütasyon ve Koşullu/Toplam Olasılığa Giriş (Örneklem Uzay ve Alt Uzaylar Kavramları)</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_02">Hafta 2: Kombinasyon ve Koşullu/Toplam Olasılık (devam)</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_03">Hafta 3: Buluşma İhtimali (Matematiksel ve Nümerik Çözüm)</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_04">Hafta 4: Koşullu/Toplam Olasılık</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_05">Hafta 5: Histogramlara Giriş, Histogramda (Basit) Koşullu Olasılık</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_06">Hafta 6: Histogramlar (devam), Dağılımlar ve Rasgele Değişkenlere Giriş, Histogramda Koşullu Olasılık</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_07">Hafta 7: Üstel (Eksponansiyel) Dağılım Uydurma, Histogramlarda Koşullu/Toplam Olasılık</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/uniform">Tekdüze (Uniform) Dağılım</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/normal">Normal Dağılım</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/Bayes">Bayes</a></p>