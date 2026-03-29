# Eigenvalues ve Eigenvectors

İsim: Görkem Özer  
Numara: 23291007  

## 1. Teorik Kısım

Makine öğrenmesinde veriler genellikle matrisler şeklinde tutulur. Her satır bir gözlemi, her sütun ise bir özelliği temsil eder. Bu yüzden matris işlemleri oldukça önemlidir.

Özdeğer (eigenvalue) ve özvektör (eigenvector) kavramları bu matrislerin yapısını anlamak için kullanılır.

Bir matris A için:

A * v = λ * v

Burada:
- v → özvektör
- λ → özdeğer

Bu kavramlar özellikle PCA (Principal Component Analysis) yönteminde kullanılır. PCA sayesinde veri boyutu düşürülürken önemli bilgiler korunur.

Ayrıca:
- SVD
- Spektral clustering

gibi yöntemlerde de kullanılır.

---

## 2. Numpy eig fonksiyonu

Numpy kütüphanesinde bulunan np.linalg.eig fonksiyonu bir matrisin özdeğerlerini ve özvektörlerini hesaplar.

Örnek kullanım:

import numpy as np

A = np.array([[1,2],
              [3,4]])

values, vectors = np.linalg.eig(A)

Fonksiyon arka planda QR algoritması gibi yöntemler kullanır.

---

## 3. Manuel hesaplama ve karşılaştırma

Matris:

A = [[4,2],
     [1,3]]

Karakteristik denklem:

|A - λI| = 0

(4-λ)(3-λ) - 2 = 0

λ² - 7λ + 10 = 0

Buradan:

λ1 = 5  
λ2 = 2  

Numpy ile yapılan hesaplama da aynı sonucu verir.

---

## Sonuç

Bu ödevde özdeğer ve özvektör kavramlarının makine öğrenmesindeki önemi incelenmiştir. Özellikle PCA gibi yöntemlerde kritik rol oynadığı görülmüştür.