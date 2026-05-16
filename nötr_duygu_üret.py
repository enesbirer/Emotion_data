import json
import random

FILE_PATH = r"c:\Users\Enes\Desktop\Yapayzeka Dataset\emotion_data.json"
TARGET = 500
LABEL = "nötr"

openers = [
    "Gün içinde pek çok şey üst üste geldi ve zihin yordu",
    "Bekleyiş uzadıkça duygular sağa sola savruldu",
    "Yanıt gecikince kafamda farklı senaryolar gezindi",
    "İddialar havada uçuşunca ortalık karıştı",
    "Veriler birbiriyle çelişince anlamlandırmak zorlaştı",
    "Konuşmanın tonları dalgalanınca belirsizlik arttı",
    "Planlar değişince bakış açısı kaydı",
    "Duygular bir sağa bir sola çekiştirince yoruldum",
    "Sessizlik uzayınca anlam bulanıklaştı",
    "Uyarılar ve müjdeler aynı anda gelince kafa karıştı"
]

connectors = [
    "ama analiz derinleşince resim netleşti",
    "ancak kanıtlar sıralanınca tablo aydınlandı",
    "fakat ölçütler belirlenince akış sadeleşti",
    "gelgelelim yöntem belirlenince süreç düzenlendi",
    "nihayet gerçekler ortaya konunca gürültü azaldı",
    "sonrasında çerçeve çizilince anlam berraklaştı",
    "derken taraflar sakinleşince konuşma dengelendi",
    "akabinde denge politikası benimsendi",
    "tam o sırada standartlar kabul edilince ölçü oluştu",
    "uzun bir değerlendirmeden sonra tartışma soğudu"
]

settings = [
    "toplantı odasında",
    "ofiste",
    "laboratuvarda",
    "kütüphane bölümünde",
    "konferans salonunda",
    "belediye salonunda",
    "mahkeme koridorunda",
    "dernek binasında",
    "sınıf içinde",
    "seminer sırasında",
    "kampüste",
    "şehir meclisinde",
    "basın odasında",
    "panel çıkışında",
    "komite çalışmasında",
    "kurul görüşmesinde",
    "arabuluculuk toplantısında",
    "uzlaşı masasında",
    "rapor yazımında",
    "taslak değerlendirmesinde"
]

enrichers = [
    "duyguları ayıklayarak",
    "verileri karşılaştırarak",
    "ölçütleri tanımlayarak",
    "kanıt zincirini kurarak",
    "hipotezleri sınayarak",
    "tarafsız dili koruyarak",
    "serinkanlı bir üslup benimseyerek",
    "nesnel bakış açısı geliştirerek",
    "aşırılıklardan kaçınarak",
    "mantığı önceleyerek",
    "ortak payda arayarak",
    "dengeyi gözeterek",
    "süpheleri gidererek",
    "öncelikleri belirleyerek",
    "sorunları sınıflandırarak",
    "akılcı bir plan yaparak",
    "arabuluculuk kanallarını açarak",
    "uzlaşı zemini kurarak",
    "karar çerçevesini çizerek",
    "ölçülü değerlendirme yaparak"
]

noise = [
    "nötr bir bakışla süzülen tarafsızlık",
    "öfke ve kırgınlık gölgeleri",
    "umut ve kuşku karışımı",
    "rahatsızlık ve endişe",
    "şaşkınlık ve donakalma",
    "stres ve telaş",
    "kafa karışıklığı ve belirsizlik",
    "gerilim ve bekleyiş",
    "yorgunluk ve bitkinlik",
    "görüş ayrılıkları"
]

endings = [
    "durumu objektif değerlendirdim ve nötr kaldım",
    "duygusal tepkiden kaçınıp tarafsız bir karar verdim",
    "olayı serinkanlılıkla kapatıp nötr bir tutum aldım",
    "ne sevindim ne üzüldüm, ölçülü davrandım",
    "meseleyi sakin bir kararla sonlandırdım",
    "gerçeklere bakıp yorum yapmadan geçtim",
    "dengeyi koruyup duygusuz bir sonuçla kapattım",
    "mesafeli kalıp tarafsız kaldım",
    "duyguları ayıklayıp nötr karşılıyorum",
    "nesnel bakıp aşırıya kaçmadan noktayı koydum",
    "uzlaşı ihtimali koruyup nötr kaldım",
    "karar metnini tarafsızca onayladım",
    "standartlara bağlı kalıp nötr tutum aldım",
    "serinkanlı bir değerlendirmeyle nötr sonuca vardım",
    "ölçülü bir cümleyle tartışmayı noktaladım",
    "nesnel çizgiye sadık kalarak nötr kaldım",
    "denge ilkesiyle tarafsızlık korudum",
    "uyuşmazlığı duygusuzca kapatarak nötr kaldım",
    "ortak paydaya bağlı kalıp nötr tutum aldım",
    "nesnellik baskın olup nötr kaldım"
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
