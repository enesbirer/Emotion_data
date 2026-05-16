import json
import random

FILE_PATH = r"c:\Users\Enes\Desktop\Yapayzeka Dataset\emotion_data.json"
TARGET = 500
LABEL = "kızgın"

openers = [
    "Sabah tatsız bir mesajla uyanınca canım sıkıldı",
    "Toplantıda gereksiz bir çıkış duyunca içim daraldı",
    "Yanlış bir ithamla karşılaşınca sinirlerim gerildi",
    "Arkadaşımla anlamsız bir tartışmaya girince huzurum kaçtı",
    "Beklenen teslimat gecikince işler aksadı",
    "Trafikte saygısız bir manevra görünce gerildim",
    "Küçümseyici bir ton duyunca içim kabardı",
    "Mesajlarıma yanıt alamayınca sabrım tükendi",
    "Hak ettiğim saygı verilmediğinde keyfim kaçtı",
    "Haksız bir karar duyunca içim yandı",
    "İş yerinde emeğimin görünmez kılınması canımı sıktı",
    "Yanlı yorumlar havayı zehirleyince içim karardı",
    "Kuralların umursanmaması beni yaraladı",
    "Sorumsuzluk zinciri büyüyünce sabrım taştı",
    "Anlamsız beklemelerle vaktim boşa gidince darlandım",
    "İkiyüzlü tavırlarla karşılaşınca sinirlendim",
    "Hakaret kokan ifadeler duyunca yıkıldım",
    "Sözüm kesilince gerildim",
    "Hataların üzeri örtülünce içim kabardı",
    "Küstah bir ifadeyle karşılaşınca kan beynime sıçradı"
]

connectors = [
    "ama ayrıntı konuşulunca haksızlık daha da görünür oldu",
    "ancak tartışma büyüyünce tansiyon yükseldi",
    "fakat perde arkasındaki ihmaller öğrenilince kanım kaynadı",
    "gelgelelim özür beklerken üstüne bir de pişkinlik yapıldı",
    "nihayet sabrım taşınca tepkimi dile getirmenin zamanı geldi",
    "sonrasında kaba bir tavır takılınca ortam gerildi",
    "derken umursamaz bir yaklaşım sergilenince sinirler hopladı",
    "akabinde üstten konuşulunca kanım çekildi",
    "tam o sırada alaycı bir gülüş görülünce ipler koptu",
    "uzun bir konuşmanın ardından yük daha da ağırlaştı"
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
    "iş çıkışı yorgun argın",
    "market kasasında",
    "bankada işlem sırasındayken",
    "stadyum çevresinde",
    "belediye salonunda",
    "mahalle aralarında"
]

enrichers = [
    "gerçekleri açıkça dile getirerek",
    "kararlı bir sesle haksızlığı göstererek",
    "tutarlı örneklerle sorunu kanıtlayarak",
    "adil ölçütleri hatırlatarak",
    "hak ettiğim saygıyı talep ederek",
    "yerinde ve net bir tepki vererek",
    "sert ama tutarlı bir dille konuşarak",
    "sabır tükendiği için netleşerek",
    "konuyu kişiselleştirmeden ilkelerle anlatarak",
    "yüzleşmekten çekinmeden ifade ederek",
    "özgüvenimi koruyarak",
    "hakkımı arayarak",
    "usulünce uyararak",
    "gerekçeleri sıralayarak",
    "yanlışları tek tek göstererek",
    "tahammül sınırını vurgulayarak",
    "yükü taşıyamadığımı açıklayarak",
    "sözümün kesilmesine itiraz ederek",
    "adaletsizliği işaret ederek",
    "saygı çıtasını hatırlatarak"
]

noise = [
    "öfke, kırgınlık, hayal kırıklığı ve kafa karışıklığı",
    "üzüntü ve pişmanlıkla karışık bir gerginlik dalgası",
    "korku ve huzursuzluk kıvılcımları",
    "şaşkınlık ve donakalma izleri",
    "stres ve telaş yansımaları",
    "iğrenme ve rahatsızlık kırıntıları",
    "tarafsızlık iddiası altında büyüyen kızgınlık",
    "yorgunluk ve bitkinlik gölgesi",
    "kırgınlıkla karışan sitem",
    "haksızlığın tetiklediği gerilim"
]

endings = [
    "çileden çıktım ve çok kızdım",
    "öfkem kabardı, dişlerimi sıktım",
    "sabır taştı ve sinirlendim",
    "haksızlık karşısında öfkeye kapıldım",
    "saygısızlık canımı sıktı ve kızdım",
    "yanlış anlaşılmalar üstüne çıldırdım gibi hissettim",
    "agresif tavra sinirlenip tepki verdim",
    "hakaret duyunca öfkelendim",
    "görmezden gelinince sinirim bozuldu",
    "emeklerim ziyan olunca kızgın kaldım",
    "sözümün hiçe sayılmasına kızdım",
    "tahammül sınırım aşıldı ve öfkelendim",
    "adaletsizlik büyüyünce sinirlendim",
    "umursamazlık karşısında öfkem arttı",
    "küçümseyen tavra kızgın kaldım",
    "hardalı basıp tepki verdim",
    "tonlamadaki kibire sinirlendim",
    "haklı talebim reddedilince kızdım",
    "pişkinliğe dayanamayarak öfkelendim",
    "uyarılarım görmezden gelinince kızgın kaldım"
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
