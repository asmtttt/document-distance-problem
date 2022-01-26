import math
from string import punctuation,digits

def dosya_Oku(dosya_ad): # dosyayi okuyup bir degiskene atiyoruz
  with open(dosya_ad, 'r') as dosya:
    metin = dosya.read()

  return metin

def kelimelere_ayir(metin):
  cevirici = str.maketrans('', '', punctuation)  # noktalama isaretlerinin silinme operasyonu uygulandi.
  icerik = metin.translate(cevirici)  # silinme operasyonunun metin degiskeninde uygulandi.
  cevirici = str.maketrans('', '', digits)  # noktalama isaretlerinin silinme operasyonu uygulandi.
  icerik = metin.translate(cevirici)  # silinme operasyonunun metin degiskeninde uygulandi.

  icerik = icerik.lower()  # metindeki buyuk harfler kucuk harfe cevrildi
  icerik = icerik.replace("\n", " ")  # satir sonunda hata cikarticak sorunlar duzeltildi
  icerik = icerik.split()  # metin bosluklardan kelimelere ayrildi


  return icerik

def farkli_kelimeler_frekanslari(kelime_listesi):
  farkli_kelimeler_frekanslari = {}

  for i in kelime_listesi:

    if i in farkli_kelimeler_frekanslari:
      farkli_kelimeler_frekanslari[i] = farkli_kelimeler_frekanslari[i] + 1

    else:
      farkli_kelimeler_frekanslari[i] = 1

  return farkli_kelimeler_frekanslari


def vektor_bul(dosya_ad):
  metin = dosya_Oku(dosya_ad)
  kelime_listesi = kelimelere_ayir(metin)
  vektor = farkli_kelimeler_frekanslari(kelime_listesi)

  return vektor


def ic_carpim(vektor1, vektor2):
  toplam = 0

  for i in vektor1:

    if i in vektor2:
      toplam += (vektor1[i] * vektor2[i])

  return toplam

def uzunluk_carpim(vektor1,vektor2):

  uzunluk_carpim = math.sqrt(ic_carpim(vektor1, vektor1) * ic_carpim(vektor2, vektor2))

  return uzunluk_carpim

def vektor_acisi(vektor1, vektor2):
   deger = ic_carpim(vektor1, vektor2) / uzunluk_carpim(vektor1,vektor2)
   aci = math.acos(deger)
   aci = aci / math.pi

   return aci

def belge_mesafesi(dosya_ad1, dosya_ad2):

  a = vektor_bul(dosya_ad1)
  b = vektor_bul(dosya_ad2)
  benzerlik_acisi = vektor_acisi(a, b)

  return benzerlik_acisi



print("Bilgilendirme : Sonuç 0'a yaklaştıkça dokümanlar arası benzerlik artmaktadır.\n"
      "Sonuç = 0 ise iki doküman aynı dokümandır.")
print('')
print('')

# testler

print("nutuk ve nutuk arasindaki benzerlik degeri : ", belge_mesafesi("nutuk","nutuk"))
#print("safahat ve safahat arasindaki benzerlik degeri : ", belge_mesafesi("safahat","safahat"))
#print("genclikhitabe ve genclikhitabe arasindaki benzerlik degeri : ", belge_mesafesi("genclikhitabe","genclikhitabe"))
print("nutuk ve safahat arasindaki benzerlik degeri : ", belge_mesafesi("nutuk","safahat"))
print("nutuk ve genclikhitabe arasindaki benzerlik degeri : ",belge_mesafesi("nutuk","genclikhitabe"))
#print("genclikhitabe ve safahat arasindaki benzerlik degeri : ",belge_mesafesi("genclikhitabe","safahat"))
