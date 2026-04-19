# YZM212 Makine Öğrenmesi - 4. Ödev

**Öğrenci:** Görkem Özer  
**Numara:** 23291007

## Problem Tanımı
Gürültülü gözlem verilerinden Bayesyen çıkarım ve MCMC yöntemiyle bir gök cisminin gerçek parlaklığı (μ) ve gözlem hatası (σ) tahmin edilmiştir.

## Veri
- Gerçek μ = 150.0, gerçek σ = 10.0
- 50 adet gürültülü gözlem (normal dağılım)
- Rastgele tohum: seed=42

## Yöntem
- **Likelihood:** Gaussian
- **Prior:** Uniform (geniş: 0<μ<300, 0<σ<50) ve dar (100<μ<110) karşılaştırması
- **MCMC:** emcee kütüphanesi, 32 walker, 2000 adım, burn-in=500, thin=15
- **Deneyler:** Prior etkisi, veri miktarı etkisi (n=5)

## Sonuçlar
- μ tahmini: 149.85 [147.20, 152.50]
- σ tahmini: 10.42 [8.60, 12.80]
- Mutlak hata μ: 0.15, σ: 0.42

## Yorum
- Bayesyen yöntem gürültülü veride başarılıdır.
- Yanlış prior tahmini bozar.
- Az veriyle belirsizlik artar.
- μ ve σ arasında pozitif korelasyon vardır.

## Dosyalar
- `odev.ipynb` – Tüm kod ve analizler
- `odev4rapor.pdf` – Detaylı rapor
- 'Sonuclar.txt' - Sonuclar
