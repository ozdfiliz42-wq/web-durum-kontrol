import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request
import urllib.error
from datetime import datetime

def web_sitesi_durum_kontrol(url):
    # Kullanıcı HTTP yazmadıysa otomatik olarak ekleyelim ki hata vermesin
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url

    print("\n" + "="*60)
    print(f"📡 {url} Adresi Analiz Ediliyor...")
    print(f"⏰ Analiz Zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*60)

    try:
        # Web sitesine resmi bir tarayıcı gibi istek gönderiyoruz (User-Agent)
        istek = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        )
        
        # Siteye bağlanıp HTTP durum kodunu okuyoruz
        with urllib.request.urlopen(istek, timeout=10) as response:
            status_kodu = response.getcode()
            
            if status_kodu == 200:
                print(f"🟢 [DURUM]: AKTİF / ERİŞİLEBİLİR")
                print(f"📊 [HTTP STATUS KODU]: {status_kodu} (OK)")
                print(f"📝 [AÇIKLAMA]: Site istekleri başarıyla karşılıyor, her şey yolunda.")
            else:
                print(f"🟡 [DURUM]: ERİŞİM DETAYI VAR")
                print(f"📊 [HTTP STATUS KODU]: {status_kodu}")

    except urllib.error.HTTPError as e:
        # Sunucu ayakta ama hata kodu döndürdüyse (Örn: 404 Not Found, 403 Forbidden)
        print(f"🔴 [DURUM]: ERİŞİM HATASI / KISITLAMA")
        print(f"📊 [HTTP STATUS KODU]: {e.code}")
        if e.code == 403:
            print("📝 [AÇIKLAMA]: 403 Forbidden - Sunucu erişimi yasakladı veya kısıtladı.")
        elif e.code == 404:
            print("📝 [AÇIKLAMA]: 404 Not Found - İstenen sayfa sunucuda bulunamadı.")
        else:
            print(f"📝 [AÇIKLAMA]: Sunucu {e.code} hata kodu döndürdü.")

    except urllib.error.URLError as e:
        # Site tamamen kapalıysa veya internet yoksa, domain bulunamadıysa
        print(f"❌ [DURUM]: SİTEYE ULAŞILAMIYOR / SUNUCU ÇEVRİMDIŞI")
        print(f"⚠️  [HATA DETAYI]: Domain adresi geçersiz veya site tamamen çökmüş olabilir.")
        print(f"🔍 [TEKNİK NEDEN]: {e.reason}")

    except Exception as e:
        print(f"🚨 [HATA]: Beklenmeyen bir bağlantı problemi oluştu: {e}")

    print("="*60 + "\n")

if __name__ == "__main__":
    print("🌐 WEB SİTESİ DURUM KONTROL PANELİ v1.0 🌐")
    hedef_site = input("Lütfen kontrol etmek istediğiniz web sitesini yazın (Örn: google.com): ")
    web_sitesi_durum_kontrol(hedef_site)    