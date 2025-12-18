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

<p align="justify">Bu iki parametre, normal dağılımın hem konumunu hem de yayılımını tamamen belirler. Aşağıdaki şekilde, farklı parametre değerleri için normal dağılımın görünümü <a href="https://github.com/mtahakoroglu/probability/blob/main/lecture/normal/normal-distribution-pdf.py">çizdirilmiştir</a>.<br>📌 Not: Normal dağılım sürekli bir dağılımdır ve olasılıklar, pdf'in belirli aralıklardaki integrali ile hesaplanır.</p>

<img src="normal_distribution_pdf.png" alt="Normal dağılım olasılık yoğunluk fonksiyonu" width=500>

---
<p align="justify"><b>Soru: </b>Aşağıda bir dağılıma ait normalize edilmiş dört histogram verilmiştir. <i>(a)</i> Bu dağılımın ismi nedir? <i>(b)</i> Bu dağılımın parametreleri nelerdir? İsimlerini ve sembollerini yazıp ne manaya geldiklerini açıklayınız. <i>(c)</i> {a, b, c, d, e, f, g, h} değerlerini {0, 0, 0, 0.2, 0.5, 1, 5, -2} değerleriyle eşleyiniz. <i>(d)</i> Sözüne güvenilir ve güvenilmez iki insan var. <i>(i)</i>, <i>(ii)</i>, <i>(iii)</i> ve <i>(iv)</i>'te gösterilen dağılımlarından hangi ikisi bu insanları modelleyemeye uygundur?</p>

<img src="normal_distribution_parameters.png" alt="normal dağılım parametreleri" width=%100 height=auto>

<p align="justify"></b><i>(a)</i> Bu dağılımın ismi Normal (Gaussian) dağılımdır. Dağılıma ait pdf aşağıdaki gibidir.</p>

$$f_X(x) = \displaystyle \frac{1}{\sqrt{2\pi\sigma^2}} \displaystyle e^{\displaystyle -\frac{(x - \mu)^2}{2\sigma^2}}$$

<p align="justify"><i>(b)</i> Normal dağılımın yatay eksende hareket edebilen merkezine ortalama (mean) denilmekte ve $\mu$ sembolüyle gösterilmektedir. Dağılıma ait ikinci parametre standart sapma (standard deviation) denilen ve $\sigma$ sembolüyle gösterilen parametredir. Bu parametrenin ifade ettiği manaya öbür şıklarda değinilecektir.</p>

<p align="justify"><i>(c)</i> Parametrelerin değerleri aşağıdaki gibidir.<br>a=c=e=0<br>g=-2<br>b=0.2<br>h=0.5<br>d=1<br>f=5</p>

<p align="justify"><i>(d)</i> Sözüne güvenilen kişi <i>(i)</i> ile modellenebilir. Güvenilmez olan ise <i>(iii)</i> ile modellenmeye daha uygundur.</p>

---

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
Buna göre, bir öğrencinin<br>
<b>a)</b> 52'den daha düşük not almış olma olasılığı nedir?<br>
<b>b)</b> 49'dan daha düşük not almış olma olasılığı nedir?<br>
<b>c)</b> 48'den daha yüksek not almış olma olasılığı nedir?<br>
<b>d)</b> 53'ten daha yüksek not almış olma olasılığı nedir?<br>
<b>e)</b> 45 ile 55 arasında not almış olma olasılığı nedir?</p>

<p><b>Çözüm:</b></p>

$$\displaystyle X \sim N(50, 5^2)$$

<p><b>a)</b> İlk önce standartlaştırma işlemi uygulanır:</p>

$$\displaystyle P(X<52) = P \bigg (\frac{X-\mu}{\sigma} < \frac{52-50}{5} \bigg) = P(Z<0.4)$$

<p>Eğer Normal dağılıma ait pdf kolayca integrallenebilir olsaydı</p>

$$P(Z<0.4) = \int_{-\infty}^{0.4}f_Z(z)$$

<p>şeklinde çözümü elde edebilirdik. Öyle olmadığından <a href="https://github.com/mtahakoroglu/probability/blob/main/lecture/normal/standard-normal-cdf-table.pdf">standart normal dağılım cdf tablosundan</a> faydalanarak çözümü hesaplarız.</p>

$$P(Z<0.4) = \Phi(0.4) \approx 0.6554$$

<p align="justify">Aşağıda sorunun <a href="https://github.com/mtahakoroglu/probability/blob/main/lecture/normal/exam-grades.py">Monte Carlo simülasyonu ile elde edilen çözümü</a> de ayrıca verilmiştir.</p>

<img src="exam_grades_distribution.png" alt="Sınav notları dağılımı" width=500>

