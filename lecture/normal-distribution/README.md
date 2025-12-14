<h2>Normal Dağılım</h2>
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

<img src="normal_distribution_pdf.png" alt="Normal dağılım olasılık yoğunluk fonksiyonu" width=500>

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

<p align="justify"><b>Soru 1:</b> Bir olasılık sınavında notların dağılımı, ortalaması 50 ve varyansı 25 olan bir normal dağılımla modellenmektedir.
Buna göre, bir öğrencinin 52’den daha düşük not alma olasılığı nedir?</p>

$$\displaystyle X \sim N(50, 25)$$

<p>Standartlaştırma işlemi uygulanır:</p>

$$\displaystyle P(X<52) = P \bigg (\frac{X-\mu}{\sigma} < \frac{52-50}{5} \bigg) = P(Z<0.4)$$

<p align="justify">Standart normal dağılım cdf tablosundan:</p>

$P(Z<0.4) = F_Z(0.4) = \Phi(0.4) \approx 0.6554$

<p align="justify">sonucu elde edilir.</p>

<img src="exam_grades_distribution.png" alt="Sınav notları dağılımı" width=500>