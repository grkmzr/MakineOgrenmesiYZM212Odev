# Logistic Regression

## İsim: Görkem Özer  
## Numara: 23291007  

## Logistic Regression Nedir?

Logistic Regression, sınıflandırma problemlerinde kullanılan bir makine öğrenmesi algoritmasıdır. Adında "regression" geçmesine rağmen aslında sınıflandırma yapar.

Bu algoritma, bir verinin belirli bir sınıfa ait olma olasılığını hesaplar.

---

## Çalışma Mantığı

Logistic Regression, doğrusal bir fonksiyonu sigmoid fonksiyonundan geçirerek çıktı üretir.

Sigmoid fonksiyonu şu şekildedir:

f(x) = 1 / (1 + e^(-x))

Bu fonksiyon çıktıyı 0 ile 1 arasına sıkıştırır. Bu da olasılık olarak yorumlanır.

- 0’a yakınsa → sınıf 0  
- 1’e yakınsa → sınıf 1  

---

## Kullanım Alanları

Logistic Regression genellikle şu alanlarda kullanılır:

- Spam tespiti  
- Hastalık tahmini  
- Müşteri davranışı analizi  

---

## Avantajları

- Basit ve anlaşılırdır  
- Hızlı çalışır  
- Küçük veri setlerinde iyi performans verir  

---

## Dezavantajları

- Karmaşık veri yapılarında yetersiz kalabilir  
- Lineer ilişki varsayar  

---

## Örnek Kullanım (Python)

```python
from sklearn.linear_model import LogisticRegression
import numpy as np

# Veri
X = np.array([[1,2], [2,3], [3,4], [6,7], [7,8], [8,9]])
y = np.array([0,0,0,1,1,1])

# Model
model = LogisticRegression()
model.fit(X, y)

# Tahmin
print(model.predict([[5,6]]))