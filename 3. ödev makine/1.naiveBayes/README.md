# Naive Bayes

## İsim: Görkem Özer  
## Numara: 23291007  

## Naive Bayes Nedir?

Naive Bayes, olasılık temelli bir sınıflandırma algoritmasıdır. Bayes teoremini temel alır.

Bayes teoremi şu şekildedir:

P(A|B) = (P(B|A) * P(A)) / P(B)

Burada bir olayın gerçekleşme olasılığı, başka bir olaya bağlı olarak hesaplanır.

"Naive" denmesinin sebebi, özelliklerin birbirinden bağımsız olduğu varsayımını yapmasıdır. Gerçek hayatta bu çoğu zaman tam doğru değildir ama buna rağmen oldukça iyi sonuçlar verir.

---

## Kullanım Alanları

Naive Bayes genellikle şu alanlarda kullanılır:

- Spam filtreleme  
- Metin sınıflandırma  
- Duygu analizi (sentiment analysis)  

Özellikle metin verilerinde çok hızlı ve başarılıdır.

---

## Avantajları

- Hızlı çalışır  
- Az veri ile bile iyi sonuç verir  
- Uygulaması kolaydır  

---

## Dezavantajları

- Özelliklerin bağımsız olduğunu varsayar  
- Bu varsayım her zaman doğru değildir  

---

## Örnek Kullanım (Python)

```python
from sklearn.naive_bayes import GaussianNB
import numpy as np

# Veri
X = np.array([[1,2], [2,3], [3,4], [6,7], [7,8], [8,9]])
y = np.array([0,0,0,1,1,1])

# Model
model = GaussianNB()
model.fit(X, y)

# Tahmin
print(model.predict([[5,6]]))