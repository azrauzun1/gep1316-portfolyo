
from datetime import datetime  # Güncel tarihi kullanmak için datetime modülünü içe aktarır.

ad = input("Adınızı giriniz: ")  # Kullanıcıdan adını ister.
dogum_yili = int(input("Doğum yılınızı giriniz: "))  # Doğum yılını tam sayıya dönüştürür.
simdiki_yil = datetime.now().year  # İçinde bulunduğumuz yılı belirler.
if dogum_yili > simdiki_yil:
    print("Geçersiz doğum yılı girdiniz.")
else:
    yas = simdiki_yil - dogum_yili  # Kullanıcının yaklaşık yaşını hesaplar.

    print(f"Merhaba {ad}! Hoş geldiniz.")  # Kullanıcıya adıyla hitap eder.
    print(f"Bu yıl {yas} yaşına giriyorsunuz.")  # Hesaplanan yaşı gösterir.
