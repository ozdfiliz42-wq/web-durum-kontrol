# 🌐 Web Sitesi Durum Kontrol Aracı (HTTP Status Analyzer)

## 1. Proje Hakkında
Bu araç; siber güvenlik ve sistem yönetimi süreçlerinde hedef web sitelerinin erişilebilir olup olmadığını, sunucu düzeyinde herhangi bir kısıtlama (Firewall/WAF engeli vb.) veya çökme yaşanıp yaşanmadığını **HTTP Durum (Status) Kodları** üzerinden anlık olarak analiz eden hafif düzey bir betiktir. Ostim Teknik Üniversitesi Bilgi Güvenliği Teknolojisi ders projesi kapsamında geliştirilmiştir.

## 2. Teknik Özellikler ve Çalışma Mantığı
* **Saf Python Mimarisi:** Projede harici hiçbir üçüncü parti kütüphane kullanılmamış; tamamen Python'ın yerleşik `urllib`, `ssl` ve `datetime` modülleriyle optimize edilmiştir.
* **SSL Muafiyet Katmanı:** Güvenli bağlantılarda (HTTPS) işletim sistemi düzeyinde yaşanabilecek sertifika doğrulama (SSL Verify) tıkanıklıklarını aşmak için özel güvenlik bağlamı (`ssl._create_unverified_context`) entegre edilmiştir.
* **Akıllı HTTP Hata Yönetimi:** Sunucudan dönen `200 OK`, `403 Forbidden` (Erişim Engeli) veya `404 Not Found` (Sayfa Bulunamadı) gibi adli bilişim kodlarını ayrıştırarak kullanıcıya Türkçe anlamlandırılmış rapor sunar.

## 3. Örnek Sistem Çıktısı (Canlı Analiz Raporu)
```text
🌐 WEB SİTESİ DURUM KONTROL PANELİ v1.0 🌐
Lütfen kontrol etmek istediğiniz web sitesini yazın (Örn: google.com): google.com

============================================================
📡 [https://google.com](https://google.com) Adresi Analiz Ediliyor...
⏰ Analiz Zamanı: 2026-06-12 01:56:55
============================================================
🟢 [DURUM]: AKTİF / ERİŞİLEBİLİR
📊 [HTTP STATUS KODU]: 200 (OK)
📝 [AÇIKLAMA]: Site istekleri başarıyla karşılıyor, her şey yolunda.
============================================================
