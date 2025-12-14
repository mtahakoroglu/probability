<h2>EEM 217 Olasılık Kuramı</h2>

<h3>Normal Dağılım</h3>
<p align="justify">Normal dağılım olasılık yoğunluk fonksiyonu (probability distribution function - pdf) aşağıdaki formdadır.</p>

$$
f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}}
e^{\displaystyle \frac{(x-\mu)^2}{2\sigma^2}}
$$

<p align="justify">Normal dağılım pdf parametreleri olan ortalama (mean) $\mu$ ve standard sapma (standard deviation) $\sigma$ fonksiyonunu belirlemektedir. Anlamak için aşağıdaki şekili inceleyiniz.</p>

<img src="image/normal_distribution_pdf.png" alt="Normal dağılım olasılık yoğunluk fonksiyonu" width=500>

<p align="justify">Normal dağılımın modellediği bir olasılık sorusunda ihtimal hesabı yapmak gerçekten zor ve zahmetlidir. Hiç kimse bu pdf'in integralini alıp olasılık hesaplamak istemez. Bu noktada hem normal dağılımın standardize edilmesi hem de kümülatif dağılım fonksiyonu (cumulative distribution function - cdf) kullanımı işimizi kolaylaştıracak.</p>

<h4>Standard Normal Dağılım</h4>

<p align="justify">Yukarıda $X$ rasgele değişkeninin $mu$ ve $sigma$ parametrelerine sahip bir normal dağılımla modellendiğini belirtelim.</p>

$$\displaystyle X\sim N(\mu ,\sigma ^{2})$$

<p align="justify">Burada $X$ değişkeninden ortalamayı çıkarıp standart sapmaya bölerek standartlaştırmayı gerçekleştirelim.</p>

$$\displaystyle \frac{X-\mu}{\sigma} = Z \sim N(0, 1)$$

<p align="justify">Karşılaştığımız sorularda bu standart hâle dönüştürüp normal dağılım <b>cdf</b> tablosundaki değerleri kullanarak soruyu çözeceğiz.</p>

<h3>Ders Önhazırlık</h3>

<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_01">Hafta 1: Permütasyon ve Koşullu/Toplam Olasılığa Giriş (Örneklem Uzay ve Alt Uzaylar Kavramları)</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_02">Hafta 2: Kombinasyon ve Koşullu/Toplam Olasılık (devam)</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_03">Hafta 3: Buluşma İhtimali (Matematiksel ve Nümerik Çözüm)</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_04">Hafta 4: Koşullu/Toplam Olasılık</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_05">Hafta 5: Histogramlara Giriş, Histogramda (Basit) Koşullu Olasılık</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_06">Hafta 6: Histogramlar (devam), Dağılımlar ve Rasgele Değişkenlere Giriş, Histogramda Koşullu Olasılık</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_07">Hafta 7: Üstel (Eksponansiyel) Dağılım Uydurma, Histogramlarda Koşullu/Toplam Olasılık</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_09_10">Hafta 9-10: Normal (Gaussian) Dağılım Parametreleri ve Tekdüze (Uniform) Dağılım</a></p>
<p align="justify"><a href="C:\Users\mtaha\Dropbox\GitHub\probability\lecture\week_10_11">Hafta 11-12: BAYES</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_13">Hafta 13: BAYES - devam</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_14">Hafta 14: Rasgele Sayı Üreteci ile Simülasyon</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_15">Hafta 15: Öğrenci Yaş Histogram - Python Kodu</a></p>
<p align="justify"><a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/normal-dsitribution">Normal Dağılım</a></p>
