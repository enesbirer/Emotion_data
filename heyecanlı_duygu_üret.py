import json
import random

FILE_PATH = r"c:\Users\Enes\Desktop\Yapayzeka Dataset\emotion_data.json"
TARGET = 500
LABEL = "heyecanlı"

openers = [
    "Gün uzun bekleyişlerle geçti ve sabrım zorlandı",
    "Sonuç belirsiz kaldıkça içimde gerilim birikti",
    "Planlar değişip durunca kafam karıştı",
    "Akış bir türlü netleşmeyince huzursuz oldum",
    "Tuhaf sessizlik içinde kalınca rahatsızlandım",
    "Yanıt gecikince sabırsızlık arttı",
    "Sürpriz var dendi ama açıklama yapılmayınca kıvrandım",
    "Hazırlıklar aksayınca endişe büyüdü",
    "Saatler uzadıkça merak coştu ama gerginlik de arttı",
    "Kalbim hızlanırken kötü ihtimalleri düşündüm"
]

connectors = [
    "ama kapı aralanınca sürprizin işareti göründü",
    "ancak perde arkasındaki hazırlık günyüzüne çıkınca tablo değişti",
    "fakat sahneye dair yeni bilgi gelince akış hızlandı",
    "gelgelelim beklenen an yaklaşınca heyecan dalgası yükseldi",
    "nihayet telafi planı açıklandı ve umut arttı",
    "sonrasında müjde duyurulunca içimde enerji patladı",
    "derken zil çalınca bekleyiş bitti",
    "akabinde son prova başlayınca atmosfer ısındı",
    "tam o sırada perde açılınca nefesler tutuldu",
    "uzun bir hazırlığın ardından an geldi"
]

settings = [
    "konser salonunda",
    "tiyatro sahnesi önünde",
    "stadyumda",
    "kamp alanında",
    "festival girişinde",
    "müze avlusunda",
    "okul sahnesinde",
    "atölyede",
    "laboratuvarda",
    "stüdyoda",
    "ofiste",
    "metroda",
    "parkta",
    "sahil boyunca",
    "dağ yamacında",
    "pazar yerinde",
    "havaalanında",
    "kütüphane salonunda",
    "sergi açılışında",
    "yolculuk öncesi"
]

enrichers = [
    "ritmi içimde büyüterek",
    "adımlarımı hızlandırarak",
    "nefesimi düzenleyerek",
    "gözlerimi ışığa dikerek",
    "kalbimin sesini dinleyerek",
    "hazırlıkları koordine ederek",
    "planı kusursuzlaştırmaya çalışarak",
    "enerjiyi diri tutarak",
    "heyecanın dengesini korumaya çalışarak",
    "umut kıvılcımını besleyerek",
    "an'a odaklanarak",
    "zamanı kollayarak",
    "detayları tamamlayarak",
    "grup uyumunu sağlayarak",
    "müjdeye kulak kesilerek",
    "göz göze gelerek",
    "adrenalin yükselterek",
    "kıpır kıpır hislerle",
    "tatlı telaşla",
    "anlatı akışını hızlandırarak"
]

noise = [
    "heyecan, stres, telaş ve sabırsızlık kıvılcımları",
    "merak dalgası ve gerilim",
    "umut ve kuşku karışımı",
    "adrenalin ve bekleyiş",
    "coşku ile endişe yan yana",
    "ritim ve kalp atışı",
    "nefes kontrolü ve titreşim",
    "hareket ve çağrı",
    "tempo ve ışık oyunları",
    "sahnede dolaşan fısıltılar"
]

endings = [
    "yerimde duramadım ve heyecanlandım",
    "nefesim hızlandı, içimi kıpır kıpır bir heyecan sardı",
    "kalbim atışlarını duyup heyecanla bekledim",
    "iyi ihtimal büyüyünce heyecana kapıldım",
    "müjdeyle heyecan tavan yaptı",
    "adrenalin yükseldi ve heyecandan titredim",
    "sahneye çıkarken heyecanla kıvranıp sevindim",
    "umut açılınca heyecandan yüzüm güldü",
    "final yaklaşınca heyecanla hazırlandım",
    "bekleyiş uzayınca tatlı bir heyecanla doldum",
    "ışıklar yanınca heyecandan yerimde duramadım",
    "ilk notayla heyecan fışkırdı",
    "kalabalığın coşkusuyla heyecanlandım",
    "son an duyurusunda heyecan arttı",
    "başlangıç gonguyla heyecana kapıldım",
    "kafile hareket edince heyecanla hızlandım",
    "adımlar senkron olunca heyecan çoğaldı",
    "tempo yükselince heyecan sardı",
    "provadan sahneye geçince heyecan doldu",
    "müjdeyle içime heyecan yayıldı"
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
