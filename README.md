# root-web-tool
# Güvenli Web Zafiyeti Tarayıcı (Linux İçin)

Bu araç **Emin Sarsılmaz** tarafından yapılmıştır ve **Root Hack Team** ile **Sarsılmaz Hack Team** adı altında geliştirilmiştir. Belirtilen URL'yi güvenlik açıkları açısından tarayarak SQL Injection, Komut Enjeksiyonu, Açık Dizin ve Dosya Dahil Etme gibi güvenlik açıklarını tespit etmeye çalışır. SQLMap, veritabanı tespiti için entegre edilmiştir ve Kali Linux kullanıcıları için önceden yüklü olduğundan herhangi bir ek kurulum gerekmez.

## Özellikler

- **Komut Enjeksiyonu** testi yapar.
- **Açık Dizin** testi gerçekleştirir.
- **Dosya Dahil Etme** testleri yapar.
- **SQLMap** ile veritabanlarını tespit eder.
- **Renkli ASCII Sanatı** ve **bilgilendirme mesajları** ile kullanıcı dostudur.

## Gereksinimler

### Python Kütüphaneleri

- `requests`
- `beautifulsoup4`
- `termcolor`
- `pyfiglet`
- `colorama`

### Harici Araçlar

- **SQLMap**: Veritabanı tespiti için kullanılan bir araçtır. Kali Linux üzerinde varsayılan olarak yüklüdür. [SQLMap İndir](https://github.com/sqlmapproject/sqlmap) (Kali Linux kullanıcıları için yükleme gerekmemektedir.)

## Kurulum

### Adım 1: Python Yüklemesi

Öncelikle Python 3'ün yüklü olduğundan emin olun. Python 3'ü yüklemek için şu komutu kullanabilirsiniz:

#### Ubuntu / Debian
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Adım 2: Gerekli Python Kütüphanelerini Yükleme

Aşağıdaki komutları kullanarak gerekli kütüphaneleri yükleyin:

```bash
pip3 install requests beautifulsoup4 termcolor pyfiglet colorama
```

### Adım 3: SQLMap (Kali Linux İçin)

**SQLMap** Kali Linux üzerinde varsayılan olarak yüklü olduğu için, ekstra bir kurulum yapmanıza gerek yok. Ancak, başka bir dağıtım kullanıyorsanız, [SQLMap İndir](https://github.com/sqlmapproject/sqlmap) sayfasından indirebilirsiniz.

### Adım 4: Dosyayı İndirip Çalıştırma
```bash
git clone https://github.com/sarsilmazhackteam/root-web-tool.git
```
Aracı indirdikten sonra aşağıdaki komutları kullanarak çalıştırabilirsiniz:

1. `sarsilmaz.py` dosyasını indirin.
2. Dosyanın bulunduğu dizine gidin.

```bash
python3 sarsilmaz.py <hedef_url>
```

Örneğin:

```bash
python3 sarsilmaz.py http://testphp.vulnweb.com/listproducts.php?cat=1
```

## Kullanım

### URL Tarama

Aracı çalıştırmak için, aşağıdaki komutu kullanarak hedef URL'yi belirleyin:

```bash
python3 sarsilmaz.py <hedef_url>
```

Örneğin:

```bash
python3 sarsilmaz.py http://testphp.vulnweb.com/listproducts.php?cat=1
```

Yukarıdaki komut, belirtilen URL'yi tarar ve olası güvenlik açıklarını raporlar.

### Desteklenen Testler

- **Komut Enjeksiyonu**: Sisteme dış komutların enjeksiyonu yapılıp yapılamadığını kontrol eder.
- **Açık Dizin**: Web sunucusunda açık dizinlerin olup olmadığını kontrol eder.
- **Dosya Dahil Etme**: `../../../../etc/passwd` gibi zararlı dosyaların dahil edilip edilemediğini test eder.
- **SQL Injection**: SQLMap kullanarak hedefin veritabanlarını tespit eder.

### Çıktı Örneği

Aracı çalıştırdıktan sonra şu şekilde bir çıktı alabilirsiniz:

```bash
[+] http://testphp.vulnweb.com/listproducts.php?cat=1 taranıyor...

[+] Komut Enjeksiyonu açığı bulunamadı.
[+] Açık dizin bulunamadı.
[+] Dosya Dahil Etme açığı bulunamadı.
[*] SQLMap ile veritabanları tespit ediliyor...
[!] Bulunan veritabanları:
    - test_db
    - users_db
```

## Sorun Giderme

- **SQLMap Yüklenmedi**: Eğer SQLMap yüklü değilse, `sqlmap` komutunun çalışmadığını görürsünüz. Kali Linux üzerinde SQLMap zaten yüklü olduğundan bu adımı atlayabilirsiniz. Diğer Linux dağıtımlarında ise [SQLMap İndir](https://github.com/sqlmapproject/sqlmap) sayfasından indirip kurabilirsiniz.

- **Yetersiz Yetki**: SQLMap'in çıktıları, doğru izinlere sahip olmalıdır. Özellikle `/tmp` dizini gibi geçici dizinlere erişiminiz olması gerekebilir.

## Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, pull request'ler açabilir veya sorunlarınızı raporlayabilirsiniz.

## Lisans

Bu proje, MIT Lisansı altında lisanslanmıştır.

---

Tüm katkılar ve öneriler için teşekkür ederiz!