<p><b>b)</b> İlk önce standartlaştırma işlemi uygulanır:</p>

$$\displaystyle P(X<49) = P \bigg (\frac{X-\mu}{\sigma} < \frac{49-50}{5} \bigg) = P(Z<-0.2)$$

<p>Eğer Normal dağılıma ait pdf kolayca integrallenebilir olsaydı</p>

$$P(Z<-0.2) = \int_{-\infty}^{-0.2}f_Z(z)$$

<p>şeklinde çözümü elde edebilirdik. Öyle olmadığından <a href="https://github.com/mtahakoroglu/probability/blob/main/lecture/normal/standard-normal-cdf-table.pdf">standart normal dağılım cdf tablosundan</a> faydalanarak çözümü hesaplarız.</p>

$$P(Z<-0.2) = \Phi(-0.2) \approx 0.4207$$

<p><b>c)</b> İlk önce standartlaştırma işlemi uygulanır:</p>

$$\displaystyle P(X>48) = P \bigg (\frac{X-\mu}{\sigma} > \frac{48-50}{5} \bigg) = P(Z<-0.4)$$

<p>Eğer Normal dağılıma ait pdf kolayca integrallenebilir olsaydı</p>

$$P(Z>-0.4) = \int_{-0.4}^{\infty}f_Z(z)$$

<p>şeklinde çözümü elde edebilirdik. Öyle olmadığından <a href="https://github.com/mtahakoroglu/probability/blob/main/lecture/normal/standard-normal-cdf-table.pdf">standart normal dağılım cdf tablosundan</a> faydalanarak çözümü hesaplarız.</p>

$$P(Z>-0.4) = 1-\Phi(-0.4) = 1-0.3446 = 0.6554$$

<p>Burada <a href="https://github.com/mtahakoroglu/probability/blob/main/lecture/normal/standard-normal-cdf-table.pdf">standart normal dağılım cdf tablosunun</a> simetrisinden faydalanarak çözümü aşağıdaki gibi de hesaplayabilirdik.</p>

$$P(Z>-0.4) = \Phi(0.4) = 0.6554$$

<p><b>d)</b> İlk önce standartlaştırma işlemi uygulanır:</p>

$$\displaystyle P(X>53) = P \bigg (\frac{X-\mu}{\sigma} > \frac{53-50}{5} \bigg) = P(Z>0.6)$$

<p>Eğer Normal dağılıma ait pdf kolayca integrallenebilir olsaydı</p>

$$P(Z>0.6) = \int_{0.6}^{\infty}f_Z(z)$$

<p>şeklinde çözümü elde edebilirdik. Öyle olmadığından <a href="https://github.com/mtahakoroglu/probability/blob/main/lecture/normal/standard-normal-cdf-table.pdf">standart normal dağılım cdf tablosundan</a> faydalanarak çözümü hesaplarız.</p>

$$P(Z>0.6) = 1-\Phi(0.6) = 1-0.7257 = 0.2743$$

<p>Burada <a href="https://github.com/mtahakoroglu/probability/blob/main/lecture/normal/standard-normal-cdf-table.pdf">standart normal dağılım cdf tablosunun</a> simetrisinden faydalanarak çözümü aşağıdaki gibi de hesaplayabilirdik.</p>

$$P(Z \gt 0.6) = \Phi(-0.6) = 0.2743$$

<p><b>e)</b> İlk önce standartlaştırma işlemi uygulanır:</p>

$$P(45 \lt X \lt 55) = P \bigg ( \frac{45-50}{5} \lt \frac{X-\mu}{\sigma} \lt \frac{55-50}{5} \bigg) = P(-1 \lt Z \lt 1)$$

<p>Eğer Normal dağılıma ait pdf kolayca integrallenebilir olsaydı</p>

$$P(-1 \lt Z \lt 1) = \int_{-1}^{1}f_Z(z)$$

<p>şeklinde çözümü elde edebilirdik. Öyle olmadığından <a href="https://github.com/mtahakoroglu/probability/blob/main/lecture/normal/standard-normal-cdf-table.pdf">standart normal dağılım cdf tablosundan</a> faydalanarak çözümü hesaplarız.</p>

$$P(-1 \lt Z \lt 1) = \Phi(1)-\Phi(-1) = 0.8413 - 0.1587 = 0.6826$$

<p>Soruda karşımıza çıkan</p>

$$45 \lt Z \lt 55$$

<p>aralığı ortalama değer olan $\mu=50$'yi merkeze alacak bakacak olursak $\pm \sigma$ aralığına tekabül ettiğinden ilgili olasılık değerini %68 olarak hesapladık. Aşağıdaki grafik bunu teyit etmektedir</p>

<img src="68-95-99-rule.png" alt="68-95-99 rule" width=600>