import json
import random

FILE_PATH = r"c:\Users\Enes\Desktop\Yapayzeka Dataset\emotion_data.json"
TARGET = 500
LABEL = "iğrenmiş"

openers = [
    "Gözümün önünde hijyen kurallarının çiğnenmesi canımı sıktı",
    "Mekanda ağır bir koku yayılınca rahatsız oldum",
    "Yemekte bozulmuş tat fark edince içim kalktı",
    "Saygısız bir davranış görünce tiksindim",
    "Özensizlik ve dağınıklık her yere sinince huzursuzlandım",
    "Etik dışı bir hamle duyunca midem bulandı",
    "Sorumsuzluk ve pislik yan yana görünce içim çekildi",
    "Kalabalıkta kirli alışkanlıklar sergilenince rahatsızlandım",
    "Uygunsuz sözler ortama yayıldıkça iğrendim",
    "Bozuk düzen ve kaba tavır bir araya gelince içim bulandı"
]

connectors = [
    "ama uyarı yapılınca tablo kısmen düzeldi",
    "ancak sebep anlatılınca yüzeydeki neden anlaşıldı",
    "fakat temizlik ekibi gelince hava değişti",
    "gelgelelim özür dilenip düzenleme yapıldı",
    "nihayet kurallar hatırlatılınca ortam toparlandı",
    "sonrasında etik çerçeve vurgulanınca davranışlar düzeldi",
    "derken kapılar açılıp havalandırma başlayınca rahatladım",
    "akabinde kontrol yapılıp sorun giderilince hava yumuşadı",
    "tam o sırada denetim gelince düzen sağlandı",
    "uzun bir uyarı listesinin ardından önlem alındı"
]

settings = [
    "kalabalık bir lokantada",
    "pazar tezgahında",
    "otobüs bekleme alanında",
    "okul kantininde",
    "sokak arasında",
    "işlek bir caddede",
    "spor salonu soyunma odasında",
    "hastane koridorunda",
    "konser alanında",
    "kamusal mutfakta",
    "ofis yemekhanesinde",
    "fabrika girişinde",
    "mahalle pazarında",
    "sahil boyunca",
    "kamp alanında",
    "stadyum çevresinde",
    "metro istasyonunda",
    "kafe arka bölümünde",
    "kütüphane dinlenme alanında",
    "sergi salonunda"
]

enrichers = [
    "kuralları hatırlatarak",
    "nazikçe uyararak",
    "temizliğin önemini anlatarak",
    "düzen ve özen vurgusu yaparak",
    "hijyen standartlarını sıralayarak",
    "etik ilkeleri hatırlatarak",
    "rahatsızlığı ölçülü bir dille paylaşarak",
    "görevliye bilgi vererek",
    "kayıt tutmayı teklif ederek",
    "denetim çağrısı yaparak",
    "gözlem notları tutarak",
    "yanlış alışkanlıkları işaret ederek",
    "sağlık risklerini anlatıp ikna ederek",
    "ortak kullanım alanını korumayı savunarak",
    "uygulama planı önererek",
    "çözüm odaklı konuşarak",
    "nazik bir dille",
    "kararlı bir tutumla",
    "serinkanlı kalmaya çalışarak",
    "görüleni açıkça ifade ederek"
]

noise = [
    "iğrenme, tiksinti ve rahatsızlık yankıları",
    "öfke ve kırgınlık kırıntıları",
    "huzursuzluk ve endişe",
    "şaşkınlık ve donakalma",
    "stres ve telaş",
    "rahatsızlık ve mide bulantısı",
    "koku ve kir yansımaları",
    "gözle görülen kusurlar",
    "düzensizlik ve kabalık",
    "pis görüntüler"
]

endings = [
    "tiksindim ve midem bulandı",
    "içim kalktı ve iğrendim",
    "kirli ayrıntıyı duyunca rahatsızlık sardı",
    "saygısız davranıştan iğrendim",
    "uygunsuzluk görünce içim çekildi",
    "koku dayanılmaz olunca tiksinti bastı",
    "ahlaki sınır aşılınca iğrendim",
    "pislik görünce midesi bulandı",
    "bozulmuş tatla iğrenme arttı",
    "etik dışı hamleye tiksindim",
    "kabalık ve hijyen eksikliği birleşince iğrendim",
    "çöp görüntüsüyle midem bulandı",
    "yağlı yüzey ve koku iğrenme yarattı",
    "kirli tutumla içim kalktı",
    "duyarsızlık karşısında tiksindim",
    "yapış yapış hisle iğrendim",
    "temizlik hiçe sayılınca iğrendim",
    "pis ayrıntılar görünce rahatsızlık büyüdü",
    "bozulan düzen iğrenme doğurdu",
    "hijyen ihlaliyle içim bulandı"
]

def generate_sentence():
    opener = random.choice(openers)
    connector = random.choice(connectors)
    setting = random.choice(settings)
    enricher = random.choice(enrichers)
    n = random.choice(noise)
    end = random.choice(endings)
    pivot = random.choice(["ama", "ancak", "fakat", "gelgelelim", "nihayet", "sonrasında"])
    parts = [
        opener,
        connector + " " + setting,
        enricher + " duyguların karmaşasına rağmen " + n + " iç içe geçiyordu",
        pivot + " " + end
    ]
    s = ", ".join(parts)
    return " ".join(s.split())

def main():
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    seen = set()
    added = []
    while len(added) < TARGET:
        s = generate_sentence()
        if len(s.split()) < 22:
            continue
        if s in seen:
            continue
        seen.add(s)
        added.append({"text": s, "label": LABEL})
    data.extend(added)
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("Added:", len(added))

if __name__ == "__main__":
    main()
