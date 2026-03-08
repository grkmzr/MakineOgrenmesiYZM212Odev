# MakineOgrenmesiYZM212Odev
# YZM212 Makine Öğrenmesi - Laboratuvar 1: HMM ile İzole Kelime Tanıma

**Öğrenci:** Görkem Özer  
**Numara:** 23291007  
**Tarih:** 8 Mart 2026

---

## Problem Tanımı

Bu laboratuvar çalışmasında, Saklı Markov Modelleri (Hidden Markov Models - HMM) kullanarak iki farklı kelimeyi ("EV" ve "OKUL") tanıyan bir sistem tasarlanması hedeflenmiştir. Çalışma iki ana bölümden oluşmaktadır:

1. **Teorik Kısım:** "EV" kelimesi için verilen geçiş ve emisyon olasılıkları kullanılarak, [High, Low] gözlem dizisinin en olası fonem dizisinin Viterbi algoritması ile hesaplanması.
2. **Uygulama Kısmı:** Python'da `hmmlearn` kütüphanesi kullanarak "EV" ve "OKUL" kelimeleri için iki ayrı HMM modeli oluşturulması ve yeni bir ses verisinin hangi kelimeye ait olduğunun log-olasılık skorlarına göre sınıflandırılması.

---

## Kullanılan Yöntem

### Teorik Kısım

Verilen parametreler:

- Gizli Durumlar: `S = {e, v}`
- Gözlemler: `O = {High (0), Low (1)}`
- Başlangıç olasılığı: `P(e) = 1.0`
- Geçiş olasılıkları (A):
  - `P(e → e) = 0.6`, `P(e → v) = 0.4`
  - `P(v → v) = 0.8`, `P(v → e) = 0.2`
- Emisyon olasılıkları (B):
  - `e` durumunda: `P(High|e) = 0.7`, `P(Low|e) = 0.3`
  - `v` durumunda: `P(High|v) = 0.1`, `P(Low|v) = 0.9`

Gözlem dizisi: `[High, Low]` → indeks olarak `[0, 1]`

Viterbi algoritması adım adım uygulanmış ve en olası durum dizisi bulunmuştur.

### Uygulama Kısmı

- `hmmlearn` kütüphanesi kullanılmıştır.
- Her kelime için 2 durumlu (fonem sayısı kadar) multinom HMM tanımlanmıştır.
- Eğitim verisi olarak, her kelime için rastgele gözlem dizileri oluşturulmuştur. Gerçek bir ses verisi olmadığından, kelimelerin fonem yapılarına uygun rastgele diziler üretilmiştir.
- Test verisi olarak `[0, 1, 1]` gözlem dizisi kullanılmıştır.
- `score()` fonksiyonu ile log-olasılık hesaplanmış ve hangi modelin daha yüksek skor verdiğine bakılmıştır.

---

## Sonuçlar

- **Viterbi sonucu:** En olası fonem dizisi **"e-v"** olarak bulunmuştur.
- **Uygulama sonucu:** Test verisi `[0, 1, 1]` için EV modeli daha yüksek log-olasılık vermiştir. Bu durum, test verisinin EV kelimesine ait olduğunu göstermektedir.

---

## Yorum ve Tartışma

### 1. Gürültünün Emisyon Olasılıklarına Etkisi

Ses verisindeki gürültü, HMM'in emisyon olasılıklarını doğrudan etkiler. Örneğin, bir fonem için beklenen frekans karakteristiği High iken, gürültü nedeniyle Low gözlemlenebilir. Bu durumda, emisyon olasılıkları değişir ve modelin doğruluğu düşer. Eğitim verisi gürültülüyse, emisyon matrisi de bu gürültüyü öğrenir ve gerçek seslerde yanlış sınıflandırma yapabilir.

### 2. Neden Deep Learning?

Binlerce kelimenin olduğu bir sistemde HMM kullanmak pratik değildir çünkü:
- Her kelime için ayrı bir HMM eğitmek gerekir.
- Fonem geçişleri ve emisyonlar manuel ayarlanamaz.
- Deep learning modelleri (RNN, LSTM, Transformer) tüm kelimeleri tek bir modelde öğrenebilir, daha esnektir ve daha yüksek doğruluk sağlar.
