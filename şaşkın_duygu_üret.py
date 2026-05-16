import json
import random

FILE_PATH = r"c:\Users\Enes\Desktop\Yapayzeka Dataset\emotion_data.json"
TARGET = 500
LABEL = "şaşkın"

openers = [
    "Uzun süredir beklediğim şey tam aksi çıktı",
    "Planlar bambaşka bir yöne evrildi ve kafam karıştı",
    "Konuşmanın akışı beklenmedik biçimde değişince afalladım",
    "Haberde şaşırtıcı bir ayrıntı görünce duraksadım",
    "Denediğim yöntem ters tepti ve sorgulamaya başladım",
    "İşler beklenmedik şekilde çözülünce ne düşüneceğimi bilemedim",
    "Güne damga vuran olay beklediğimden farklı oldu",
    "Kafamdaki tabloyla gerçekte olan uyuşmayınca şaşırdım",
    "Yanıt bambaşka gelince aklım durdu",
    "Beklenti ile sonuç arasındaki fark çarpıcıydı"
]

connectors = [
    "ama ayrıntı anlatılınca olay bambaşka bir ışık kazandı",
    "ancak perde arkasında farklı bir neden olduğu ortaya çıktı",
    "fakat teknik detaylar açıklanınca resim değişti",
    "gelgelelim yeni bir veri gelince tablo dönüştü",
    "nihayet net bir kanıt sunulunca akış başka yöne kaydı",
    "sonrasında planların gizli tarafı öğrenilince anlayışım değişti",
    "derken beklenmedik bir jest yapılınca şaşırdım",
    "akabinde karmaşık düğüm çözülünce gözlerim açıldı",
    "tam o sırada sürpriz bir bilgi paylaşılınca hesaplar bozuldu",
    "uzun bir anlatımın ardından konunun özü anlaşılınca şaşkın kaldım"
]

settings = [
    "kalabalık bir durakta",
    "yağmurlu bir akşamüstünde",
    "sessiz bir odada",
    "sıkışık bir trafikte",
    "ofiste yoğun bir günün sonunda",
    "metroda yol alırken",
    "parkta oturmuşken",
    "evde tek başıma düşünürken",
    "müze koridorlarında",
    "pazar yerinde kalabalık arasında",
    "havaalanında beklerken",
    "kamp alanında",
    "dağ yolunda",
    "sahil boyunca",
    "market kasasında",
    "belediye salonunda",
    "mahalle aralarında",
    "kütüphane raflarında",
    "laboratuvar ortamında",
    "stüdyoda"
]

enrichers = [
    "kanıtları tek tek dizerek",
    "farklı senaryoları karşılaştırarak",
    "önkabulleri sorgulayarak",
    "mantık çıtalarını yeniden kurarak",
    "örüntüleri dikkatle izleyerek",
    "veri akışını çapraz kontrol ederek",
    "başka örneklerle kıyaslayarak",
    "gözlem gücünü keskinleştirerek",
    "tuhaflıkları listeleyerek",
    "detaylara ışık tutarak",
    "yeni bakış açısı geliştirerek",
    "alternatif açıklamalar deneyerek",
    "kanıt zincirini tamamlayarak",
    "belirsizlikleri ayıklayarak",
    "soruları derinleştirerek",
    "çıkarımları revize ederek",
    "soğukkanlı bir inceleme yaparak",
    "tüm resmi tekrar kurarak",
    "öncelikleri yeniden belirleyerek",
    "zihin haritasını güncelleyerek"
]

noise = [
    "şaşkınlık, hayret, afallama ve donakalma hissi",
    "kafa karışıklığı ve tereddüt",
    "endişe ve huzursuzluk",
    "stres ve telaş",
    "rahatsızlık ve belirsizlik",
    "yorgunluk ve bitkinlik",
    "umut ve kuşku karışımı",
    "gerilim ve bekleyiş",
    "tuhaf bir sessizlik",
    "alışılagelmişin bozulması"
]

endings = [
    "donakaldım ve şaşkına döndüm",
    "aklım durdu, hayret ettim",
    "beklenmedik gerçeği duyunca afalladım",
    "ters köşe olup şaşırdım",
    "mantığı zorlayan ayrıntıya hayret ettim",
    "aniden değişince şaşkın kaldım",
    "olay farklı akınca şaşırdım",
    "kimsenin beklemediği sonuçla şaşırıp kaldım",
    "açıklamayı duyunca ağzım açık kaldı",
    "hesaplar tutmayınca şaşkınlık bastı",
    "yeni veri gelince şaşkına döndüm",
    "beklenmedik jestle şaşırdım",
    "görmediğim bağlantı ortaya çıkınca hayret ettim",
    "nokta atışı delille afalladım",
    "kök neden öğrenilince şaşırdım",
    "kural dışı sonuçla donakaldım",
    "yerleşik inanç bozulunca şaşkın kaldım",
    "özgün çözüm görünce hayret ettim",
    "yansımalar bambaşka çıkınca afalladım",
    "beklentiyle sonuç çakışmayınca şaşırdım"
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
