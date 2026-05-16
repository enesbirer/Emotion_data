import json
import random

FILE_PATH = r"c:\Users\Enes\Desktop\Yapayzeka Dataset\emotion_data.json"
TARGET = 500
LABEL = "korkmuş"

openers = [
    "Gece yarısı beklenmedik bir ses duyunca irkildim",
    "Koridorda yankılanan adımlar tedirgin etti",
    "Haberde tehlikeli bir durumdan söz edilince içim ürperdi",
    "Karanlık sokakta yürürken kalbim hızlandı",
    "Telefonum bilinmeyen bir numaradan çalınca içim sıkıldı",
    "Kapıda gölge görünce nefesim daraldı",
    "Bilinmezlik büyüyünce sanki tehlike yaklaştı",
    "Sessizliğin ortasında ani bir gürültü duyunca sarsıldım",
    "Alarm çalınca refleksle ürktüm",
    "Sokak köşesinde tuhaf bir hareket görünce endişelendim",
    "Sarsıntı hissedince telaşlandım",
    "Kötü senaryolar zihnimi doldurdu",
    "Üst üste gelen uyarılar tedirginlik yarattı",
    "Işıklar aniden sönünce paniklediğim oldu",
    "Kapı kilidi takılınca korku büyüdü",
    "Tuhaf bir sessizlik içimi titretti",
    "Gölgeler uzadıkça içim ürperdi",
    "Puslu havada yönümü kaybedince endişelendim",
    "Kayıp bir ses ararken tedirgin oldum",
    "Beklenmeyen bir sızı duyunca panikledim"
]

connectors = [
    "ama ayrıntı netleşince tehlikenin boyutu anlaşıldı",
    "ancak konuşmanın ilerleyen kısmında işin uyarı olduğu ortaya çıktı",
    "fakat perde arkasında basit bir aksaklık olduğu öğrenildi",
    "gelgelelim teknik bir arıza çıkınca bekleme uzadı",
    "nihayet görevli açıklama yapınca tablo sakinleşti",
    "sonrasında güvenlik devriyesi görünce rahatladım",
    "derken sistemin test amacıyla çaldığı anlaşıldı",
    "akabinde ekip kontrol ederek durumun ciddiyetini azalttı",
    "tam o sırada yanlış alarm olduğu ortaya çıktı",
    "uzun bir aramanın ardından kaynağın zararsız olduğu görüldü"
]

settings = [
    "apartman boşluğunda",
    "karanlık bir sokakta",
    "ıssız bir durakta",
    "yol kenarında",
    "merdiven başında",
    "asansör beklerken",
    "otopark girişinde",
    "bodrum katında",
    "şehir dışındaki bir yolda",
    "kamp alanında",
    "dağ yamacında",
    "ıssız bir sahilde",
    "kalabalık pazar yerinde",
    "konut sitesinde",
    "okul koridorunda",
    "hastane girişinde",
    "stadyum çevresinde",
    "depo alanında",
    "otelde",
    "metronun kuytu köşesinde"
]

enrichers = [
    "adımlarımı yavaşlatıp çevreyi dikkatle inceleyerek",
    "duvarların ardındaki sesleri ayırt etmeye çalışarak",
    "olası çıkış yollarını hesaplayarak",
    "telefon ışığıyla alanı tarayarak",
    "kalabalığı gözleyip güvenlik arayarak",
    "nefesimi düzenleyerek",
    "alarm kaynaklarını kontrol ederek",
    "görevliyle konuşarak",
    "sağduyuyla riskleri küçülterek",
    "yakınlara haber vererek",
    "akılcı bir plan yaparak",
    "yalnızlık hissini bastırmaya çalışarak",
    "adım seslerini dinleyerek",
    "kapıları kontrol ederek",
    "ışıkları açarak",
    "rota değiştirerek",
    "gölgeleri ayırt etmeye çalışarak",
    "kaynak tespiti yaparak",
    "kendimi sakinleştirerek",
    "tehlike senaryolarını elekten geçirerek"
]

noise = [
    "korku, tedirginlik, panik ve huzursuzluk izleri",
    "ürperti ve endişe dalgası",
    "şaşkınlık ve donakalma kırıntıları",
    "stres ve telaş yansımaları",
    "rahatsızlık ve güvensizlik gölgesi",
    "belirsizlik ve kuşku",
    "yorgunlukla karışan tedirginlik",
    "kalp çarpıntısı ve nefes darlığı",
    "alarm duygusu ve panik",
    "birkaç olumsuz ihtimalin tetiklediği huzursuzluk"
]

endings = [
    "dehşete kapıldım ve korktum",
    "ödüm patladı, tedirgin oldum",
    "tehlikeyi sezince ürktüm",
    "belirsizlik büyüyünce korkuya kapıldım",
    "karanlıkta ses duyunca ürperdim",
    "kalbim hızlandı ve korku sardı",
    "adımlarımı yavaşlatıp endişeyle kaçındım",
    "risk görünce çekindim ve korktum",
    "ani hareketle irkildim ve tedirgin oldum",
    "tehdit edilince korku hakim oldu",
    "ne olur ne olmaz diyerek korkmuş kaldım",
    "tehlike ihtimali aklımdan gitmeyince korktum",
    "güvensizlik büyüyünce ürktüm",
    "kuşku artınca tedirgin oldum",
    "çevreyi yoklarken korku hakim oldu",
    "kapı sesleri artınca ürperdim",
    "aniden beliren gölgeyle korktum",
    "yanlış alarm bile içimi ürpertti",
    "tehlike tetikleri zihnimde çoğalınca korktum",
    "yalnızlık hissi büyüyünce tedirgin kaldım"
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
