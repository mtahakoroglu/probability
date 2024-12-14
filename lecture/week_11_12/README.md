<h3>Hafta 11-12: BAYES</h3>

<p align="justify"><b>Soru 14 (Koşullu ve Toplam Olasılık):</b> Gümüşhane Üniversitesi EEM öğrencileri haftasonu pikniğe gitmeyi planlıyorlar. Havanın yağmurlu olma ihtimali %40'tır. Hava açık olursa %90 ihtimalle pikniğe gidilecek ancak hava yağmurlu olursa pikniğe gitme ihtimali %20'ye düşüyor. Öğrencilerin pikniğe gitme ihtimalini koşullu olasılık ve toplam olasılık kullanarak bulunuz. <b>Not: </b>Bayes sorularında kullanacağımız formüldeki kesirli ifadede pay kısmı koşullu olasılı, payda kısmı toplam olasılık olacağından dolayı burada bir kez daha koşullu ve toplam olasılık formüllerini/ifadelerini tekrar etmek istedik.</p>

<p align="justify"><b>Çözüm 14:</b> Bu soruyu aşağıdaki Bayes sorusuna hazırlık olsun diye buraya koyduk. Koşullu ve toplam olasılık Bayes formulünün de bir parçası. Pikniğe gitme olayına sembolik olarak P, havanın yağmurlu olma olayına Y dersek, çözüm aşağıdaki gibi bulunur.</p>

$$P(P) = P(P|Y)P(Y) + P(P|Y')P(Y')$$

$$P(P) = \frac{20}{100}\frac{40}{100} + \frac{90}{100}\frac{60}{100}$$

$$P(P) = \frac{62}{100} = 0.62$$

<p align="justify"><b>Soru 15 (Bayes):</b> Bir lisedeki öğrencilerin %40'ı kızdır. Kızların %80'i erkeklerin ise %50'si basketbol kulübüne üyedir. 
<ul>(a) Basketbol kulübünden rasgele bir şekilde bir temsilci seçilecektir. Bu temsilcinin kız olma olasılığını bulunuz.</ul>
<ul>(b) Liseden rasgele bir şekilde bir temsilci seçilecektir. Bu temsilcinin basketbol kulübünden olma olasılığını bulunuz.</ul>
</p>

<p align="justify"><b>Çözüm 15:</b> Soruda bize söylenen verileri matematiğe dökelim.</p>

$$P(K) = \frac{40}{100}$$

$$P(K') = \frac{60}{100}$$

$$P(B|K) = \frac{80}{100}$$

$$P(B|K') = \frac{50}{100}$$

<p align="justify"><b>(a)</b> Bizden P(K|B) isteniyor. Bu bugüne kadar koşullu ve toplam olasılık sorularında gördüğümüz formattan farklı. İfade tersine dönmüş. Burada Bayes formulü gerekiyor. Bayes formulü aşağıdaki gibi yazılır.</p>

$$P(K|B) = \frac{P(B|K)P(K)}{P(B)}$$

$$P(K|B) = \frac{P(B|K)P(K)}{P(B|K)P(K) + P(B|K')P(K')}$$

<p align="justify">Paydada yer alan P(B) ifadesini toplam olasılıkla (b) şıkkında buluyoruz. İfadeleri yerlerine koyalım.</p>

$$P(K|B) = \frac{\frac{80}{100}\frac{40}{100}}{\frac{62}{100}}$$

$$P(K|B) = \frac{\frac{32}{100}}{\frac{62}{100}} = \frac{32}{62} = \frac{16}{31} \approx 0.52$$

<p align="adjust"><b>Not:</b> Bayes soruları sayı vererek kolayca çözülebilir.</p>

<p align="justify"><b>(a)</b> Bizden P(B) isteniyor. Toplam olasılık formulü ile çözebiliriz.</p>

$$P(B) = P(B|K)P(K) + P(B|K')P(K')$$

$$P(B) = \frac{80}{100}\frac{40}{100} + \frac{50}{100}\frac{60}{100}$$

$$P(B) = \frac{32+30}{100} = \frac{62}{100} = 0.62$$
