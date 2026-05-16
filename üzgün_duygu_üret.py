import json
import random

FILE_PATH = r"c:\Users\Enes\Desktop\Yapayzeka Dataset\emotion_data.json"
TARGET = 500
LABEL = "üzgün"

openers = [
    "Sabah tatsız bir mesajla uyanınca içim karardı",
    "Gün içinde beklenmedik aksilikler üst üste binince yoruldum",
    "Toplantıda gereksiz bir çıkış duyunca kafam dağıldı",
    "Arkadaşımla yanlış anlaşılma yüzünden tartışınca kırıldım",
    "Haber beklerken umutlarım sallanınca içim daraldı",
    "Yolda aksilik yaşayıp planlarım bozulunca moralim düştü",
    "Evde gergin bir atmosfer oluşunca içim burkuldu",
    "Kalbim hızlı atarken kötü olasılıklar zihnimi sardı",
    "Geciken dönüşler sabrımı taşırınca huzursuzlaştım",
    "Kötü bir ihtimal aklıma yapışınca keyfim kaçtı",
    "Beklenen destek gelmeyince omuzlarım çöktü",
    "Kırıcı bir söz işitince içim sızladı",
    "Gecikme uzayınca beklentim yerle bir oldu",
    "Sert eleştiriler canımı acıtınca sessizleştim",
    "Bozulan planlar yüzünden yıkıldım",
    "Kafamda karanlık düşünceler dolaşınca hüzün bastı",
    "Sakinlik bozulunca içimde bir çöküş başladı",
    "Yükler ağırlaşınca nefesim daraldı",
    "Olumsuzluklar birikince içim bulandı",
    "Yanlış anlaşılmalar çoğalınca yüreğim sızladı"
]

connectors = [
    "ama ayrıntıları öğrenince tablo bir anda değişti",
    "ancak konuşmanın ilerleyen kısmında yeni bir gerçek ortaya çıktı",
    "fakat perde arkasını duyunca beklenmedik şeyler oldu",
    "gelgelelim başka bir karar alınınca yön değişti",
    "nihayet sakinleşip yeniden düşününce resim netleşti",
    "sonrasında acı bir açıklama gelince duygu ağırlaştı",
    "derken beklediğim destek iptal edilince içim çöktü",
    "akabinde olumsuz bir sonuç bildirilince umut söndü",
    "tam o sırada tatsız bir gelişme duyulunca içim burkuldu",
    "uzun bir konuşmanın ardından hayal kırıklığı belirginleşti"
]

settings = [
    "kalabalık bir durakta",
    "yağmurlu bir akşamüstünde",
    "sessiz bir odada",
    "sıkışık bir trafikte",
    "küçük bir atölyede",
    "ofiste yoğun bir günün sonunda",
    "metroda yol alırken",
    "parkta oturmuşken",
    "evde tek başıma düşünürken",
    "deniz kenarında yürürken",
    "müze koridorlarında",
    "konser bilet kuyruğunda",
    "kitap fuarında",
    "spor salonunda",
    "pazar yerinde kalabalık arasında",
    "havaalanında beklerken",
    "kamp alanında",
    "dağ yolunda",
    "sahil boyunca",
    "hastane koridorunda"
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
    "hassas bir üslup koruyarak",
    "ölçülü bir değerlendirme yaparak",
    "yumuşak bir dille konuşarak",
    "nazikçe hatırlatarak",
    "dengeli bir tutumla",
    "özür bekleyerek",
    "teselli arayarak",
    "umut kırıntılarını ararken",
    "derin bir iç çekişle",
    "yalnızlığın gölgesinde"
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
    "içim burkuldu ve üzüldüm",
    "moralim çöktü ve kederlendim",
    "gözlerim doldu, yüreğim sızladı",
    "beklentilerim yıkıldı ve hüzün çöktü",
    "sessizce içine kapanıp üzüldüm",
    "derin bir iç çekişle üzüntüye kapıldım",
    "umut dağıldı ve kederle kaldım",
    "kalbim kırıldı ve üzüldüm",
    "boşluğa baktım ve içim sızladı",
    "yalnızlık ağırlaştı ve hüzünlendim",
    "dizlerim çözüldü ve hüzne teslim oldum",
    "hatıralar canlanınca hüzün bastı",
    "yanıtlar gecikince keder büyüdü",
    "tatsız sonuca üzülerek boyun eğdim",
    "üst üste gelenlere üzülerek sustum",
    "dayanamadım ve hüzne kapıldım",
    "içimde ince bir sızıyla üzüldüm",
    "beklentim kırılınca kederlendim",
    "içimden bir şeyler koptu ve üzüldüm",
    "yılların yükü çökerken hüzün bastı"
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
