import json
import random

FILE_PATH = r"c:\Users\Enes\Desktop\Yapayzeka Dataset\emotion_data.json"
TARGET = 500
LABEL = "mutlu"

openers = [
    "Bugün planlarım darmadağın oldu ve üzerimde ağır bir baskı vardı",
    "Sabah tatsız bir mesajla uyanınca içim karardı",
    "Toplantıda gerilim yükselince kafam karıştı ve moralim bozuldu",
    "Yolda beklenmedik bir aksaklık yaşayınca sinirlerim gerildi",
    "Kalbim gümbür gümbür atarken kötü bir haber alacağımı sandım",
    "Arkadaşımla sert bir tartışmaya tutuşunca içim karardı",
    "İşler ters gidince umutsuzluğa kapıldım ve omuzlarım çöktü",
    "Evde birikmiş sorunlar üst üste binince huzursuzluk sardı",
    "Şehir gürültüsü ve kalabalık içinde başım ağrıyınca daraldım",
    "Belirsizlik büyüdükçe endişe ve pişmanlık iç içe geçti",
    "Kafamda bin bir soru dönüp dururken huzursuzlaştım",
    "Bir yanlış anlaşılma yüzünden kırgınlık içimde büyüdü",
    "Uzayan bekleyiş sabrımı zorlayınca gerildim",
    "Yetersiz hissettiğim anlar üst üste gelince içim burkuldu",
    "Kötü olasılıklar zihnimi meşgul ederken keyfim kaçtı",
    "Sert bir eleştiri moralimi yerle bir etti",
    "Tuhaf bir sessizlik içinde endişe büyüdü",
    "Telaşlı bir tempo nefesimi daralttı",
    "Yanlış giden ayrıntılar canımı sıktı",
    "Gün boyu üzerimde ağır bir yorgunluk vardı"
]

connectors = [
    "ama ayrıntıları öğrenince tablo değişti",
    "ancak konuşmanın ilerleyen kısmında gerçek ortaya çıktı",
    "fakat olayın perde arkasını duyunca bakışım farklılaştı",
    "gelgelelim yapıcı bir öneri gelince her şey dönüştü",
    "nihayet sakinleşip yeniden değerlendirme yapınca umut belirdi",
    "sonrasında barışçıl bir yaklaşım benimsendi ve hava yumuşadı",
    "derken beklenmedik bir esneklik gösterildi ve ortam gevşedi",
    "akabinde olumlu bir geri bildirim alınca nefesim rahatladı",
    "tam o sırada müjdeli haber ulaşınca içim hafifledi",
    "uzun bir konuşmanın ardından uzlaşma zemini oluştu",
    "sonra tatlı bir sürpriz kapıyı çalınca duygu değişti",
    "akşamüstü sevindiren bir açıklama gelince her şey aydınlandı",
    "ekipçe destek verilince tablo netleşti",
    "karşı taraf özür dileyince hava tatlıya bağlandı",
    "yapılan jest içimi ısıtınca umut büyüdü"
]

settings = [
    "kalabalık bir kafede",
    "yağmurlu bir akşamüstünde",
    "sessiz bir kütüphanede",
    "sıkışık bir trafikte",
    "şehir dışındaki küçük bir kasabada",
    "ofiste yoğun bir günün sonunda",
    "metroda yol alırken",
    "parkta oturmuşken",
    "evde tek başıma düşünürken",
    "deniz kenarında yürürken",
    "müze koridorlarında",
    "konser bilet kuyruğunda",
    "kitap fuarında",
    "spor salonunda",
    "atölyede çalışırken",
    "pazar yerinde kalabalık arasında",
    "havaalanında beklerken",
    "kamp alanında",
    "dağ yolunda",
    "sahil boyunca"
]

enrichers = [
    "empati kurup farklı bakış açılarını dinleyerek",
    "kanıtları serinkanlılıkla tartarak",
    "kelimeleri özenle seçerek",
    "duyguları ayıklayıp verileri önceliklendirmeye çalışarak",
    "gerçekçi bir çerçeve kurarak",
    "mantıklı çıkarımlar yaparak",
    "hafızamdaki benzer olaylarla kıyaslayarak",
    "geçmiş tecrübelerimi hatırlayarak",
    "iç sesimi dinleyip dış sesleri süzerek",
    "sabırla ayrıntılara ışık tutarak",
    "naif bir umut tohumu besleyerek",
    "özgüvenimi tazeleyerek",
    "dengeli bir üslup koruyarak",
    "şefkatli bir dil kurarak",
    "dayanışmayı önceleyerek",
    "üstüne bir de sürpriz bir destek gelince",
    "ikna edici gerekçelerle",
    "akılcı bir plan yaparak",
    "güzel bir haberin etkisiyle",
    "tatlı bir jestle"
]

noise = [
    "üzüntü, endişe, pişmanlık ve gerginlik dalgası",
    "öfke, kırgınlık, hayal kırıklığı ve kafa karışıklığı",
    "korku, tedirginlik, panik ve huzursuzluk izleri",
    "şaşkınlık, hayret, afallama ve donakalma hissi",
    "heyecan, stres, telaş ve sabırsızlık kıvılcımları",
    "iğrenme, tiksinti ve rahatsızlık yankıları",
    "nötr bir bakışla süzülen tarafsızlık izi",
    "belirsiz umut kırıntıları ile karışan duygular",
    "yorgunluk ve bitkinlik gölgesi",
    "gözyaşı ile karışan kırgınlık"
]

endings = [
    "tatlıya bağladık ve içim mutlulukla doldu",
    "kahkaha attık ve sevindim",
    "rahat bir nefes aldım ve yüzüm güldü",
    "iyi haberle sevince boğuldum",
    "umut büyüdü ve mutlu oldum",
    "kalbim hafifledi, sevinçle gülümsedim",
    "içten bir teşekkür aldım ve sevindim",
    "dayanışma kazandı, mutlu hissettim",
    "sıcak bir sarılmayla mutlu sona ulaştık",
    "barışıp helalleştik ve içim neşeyle doldu",
    "müjdeyi alınca mutluluk taşırdım",
    "iyi sürprizle sevincim katlandı",
    "gülüşler yükseldi ve mutluluk belirginleşti",
    "içimi coşku kapladı ve sevindim",
    "şefkatli yaklaşım sayesinde mutlu oldum",
    "tatlı bir espri ortamı yumuşattı ve sevindim",
    "samimi bir özürle içim ısındı ve mutlu oldum",
    "iyi niyet kazanıp sevindim",
    "huzur yayıldı ve yüzüm güldü",
    "barış çabası sonuç verdi ve sevindim"
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
