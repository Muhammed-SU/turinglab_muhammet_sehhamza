# TURINGLAB PROJE RAPORU 

## 1. Giriş
[cite_start]TuringLab, Deterministic Single-Tape Turing makinelerini simüle etmek, test etmek ve çalıştırmak amacıyla Python 3.10+ mimarisiyle sıfırdan geliştirilmiş bir yazılım motorudur[cite: 63, 88, 94]. [cite_start]Proje kapsamında, biçimsel matematiksel modeller kod dünyasına aktarılmış ve 4 farklı hesaplama problemi bu motor üzerinde çözülmüştür[cite: 17, 24].

## 2. Sistem Mimarisi ve Tasarım Kararları
[cite_start]Proje, modüler ve genişletilebilir bir yapıda tasarlanmıştır[cite: 44, 142]. [cite_start]`tm_engine.py` içinde iki ana sınıf yer almaktadır: `Tape` ve `SingleTapeTM`[cite: 95].
* [cite_start]**Şerit (Tape) Temsili:** Python'da string yapısı değiştirilemez (immutable) olduğundan, performans kaybını ve olası hataları önlemek adına şerit bir `list[str]` (karakter listesi) olarak modellenmiştir. [cite_start]Kafa sağa doğru taşarsa liste dinamik olarak genişletilir; sola doğru taşarsa (`head_position < 0`) kafanın indeks 0'da sabit kalması kararlaştırılmıştır[cite: 118, 151].
* [cite_start]**Geçiş Fonksiyonu:** YAML dosyasından okunan kurallar, arama maliyetini $O(1)$ seviyesine indirmek için Python sözlük (`dict`) yapısına dönüştürülmüştür[cite: 99].

## 3. Tasarlanan Turing Makineleri
[cite_start]Proje kapsamında aşağıdaki 4 makine başarıyla simüle edilmiştir[cite: 17, 207]:
1. [cite_start]`unary_to_binary.yaml`: Unary girdiyi binary sayıya dönüştürür[cite: 179, 207].
2. [cite_start]`binary_compare.yaml`: İki binary sayıyı karşılaştırır ($Sayı1 > Sayı2$)[cite: 183, 207].
3. [cite_start]`string_copy.yaml`: Verilen dizgiyi araya '#' koyarak kopyalar[cite: 187, 207].
4. [cite_start]`student_choice.yaml`: Basit parantez denge kontrolünü gerçekleştirir[cite: 191, 195, 207].

[cite_start]Karşılaştırma (TM-2) ve kopyalama (TM-3) gibi işlemler tek şerit üzerinde çok fazla ileri-geri kafa hareketi gerektirdiğinden, zaman karmaşıklıkları karesel ($O(n^2)$) düzeydedir[cite: 198]. [cite_start]Bu durum, çok şeritli (Multi-tape) makinelerin önemini kavramsal olarak kanıtlamaktadır[cite: 198].

## 4. Kavramsal Tartışma: Halting Problemi
*Seçilen Soru: (a) Halting problemini TuringLab içinde "çözmek" mümkün mü? Neden değil? [cite: 290, 291]*

Halting problemi, genel bir Turing makinesinin girdi olarak verilen başka bir Turing makinesinin çalışmasını sonsuza kadar sürdürüp sürdürmeyeceğini (durup durmayacağını) tahmin eden kesin bir algoritmanın yazılamayacağını kanıtlar. [cite_start]TuringLab bir Turing makinesi simülatörüdür[cite: 12, 94]. [cite_start]TuringLab içinde bir `will_halt(tm, input)` fonksiyonu yazmaya çalışırsak, simülatörün kendisi de evrensel bir Turing makinesi (UTM) gibi davranacaktır[cite: 292]. [cite_start]Ancak, eğer girdi olarak verilen makine sonsuz döngüye giriyorsa, TuringLab'deki simülasyon döngüsü de (eğer `max_steps` sınırı konulmazsa) sonsuza kadar çalışacak ve asla bir karar üretemeyecektir[cite: 111, 334]. Matematiksel olarak hiçbir Turing makinesi kendi üst kümesindeki veya kendi seviyesindeki tüm makinelerin durma problemini çözemez; dolayısıyla TuringLab içinde Halting problemini "çözmek" imkansızdır.

## 5. Sınırlar ve İleri Çalışma
[cite_start]Mevcut sistem deterministik ve tek şeritli yapıyla sınırlıdır[cite: 88, 94]. [cite_start]Gelecekte sistem, hesaplama adımlarını ve kafa hareketlerini grafiksel olarak PNG/GIF formatında dışarı aktaran bir görselleştirici modülü (`visualizer.py`) ve BFS algoritması kullanan bir Non-Deterministic (NTM) motoru ile geliştirilebilir[cite: 43, 333, 343].

## 6. Kaynakça
* Sipser, M. (2012). *Introduction to the Theory of Computation*.
* [cite_start]Selçuk Üniversitesi Bilgisayar Mühendisliği Hesaplama Kuramı TuringLab Öğrenci El Kitabı[cite: 6, 8].
