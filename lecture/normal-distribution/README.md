<h2>Normal Dağılım</h2>
<p align="justify">Normal dağılım olasılık yoğunluk fonksiyonu (probability distribution function - pdf) aşağıdaki formdadır.</p>

$$
f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}}
e^{\displaystyle \frac{(x-\mu)^2}{2\sigma^2}}
$$

<p align="justify">Normal dağılım pdf parametreleri olan ortalama (mean) $\mu$ ve standard sapma (standard deviation) $\sigma$ fonksiyonunu belirlemektedir. Anlamak için aşağıdaki şekili inceleyiniz.</p>

<img src="normal_distribution_pdf.png" alt="Normal dağılım olasılık yoğunluk fonksiyonu" width=500>

<p align="justify">Normal dağılımın modellediği bir olasılık sorusunda ihtimal hesabı yapmak gerçekten zor ve zahmetlidir. Hiç kimse bu pdf'in integralini alıp olasılık hesaplamak istemez. Bu noktada hem normal dağılımın standardize edilmesi hem de kümülatif dağılım fonksiyonu (cumulative distribution function - cdf) kullanımı işimizi kolaylaştıracak.</p>

<h4>Standard Normal Dağılım</h4>

<p align="justify">Yukarıda $X$ rasgele değişkeninin $mu$ ve $sigma$ parametrelerine sahip bir normal dağılımla modellendiğini belirtelim.</p>

$$\displaystyle X\sim N(\mu ,\sigma ^{2})$$

<p align="justify">Burada $X$ değişkeninden ortalamayı çıkarıp standart sapmaya bölerek standartlaştırmayı gerçekleştirelim.</p>

$$\displaystyle \frac{X-\mu}{\sigma} = Z \sim N(0, 1)$$

<p align="justify">Karşılaştığımız sorularda bu standart hâle dönüştürüp normal dağılım <b>cdf</b> tablosundaki değerleri kullanarak soruyu çözeceğiz.</p>