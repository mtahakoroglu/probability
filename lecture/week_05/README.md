<h3>Hafta 5</h3>
<h4>Histogramlar (devam), Dağılımlar ve Rasgele Değişkenlere Giriş, Histogramlarda Koşullu/Toplam Olasılık</h4>

<p align="justify"><b>Soru 9 (Histogram - Üstel Dağılım): </b>Trabzon otogarından Gümüşhane'ye her sabah 08:00'de otobüs kalkıyor. Bazı günler (yolcu sayısının az olması gibi) çeşitli nedenlerden dolayı otobüsün kalkışında gecikmeler olabiliyor. Haftada birkaç kez Trabzon'dan Gümüşhane'ye gitmesi gereken bir öğrenci otogara bir kamera sistemi kurarak otobüsün otogardan ayrılış vakitlerini otomatik olarak yüz gün boyunca kaydediyor. Bu sürenin sonunda topladığı veriyi çizdirince aşağıdaki grafiği elde ediyor.</p>

<ul>
<li>Öğrenci otobüsü en az %90 ihtimalle yakalamak isterse <b>en geç</b> saat kaçta otogarda olmalıdır?</li>
<li>Öğrenci otobüsü en az %30 ihtimalle yakalamak isterse <b>en geç</b> saat kaçta otogarda olmalıdır?</li>
<li>Grafikteki veriye göre öğrenci tam saat 8:06'da otogarda olursa hangi olasılıkla otobüse biner?</li>
<li>Grafikteki veriye göre öğrenci tam saat 8:03 ile 08:05 arası otogarda bulunursa hangi olasılıkla otobüse biner?</li>
<li>Histogramda görülen dağılım modellenebilir mi?</li>
<li>Grafikte verilen verileri normalize ederek histogramı tekrar çiziniz. Dağılımın formülünde integral operatörü kullanarak ne mânâya geldiğini anlamaya çalışınız.</li>
</li>
</ul>

<img src="../../image/trabzon_gumushane_bus.png" alt="Trabzon Gümüşhane sabah 8 otobüsü histogram" width=500 height=auto>

<p align="justify"><b>Cevap 9:</b></p>

<ul>
    <li>Öğrenci en geç 08:04'te otogarda olursa (en az) %90 ihtimalle otobüsü yakalar.</li>
    <li>Öğrenci en geç 08:01'te otogarda olursa en az %30 ihtimalle (gerçekte %55 ihtimal) otobüsü yakalar.</li>
    <li>Öğrenci en geç 08:06'da otogarda olursa %2 ihtimalle otobüsü yakalar.</li>
    <li>Öğrenci tam saat 8:03 ile 08:05 arası otogarda bulunursa %13 ihtimalle otobüse biner.</li>
    <li>Evet, üstel (eksponansiyel) dağılım ile modellenir. Formülüze edilmiş hâli aşağıdaki gibidir. Formüldeki X rasgele değişken (random variable) kavramını temsil etmektedir.</li>
</ul>

$$f_X(x) = e^{-\lambda x} \text{ for } x \geq 0$$

<p align="justify"><b>Soru 10 (Histogram - Normal Dağılım): </b>Bir öğrenci kaldığı yurttan üniversiteye sabahları 8:00'da dolmuşla gidiyor. Öğrenci bazı günler saat tam 8:00'de ve hatta bazen daha önce bile durakta olmasına rağmen dolmuşu kaçırıyor. Bunun üzerine öğrenci durağa bir kamera sistemi kurarak dolmuşun durağa geliş zamanlarını otomatik olarak 100 gün boyunca kaydediyor. Öğrenci 100 günün sonunda topladığı veriyi çizdirince aşağıdaki grafiği elde ediyor.</p>

<ul>
<li>Buna göre öğrenci dolmuşu en az %75 olasılıkla yakalamak isterse en geç saat kaçta durakta olmalıdır?</li>
<li>Grafikteki veriye göre öğrenci tam saat 8:02'de durakta olursa hangi olasılıkla dersine yetişir?</li>
<li>Histogramda görülen dağılım modellenebilir mi?</li>
<li>Grafikte görselleştirilen veriyi normalize ederek histogramı tekrar çiziniz.</li>
</ul>

<img src="../../image/student_waiting_at_bus_stop.png" alt="öğrenci ara durak'ta otobüs bekleme histogramı" width=500 height=auto>

<p align="justify"><b>Cevap 10: </b></p>

