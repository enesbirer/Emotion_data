# 📊 Duygu Analizi Veri Seti (8 Sınıflı)

## 📌 Proje Açıklaması

Bu veri seti, Türkçe metinler üzerinde duygu analizi (sentiment analysis) modelleri geliştirmek amacıyla hazırlanmıştır. Veri seti toplamda 8 farklı duygu sınıfını içermektedir.

Veri seti oluşturulurken cümle çeşitliliğini artırmak için çoklayıcı (data augmentation) yöntemi kullanılmış, ancak tüm cümleler manuel olarak kontrol edilerek düzenlenmiştir. Böylece hem çeşitlilik hem de dilsel tutarlılık sağlanmıştır.

---

## 😊 Duygu Sınıfları

Veri seti aşağıdaki 8 duygu kategorisinden oluşmaktadır:

- Mutluluk 😊  
- Üzüntü 😢  
- Öfke 😡  
- Korku 😨  
- Şaşkınlık 😲  
- Tiksinme 🤢  
- Güven 😌  
- Nötr 😐  

---

## 📁 Veri Seti Yapısı

Veri seti genellikle CSV formatındadır.

### Dosya adı:

### Örnek veri yapısı:

| text | label |
|------|-------|
| Bugün kendimi çok iyi hissediyorum | Mutluluk |
| Bu haber beni gerçekten çok üzdü | Üzüntü |
| Buna inanamıyorum, şok oldum | Şaşkınlık |

---

## ⚙️ Veri Oluşturma Süreci

Veri seti hazırlanırken aşağıdaki adımlar izlenmiştir:

- Her duygu sınıfı için temel cümleler oluşturuldu  
- Çoklayıcı (augmentation) yöntemi ile veri çeşitliliği artırıldı  
- Cümleler manuel olarak gözden geçirildi  
- Dil bilgisi ve anlam bütünlüğü kontrol edildi  
- Sınıflar arasında mümkün olduğunca denge sağlandı  

---

## 🎯 Kullanım Alanları

Bu veri seti şu alanlarda kullanılabilir:

- Duygu analizi (Sentiment Analysis)  
- Türkçe NLP projeleri  
- Metin sınıflandırma modelleri  
- Makine öğrenmesi ve derin öğrenme çalışmaları  
- Akademik araştırmalar  

---

## 🚀 Basit Kullanım Örneği (Python)

```python
import pandas as pd

df = pd.read_csv("dataset.csv")

print(df.head())

# Sınıf dağılımı
print(df["label"].value_counts())
