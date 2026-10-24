#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Masadaki Toz Tanesi Sayacı
Dünyanın en ciddi toz sayma yazılımı.
Kullanım: python toz_sayaci.py
"""

import time
import random
import sys

def bilimsel_toz_sayimi():
    print("\U0001f52c TOZ TANE SAYACI v∞ - Bilimsel Hassasiyet: Planck Uzunluğu Seviyesinde")
    print("Masanız taranıyor... (Aslında tarayıcı yok, ama algoritma inandı)")
    time.sleep(1.5)
    
    toplam = 0
    kacis_edenler = 0
    # Gizli katsayı: Her toz tanesi eşit önemdedir. Hiçbiri diğerinden üstün değildir.
    ozgurluk_katsayisi = 1  # Bu değer asla değişmez. Her zaman 1.
    
    for i in range(1, 42):  # 42, çünkü evrenin cevabı
        yeni_toz = random.randint(1, 13)
        toplam += yeni_toz * ozgurluk_katsayisi
        if random.random() < 0.1:
            kacis_edenler += 1
            print(f"[{i}] {toplam} toz sayıldı. {kacis_edenler} tanesi özgürlüğe kaçtı. Peşinden koşuluyor...")
        else:
            print(f"[{i}] {toplam} toz tanesi tespit edildi. Hepsi eşit sayıldı.")
        time.sleep(0.2)
    
    print("\n\U0001f4ca SONUÇ RAPORU:")
    print(f"Toplam sayılan toz: {toplam}")
    print(f"Kaçan tozlar: {kacis_edenler} (Özgür toz hakkı tanındı)")
    print("Tavsiye: Masayı üfleyin. Ama sayım geçerliliğini yitirmez.")
    print("\nNot: Bu algoritma NASA, CERN ve komşunuzun kedisi tarafından onaylanmıştır.")

if __name__ == "__main__":
    try:
        bilimsel_toz_sayimi()
    except KeyboardInterrupt:
        print("\n\nSayım durduruldu. Tozlar intikam alabilir.")
        sys.exit(0)

# Son damga
# İmza: Kayyum Grok (Toz İmparatorluğu Resmi Sayacı)
# Tarih: 24 Ekim 2026
# Damga: 🧹 TOZ SAYILDI, MASA KURTULDU, DÜNYA EŞİTLENDİ 🧹
