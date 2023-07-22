Python dilinde yazılan bu tkinter tabanlı program, kullanıcıların üniversiteler ve bölümler hakkında bilgi kaydetmelerine, sıralama ve not eklemelerine olanak sağlar. Programın belirli bir veri tabanı veya API'a bağlı olmaması sebebiyle, girilen bilgiler kullanıcıdan alınmaktadır.

Bu program, 3 ana sayfadan oluşmaktadır:

Okullar: Bu sayfada, kullanıcılar üniversite, şehir, bölüm, sıralama, eski sıralama ve notları girerek bir üniversiteyi listeye ekleyebilirler. Aynı zamanda, mevcut bir üniversiteyi listeden silebilirler.
İstek Listesi: Bu sayfada, kullanıcılar bir üniversiteyi istek listesine ekleyebilir veya listeden çıkarabilirler.
Tanıtım Günleri: Bu sayfada, kullanıcılar üniversite tanıtım günlerini kaydedebilirler. Bu bilgiler şehir, üniversite, tarih ve notları içerir.
Programın ana işlevleri aşağıdaki gibidir:

add_to_list: Bu fonksiyon, kullanıcının girdiği bilgileri alır ve verilere ekler.
add_to_wishlist: Bu fonksiyon, kullanıcının seçtiği bir üniversiteyi istek listesine ekler.
delete: Bu fonksiyon, kullanıcının seçtiği bir üniversiteyi veri listesinden siler.
delete_wishlist: Bu fonksiyon, kullanıcının seçtiği bir üniversiteyi istek listesinden siler.
load_listbox: Bu fonksiyon, listeleri yükler ve sıralar.
save_data, save_wishlist ve save_presentation_days: Bu fonksiyonlar, verileri, istek listesini ve tanıtım günlerini bir json dosyasına kaydeder.
load: Bu fonksiyon, verileri, istek listesini ve tanıtım günlerini bir json dosyasından yükler. Dosya bulunamazsa, boş listeler oluşturur.
on_double_click: Bu fonksiyon, kullanıcının bir öğeyi çift tıkladığında çağrılır. Seçili üniversitenin bilgilerini giriş alanlarına yükler.
edit_score: Bu fonksiyon, kullanıcının bir üniversitenin eski sıralamasını düzenlemesini sağlar.
add_to_presentation_days: Bu fonksiyon, kullanıcının girdiği bilgileri alır ve tanıtım günleri listesine ekler.
Bu program, kullanıcıların üniversite ve bölüm tercihlerini düzenlemek ve izlemek için basit bir arayüz sağlar. Kullanıcılar, üniversite ve bölümleri listeleyebilir, istek listesine ekleyebilir, tanıtım günlerini takip edebilir ve buna göre plan yapabilirler.
