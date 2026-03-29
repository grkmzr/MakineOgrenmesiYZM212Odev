# YZM212 - Makine Öğrenmesi: MLE ile Trafik Yoğunluğu Modellemesi

Bu proje, bir şehir caddesinden 1 dakikada geçen araç sayılarını modellemek için **Maximum Likelihood Estimation (MLE)** yöntemini kullanmayı amaçlamaktadır.

## Problem Tanımı
Bir belediyenin elindeki trafik verilerine dayanarak, caddenin ortalama trafik yoğunluğunu (λ) tahmin etmek ve bu yoğunluğun Poisson Dağılımı'na uygunluğunu incelemek.

## Veri Seti
Veri seti, bir caddeden 1 dakikada geçen araç sayılarını içeren 14 gözlemden oluşmaktadır:
`[12, 15, 10, 8, 14, 11, 13, 16, 9, 12, 11, 14, 10, 15]`

## Kullanılan Yöntemler
1.  **Analitik MLE:** Poisson dağılımı için Log-likelihood fonksiyonu türetilmiş ve MLE tahmincisinin (λ̂) verilerin ortalaması olduğu kanıtlanmıştır.
2.  **Sayısal MLE:** `scipy.optimize` kütüphanesi kullanılarak Negatif Log-Likelihood (NLL) fonksiyonu minimize edilmiş ve λ değeri bulunmuştur.
3.  **Görselleştirme:** Bulunan λ ile teorik Poisson dağılımı çizilmiş, gerçek veri histogramı ile karşılaştırılmıştır.
4.  **Aykırı Değer (Outlier) Analizi:** Veri setine gerçek dışı bir değer (200) eklenerek MLE'nin bu durumdan nasıl etkilendiği incelenmiştir.

## Sonuçlar
- Analitik ve sayısal MLE yöntemleri aynı sonucu vermiştir: **λ ≈ 12.0**.
- Oluşturulan Poisson modeli, gerçek veri histogramına oldukça iyi uyum sağlamıştır.
- Tek bir aykırı değer (200), MLE tahminini **24.5'e** yükselterek büyük bir hataya yol açmıştır. Bu durum, veri ön işlemenin önemini vurgulamaktadır.

## Tartışma / Yorum
MLE, teoride güçlü bir tahmin yöntemi olsa da, aykırı değerlere karşı hassastır. Gerçek hayat projelerinde, modelleme aşamasından önce veri temizliği ve aykırı değer analizi yapılması kritik öneme sahiptir. Aksi takdirde, hatalı tahminler maliyetli ve yanlış kararlara (örneğin gereksiz yol genişletme projeleri) yol açabilir.