<ul>
<li>Öğrenci saat 08:00'de durakta olsa %21 ihtimalle dolmuşu kaçıracak. Dolayısıyla %79 ihtimalle dolmuşu yakalar. Eğer 08:01'de durağa giderse %42 ihtimalle kaçırıp %58 ihtimalle yakalayacak. En az %75 ihtimalle yakalamasından bahsedildiği için cevap <b>08:00</b> olur.</li>
<li>(22+15+1+2) / 100 = 40/100 = 0.4</li>
<li>Evet, normal (Gaussian) dağılım olarak formülüze edilebilir.</li>
</ul>

$$f_X(x) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x - \mu)^2}{2\sigma^2}}$$

<p align="justify"><b>Soru 11 (Histogramda Koşullu/Toplam Olasılık): </b>Geçen haftaki <a href="https://github.com/mtahakoroglu/probability/tree/main/lecture/week_04">Bursa-İstanbul seferleri histogram sorusu</a>nda otobüslerin otogardan ayrılma saatlerini kaydeden yolcu dikkatli gözlemi sonucunda önemli bir şey farkediyor: Sabah 06:00'dan 10:00'a kadar olan üç seferde otobüslerin otogardan ayrılış vakitleri öğlen 12:00'dan gece 24:00'a kadar olan diğer yedi sefere göre daha az gecikmeli. Bunun sebebini araştırdığında sabah kalkan üç otobüsün geri kalan seferlere göre yolcu
sayısının daha fazla olduğunu, 12:00'dan gece 24:00'e kadar olan seferlerde yolcu sayısı artar diye otobüslerin otogardan vaktinde ayrılmada pek de acele etmediğini gözlemliyor.</p>

<p align="justify">Yolcu bu iki farklı durumu farkettikten sonra yine yirmi gün sürecek şekilde yeni veri topluyor. Bu sefer bir önceki soruda olduğu gibi verileri tek bir dağılım olarak çizdirmek yerine iki farklı dağılım
olacak şekilde bunları çizdiriyor: İlk dağılım sabah seferlerine ait iken, ikinci dağılım öğlen 12:00'dan gece 24:00'a kadar olan seferlere ait. Bu bilgilere göre:</p>

<ul>
<li>Yolcu, sabah seferlerinin herhangi birinde otobüs terminalinde saat başını 3 geçe olursa kaç ihtimalle otobüsü yakalar?</li>
<li>Yolcu, öğlen ve gece seferlerinin herhangi birinde otobüs terminalinde saat başını 3 geçe olursa kaç ihtimalle otobüsü yakalar?</li>
<li>Yolcu, sabah-öğle-akşam ayırt edilmeden herhangi bir sefere saat başını 3 geçe otogarda olacak şekilde gelirse, kaç ihtimalle otobüsü yakalar?</li>
</ul>

|       |             |
| :---: |    :---:    |
| <img src="../../image/bursa_istanbul_bus_morning.png"> | <img src="../../image/bursa_istanbul_bus_afternoon_night.png"> |

<p align="justify"><b>Cevap 11: </b>Diğer koşullu olasılık ve toplam olasılık sorularında olduğu gibi Örneklem Uzayı (Sample Space) S (otobüsün sabah vakitlerinde ayrılması) ve S' (otobüsün öğlen-akşam vakitlerinde ayrılması) olarak iki olaya ayıralım. Ardından Y olayını da 08:03'te otogara gidildiğinde otobüsü yakalama olarak tanımlarsak aşağıdaki hesaplamaları yapabiliriz.</p>

<img src="../../image/question11.jpg" alt="histogram koşullu olasılık için örneklem uzayı" width=300 height=auto>


$$P(Y|S) = \frac{6}{60} = 0.1$$

$$P(Y|S') = \frac{38}{140} = 0.1$$

$$P(Y) = P(Y|S)P(S) + P(Y|S')P(S')$$

$$P(Y) = \frac{6}{60} \frac{60}{200} + \frac{38}{140} \frac{140}{200}$$

$$P(Y) = \frac{1}{10} \frac{3}{10} + \frac{19}{70} \frac{7}{10}$$

$$P(Y) = \frac{1}{10} \frac{3}{10} + \frac{19}{70} \frac{7}{10}$$

$$P(Y) = \frac{3}{100} + \frac{19}{100}$$

$$P(Y) = \frac{22}{100} = 0.22$$
