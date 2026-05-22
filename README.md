# 🎥 TuringLab Proje Demo Videosu

Hocam, proje tanıtımı ve canlı simülasyon adımlarını içeren videosuna aşağıdaki bağlantıdan ulaşabilirsiniz:

👉 **[TuringLab Proje Demo Videosu (YouTube)]([https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID](https://youtu.be/a0M8MwlHv1E?si=v-kuaO772hGURANr))**
# turinglab_muhammet_sehhamza
# TURINGLAB TASARIM NOTLARI (BÖLÜM 2)

## TM-1: Unary → Binary Çevirici
1. **Strateji:** Şeridin en solundaki '1' karakteri sırayla silinerek 'X' yapılır. Her silme işleminde şeridin en sağına gidilerek bir Binary Increment (ikili artırma) algoritması tetiklenir. Tüm '1'ler bittiğinde yardımcı semboller temizlenir.
2. **Durum Sayısı:** 7 durum kullanılmıştır. İşaretleme, sağa ilerleme, artırma, sola dönme ve temizlik aşamaları için bu sayı optimize edilmiştir.
3. **Şerit Alfabesi:** {1, 0, B, X, #}. '#' işareti unary kısım ile binary kısmın birbirine karışmasını önlemek için sınır çizgisi olarak seçilmiştir.
4. **Karmaşıklık:** $O(n^2)$. Her bir '1' için tüm şerit boyunca sağa ve sola tarama yapıldığından karesel zaman alır.
5. **Hata Ayıklama Hikayesi:** İlk tasarımda binary increment yaparken en sağdaki boşluğa ulaştığımda kafayı sola kaydırırken sınır sembolünü taşırıyordum. Araya '#' koyarak bu bug'ı çözdüm.

## TM-2: İki İkili Sayıyı Karşılaştıran TM
1. **Strateji:** İlk sayının en solundaki karakter okunup 'X' veya 'Y' olarak işaretlenir. Karakterin 0 veya 1 olmasına göre durum değiştirilerek ikinci sayının hizasındaki karakter aranır ve karşılaştırılır.
2. **Durum Sayısı:** 7 durum kullanılmıştır. Hafızada 0 veya 1 tutulmasını sağlayan dallanmalar mevcuttur.
3. **Şerit Alfabesi:** {0, 1, #, X, Y, B}. İlk sayıdaki elemanlar ile ikinci sayıdaki işlenmiş elemanları ayırt etmek için X ve Y sembolleri seçilmiştir.
4. **Karmaşıklık:** $O(n^2)$. İki sayı arasında kafa sürekli mekik dokuduğu için zaman karmaşıklığı kareseldir.
5. **Hata Ayıklama Hikayesi:** Karşılaştırma yaparken sayıların uzunluklarının eşit olmadığı durumlarda (örn. sol taraf erken bittiğinde) doğrudan kabul durumuna geçiyordu. Durum kontrollerini sıkılaştırarak bu açığı kapattım.

## TM-3: Dizgi Kopyalayıcı
1. **Strateji:** Şeridin başındaki karakter 'A' veya 'B'' olarak işaretlenir. Sağa doğru ilerlenerek '#' sınırından sonraki ilk boşluğa aynı karakter yazılır ve sola dönülür.
2. **Durum Sayısı:** 8 durum kullanılmıştır. Karakteri akılda tutma ve dönüş yolları için ideal sayıdır.
3. **Şerit Alfabesi:** {a, b, B, #, A, B'}. Büyük harfler orijinal dizgide nerede kaldığımızı unutmamak için işaretçi görevi görür.
4. **Karmaşıklık:** $O(n^2)$. Her karakterin kopyalanması için dizginin boyu kadar sağa ve sola hareket edilir.
5. **Hata Ayıklama Hikayesi:** Döngü bittiğinde şerit üzerinde kopyalanan karakterlerin yerine büyük harfler (A ve B') kalıyordu. En son bir temizlik durumu (`q_clean`) ekleyerek bunları tekrar küçük harfe çeviren mantığı kurdum.

## TM-4: Basit Parantez Denge Kontrolü
1. **Strateji:** Şerit boyunca sağa gidilerek karşılaşılan ilk kapanış parantezi ')' bulunur ve 'X' yapılır. Hemen solundaki ilk işlenmemiş açılış parantezi '(' aranır, o da 'X' yapılır. Dönüş döngüsüyle işlem tekrarlanır.
2. **Durum Sayısı:** 7 durum kullanılmıştır. Arama, eşleştirme ve temizlik kontrolü durumları mevcuttur.
3. **Şerit Alfabesi:** {(, ), X, B}. 'X' karakteri başarıyla eşleşip birbirini yok eden parantezleri şeritten silmek için kullanılmıştır.
4. **Karmaşıklık:** $O(n^2)$. Dengeli bir yapıda her parantez çifti için sola doğru lokal aramalar yapıldığından karesel karmaşıklık oluşur.
5. **Hata Ayıklama Hikayesi:** Girdi doğrudan ')' ile başladığında sistemin hata vermeyip sonsuz döngüye girmesi sorunuyla karşılaştım. Başlangıç durumuna `)` okuma kuralı ekleyerek direkt ret (`q_reject`) durumuna dallanmasını sağladım.
