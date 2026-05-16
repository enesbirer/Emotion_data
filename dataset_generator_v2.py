import json
import random

# Turkish Emotion Dataset Generator V2 - Expanded Vocabulary
# Target: 8 Emotions, 3600 examples each.

EMOTIONS = ["mutlu", "üzgün", "kızgın", "korkmuş", "şaşkın", "iğrenmiş", "nötr", "heyecanlı"]

class TextGenerator:
    def __init__(self):
        self.times = [
            "Sabahın köründe", "Gece yarısı", "Tam evden çıkarken", "Hafta sonu", "Toplantı sırasında", 
            "Yemekten sonra", "Bir anda", "Dün akşam", "Bugün öğle saatlerinde", "Geçen gün",
            "Tam uyumak üzereyken", "Sabah kahvesini içerken", "Yolda yürürken", "Otobüste giderken",
            "Telefon çaldığında", "Kapı açıldığında", "Bilgisayarın başındayken", "Yağmur yağarken"
        ]
        
        # --- VOCABULARY BANKS PER EMOTION ---
        self.banks = {
            "mutlu": {
                "medium_actions": [
                    "gülümsedim", "keyfim yerine geldi", "içim açıldı", "havalara uçtum", "çok beğendim", 
                    "tatmin oldum", "rahatladım", "huzur buldum", "mutluluktan ağladım", "kahkaha attım",
                    "gözlerim parladı", "içim kıpır kıpır oldu", "derin bir oh çektim", "sevince boğuldum",
                    "dünyalar benim oldu", "ayaklarım yerden kesildi", "enerjim tavan yaptı", "mest oldum",
                    "yüzümde güller açtı", "bayıldım", "hayran kaldım", "teşekkür ettim", "şükrettim"
                ],
                "contexts": [
                    "güneş açınca", "maaş yatınca", "sınav iyi geçince", "eski dostu görünce", "kahve kokusunu alınca", 
                    "proje bitince", "tatile çıkınca", "hediye alınca", "güzel bir söz duyunca", "başarıyı yakalayınca",
                    "o şarkıyı duyunca", "deniz kenarına gidince", "çiçekler açınca", "aileyle buluşunca",
                    "uzun zamandır beklediğim haber gelince", "o filmi izleyince", "yeni bir yere gidince",
                    "lezzetli bir yemek yiyince", "maaş zammı alınca", "takdir edilince", "yardım edince"
                ],
                "advanced_imagery": [
                    "gökyüzü daha mavi göründü", "kuşların cıvıltısı bir senfoni gibiydi", "içimde ılık bir rüzgar esti", 
                    "dünya bir anlığına durdu ve gülümsedi", "kalbimde kelebekler dans etti", "ruhuma bahar geldi",
                    "güneş sanki sadece benim için doğdu", "karanlık bulutlar dağıldı", "hayatın renkleri canlandı",
                    "içimdeki buzlar eridi", "zamanın akışı yavaşladı ve güzelleşti", "bir kuş gibi hafifledim",
                    "tüm evrenle bütünleştim sanki", "gözlerimdeki perde kalktı", "melodi gibi aktı zaman"
                ],
                "street": [
                    "kralsın", "on numara beş yıldız", "bomba gibi", "mis gibi", "keyifler gıcır", "daha ne olsun", 
                    "yeme de yanında yat", "ateş ediyor", "efsane olay", "kıyak iş", "miss", "on numara",
                    "tadından yenmez", "lokum gibi", "çiçek gibi", "acayip iyi", "süper ötesi", "mükemmel detay",
                    "bu iş tamamdır", "yüzümüz güldü be", "allah derim", "budur abi"
                ],
                "complex_contrast": [
                    "yorgundum ama değdi", "çok bekledim ama sonucu görünce unuttum", "bittiğine üzüldüm ama yaşandığına sevindim", 
                    "yorucu bir gündü ama şu an huzurluyum", "pahalıydı ama her kuruşuna helal olsun",
                    "korkuyordum ama başarınca rahatladım", "zorlandım ama sonunda başardım",
                    "başta istememiştim ama şimdi iyi ki yapmışım diyorum", "kaybettim sandım ama kazandım"
                ]
            },
            "üzgün": {
                "medium_actions": [
                    "moralim bozuldu", "canım sıkıldı", "gözlerim doldu", "içim burkuldu", "hevesim kaçtı", 
                    "modum düştü", "enerjim bitti", "ağlamak istedim", "boğazım düğümlendi", "yıkıldım",
                    "kahroldum", "üzüntüden uyuyamadım", "sessizliğe gömüldüm", "içime kapandım",
                    "kalbim kırıldı", "hayal kırıklığına uğradım", "gücüm tükendi", "yorgun düştüm",
                    "çaresiz hissettim", "yapayalnız kaldım", "kaybolmuş hissettim"
                ],
                "contexts": [
                    "haber gelmeyince", "telefonu açmayınca", "hava kapanınca", "yalnız kalınca", "eski günleri hatırlayınca", 
                    "başarısız olunca", "veda edince", "reddedilince", "kaybedince", "hata yapınca",
                    "eleştirilince", "unutulunca", "görmezden gelinince", "haksızlığa uğrayınca",
                    "o fotoğrafı görünce", "o mesajı okuyunca", "o sesi duyunca", "o yere gidince",
                    "hasta olunca", "param bitince", "işten çıkarılınca"
                ],
                "advanced_imagery": [
                    "boğazımda koca bir düğüm oluştu", "gökyüzü griye büründü", "dünya üzerime yıkılmış gibi", 
                    "sessizlik kulaklarımı sağır etti", "renkler soldu birden", "içimde bir cam kırığı var sanki",
                    "kalbimin üzerine bir taş oturdu", "ruhsuzca duvara baktım", "gözyaşlarım yağmura karıştı",
                    "karanlık bir kuyuya düşmüş gibiyim", "güneş doğmayı unuttu bugün", "kelimeler boğazımda can verdi",
                    "soğuk bir rüzgar yaladı geçti ruhumu", "zaman durdu ama acı devam etti"
                ],
                "street": [
                    "tadı kaçtı", "sardı yine efkar", "yak bi sigara", "bize gelmez", "kısmet değilmiş", 
                    "yalan oldu", "patladık", "gümledik", "ayvayı yedik", "hapı yuttuk", "bitti o iş",
                    "yıkım ekip", "pert olduk", "yok hükmünde", "canına yandığımın dünyası", "batsın bu dünya",
                    "ciğerimi söktü", "dağıldık abi", "iptal olduk"
                ],
                "complex_contrast": [
                    "gülüyorum ama içim kan ağlıyor", "her şey yolunda gibi ama bir eksik var", 
                    "kalabalıklar içindeyim ama yapayalnızım", "gitmesini istedim ama şimdi özlüyorum",
                    "doğru olan bu biliyorum ama canım yanıyor", "unutmaya çalışıyorum ama her yerde onu görüyorum",
                    "güçlü durmaya çalışıyorum ama dağılmak üzereyim", "bitti dedim ama içimde bitmedi"
                ]
            },
            "kızgın": {
                "medium_actions": [
                    "sinirlendim", "deliye döndüm", "tepem attı", "sabrım taştı", "çileden çıktım", 
                    "öfkelendim", "gerildim", "bağırdım", "patladım", "köpürdüm", "ateş püskürdüm",
                    "gözüm döndü", "elim ayağım titredi", "dişlerimi sıktım", "yumruğumu sıktım",
                    "tahammül edemedim", "isyan ettim", "karşı çıktım", "kavga ettim", "tersledim"
                ],
                "contexts": [
                    "yalan söylenince", "bekletilince", "haksızlık yapılınca", "trafik sıkışınca", "internet kesilince", 
                    "işler aksayınca", "saygısızlık görünce", "sıramı çalınca", "gürültü yapılınca",
                    "sözünde durmayınca", "dalga geçilince", "emir verilince", "suçlanınca",
                    "iftira atılınca", "eşyam kırılınca", "yemeğim geç gelince", "hatalı ürün gelince",
                    "iptal edilince", "kandırılınca", "oyalanınca"
                ],
                "advanced_imagery": [
                    "beynimden vurulmuşa döndüm", "damarlarımdaki kan çekildi", "gözüm döndü resmen", 
                    "ateş püskürdüm", "bir volkan gibi patlamak üzereyim", "sabır taşım çatladı",
                    "içimdeki canavar uyandı", "gözlerimden şimşekler çaktı", "kulaklarımdan duman çıktı",
                    "sakinliğimi korumak imkansızlaştı", "öfke bir zehir gibi yayıldı vücuduma",
                    "barut fıçısına döndüm", "kelimeler mermi gibi döküldü ağzımdan"
                ],
                "street": [
                    "ayar oldum", "fitil oldum", "tepe tasımı attırma", "asabımı bozma", "delirtme adamı", 
                    "bu neyin kafası", "çizgiyi aşma", "kafayı yicem", "bu ne lahana turşusu",
                    "ağzımı bozdurma", "dalgana bak", "artistlik yapma", "işine bak", "canımı sıkma",
                    "olay çıkartırım", "kıl oldum", "gıcık kaptım", "dellendim"
                ],
                "complex_contrast": [
                    "seviyorum ama bu yaptığı kabul edilemez", "haklısın diyorum ama içten içe köpürüyorum", 
                    "sakin kalmaya çalışıyorum ama ellerim titriyor", "susuyorum ama fırtına kopacak",
                    "önemsemiyormuş gibi yapıyorum ama çıldırıyorum", "anlamaya çalışıyorum ama mantığım almıyor",
                    "zarar vermek istemiyorum ama zorluyorlar", "gülümsüyorum ama sabrım tükendi"
                ]
            },
            "korkmuş": {
                "medium_actions": [
                    "ürperdim", "titredim", "dondum kaldım", "panikledim", "endişelendim", 
                    "çekindim", "tedirgin oldum", "korkudan ölecektim", "nefesim kesildi",
                    "kalbim duracak sandım", "rengim attı", "soğuk ter döktüm", "kaçmak istedim",
                    "saklandım", "yardım istedim", "çığlık attım", "gözlerimi kapattım"
                ],
                "contexts": [
                    "ses duyunca", "elektrikler gidince", "tek başıma kalınca", "bilinmeyen numara arayınca", 
                    "gölge görünce", "köpek havlayınca", "fırtına çıkınca", "deprem olunca",
                    "takip edildiğimi hissedince", "kapı zorlanınca", "çığlık duyunca", "silah görünce",
                    "kaybolunca", "karanlık sokakta", "asansörde kalınca", "uçak sallanınca"
                ],
                "advanced_imagery": [
                    "kalbim yerinden fırlayacak gibiydi", "soğuk terler döktüm", "nefesim kesildi", 
                    "ayaklarım geri geri gitti", "kanım dondu", "dehşetin soğuk nefesini ensemde hissettim",
                    "göz bebeklerim büyüdü", "bacaklarımın bağı çözüldü", "kelimeler boğazımda düğümlendi",
                    "karanlık beni yutacak gibiydi", "ölüm sessizliği çöktü", "bir karabasan gibi üzerime çöktü"
                ],
                "street": [
                    "ödüm patladı", "yusuf yusuf oldum", "aklım çıktı", "tırstım", "elim ayağıma dolaştı", 
                    "kalbe iniyordu", "fenalık geldi", "altıma yapıyordum", "yüreğim ağzıma geldi",
                    "feleğim şaştı", "nutkum tutuldu", "tırstım abi", "korkudan bayılacaktım",
                    "bittim ben", "gözüm karardı"
                ],
                "complex_contrast": [
                    "merak ediyorum ama bakmaya cesaretim yok", "gitmem lazım ama ayaklarım gitmiyor", 
                    "güvendiğim bir yer ama yine de tedirginim", "her şey normal görünüyor ama içimde kötü bir his var",
                    "cesur olmaya çalışıyorum ama titriyorum", "kaçmak istiyorum ama donup kaldım",
                    "biliyorum bir şey yok ama yine de korkuyorum"
                ]
            },
            "şaşkın": {
                "medium_actions": [
                    "şok oldum", "şaşırdım", "inanamadım", "kalakaldım", "nutkum tutuldu", 
                    "beklemiyordum", "hayret ettim", "donup kaldım", "ağzım açık kaldı",
                    "gözlerime inanamadım", "tepki veremedim", "şaşkına döndüm", "afalladım",
                    "dumur oldum", "hayrete düştüm", "küçük dilimi yuttum"
                ],
                "contexts": [
                    "birden karşıma çıkınca", "sonucu görünce", "gerçeği öğrenince", "fiyatı duyunca", 
                    "o haberi alınca", "değişimi fark edince", "tesadüfü görünce", "kazandığımı öğrenince",
                    "eski sevgiliyi görünce", "o değişikliği yapınca", "aniden olunca", "beklenmedik misafir gelince",
                    "sırrı öğrenince", "yalanı ortaya çıkınca", "hediyeyi açınca"
                ],
                "advanced_imagery": [
                    "gözlerime inanamadım", "beynim durdu sanki", "rüya görüyorum sandım", 
                    "yer ayağımın altından kaydı", "algılarım kapandı bir an", "gerçeklik algım sarsıldı",
                    "zaman dondu sanki", "bütün bildiklerim yalanmış gibi", "bir film sahnesi gibiydi",
                    "mantığım devre dışı kaldı", "hayal ile gerçek birbirine karıştı"
                ],
                "street": [
                    "hadi canım", "yok artık", "şaka yapıyorsun", "nasıl yani", "olaya gel", 
                    "bak sen şu işe", "vay be", "ohaa", "yuh", "hass", "ciddi misin",
                    "dalga geçiyorsun", "bırak bu işleri", "inanamıyorum abi", "olay var"
                ],
                "complex_contrast": [
                    "biliyordum desem yalan olur ama tahmin de ettim", "bekliyordum ama bu kadarını değil", 
                    "hem tanıdık hem çok yabancı", "imkansız ama gerçek", "görüyorum ama inanamıyorum",
                    "mantıksız ama oluyor", "hem şaşırdım hem sevindim", "kızsam mı şaşırsam mı bilemedim"
                ]
            },
            "iğrenmiş": {
                "medium_actions": [
                    "midem bulandı", "tiksindim", "içim kalktı", "rahatsız oldum", "öğürdüm", 
                    "yüzümü buruşturdum", "uzaklaştım", "kusacak gibi oldum", "iğrendim",
                    "tahammül edemedim", "bakımdan kaçındım", "gözlerimi çevirdim",
                    "burnumu tıkadım", "elimi sürmedim", "yemekten kesildim"
                ],
                "contexts": [
                    "yemeğin içinden çıkınca", "o kokuyu duyunca", "çöpleri görünce", "yapış yapış olunca", 
                    "küflenmiş olduğunu fark edince", "hijyen olmayınca", "bakımsız görünce", "ter kokusu gelince",
                    "böcek görünce", "kirli tuvaleti görünce", "çürümüş meyveyi görünce", "salyangoz görünce",
                    "kıl görünce", "leke görünce", "kötü söz duyunca"
                ],
                "advanced_imagery": [
                    "genzimi yakan o koku", "bakmaya bile tahammül edemedim", "bütün iştahım kaçtı", 
                    "sanki zehirlenmiş gibi hissettim", "üzerime yapışan o kirli his", "midem ağzıma geldi",
                    "boğazıma acı bir su yükseldi", "görüntü zihnime kazındı", "kirlenmiş hissettim",
                    "tüm vücudum tepki verdi", "o anı silmek istedim hafızamdan"
                ],
                "street": [
                    "ıyy", "bu ne be", "içim dışıma çıktı", "kuscam şimdi", "leş gibi", 
                    "adamı hasta eder", "görmemiş olayım", "öğk", "iğrenç ötesi",
                    "midem kaldırmadı", "bu ne pislik", "rezalet kepazelik", "kusmuk gibi"
                ],
                "complex_contrast": [
                    "lezzetli görünüyor ama o koku her şeyi bitirdi", "temizlemeye çalıştım ama dokunamadım bile", 
                    "sevdiğim bir yerdi ama bu görüntüden sonra bitti", "güzelliğine aldanma içi çürümüş",
                    "bakmak istemiyorum ama gözüm kayıyor", "mecburum ama midem almıyor"
                ]
            },
            "nötr": {
                "medium_actions": [
                    "fark etmez", "olabilir", "bakarız", "tamamdır", "sorun yok", 
                    "devam ettim", "bekliyorum", "izledim", "dinledim", "onayladım",
                    "kabul ettim", "geçtim", "yürüdüm", "oturdum", "kalktım"
                ],
                "contexts": [
                    "sabah uyanınca", "yolu izlerken", "market sırasında", "dosyaları düzenlerken", 
                    "haberleri okurken", "otobüs beklerken", "kahve içerken", "toplantıda",
                    "televizyon izlerken", "kitap okurken", "yemek yerken", "yürüyüş yaparken",
                    "asansör beklerken", "trafik ışığında", "banka sırasında"
                ],
                "advanced_imagery": [
                    "saatin tik takları dışında ses yok", "her şey olması gerektiği gibi", "durağan bir gün", 
                    "ne eksik ne fazla", "akışına bıraktım", "rutin bir sessizlik", "zaman yavaşça akıyor",
                    "her şey yerli yerinde", "sıradanlığın huzuru", "düz bir çizgi gibi hayat"
                ],
                "street": [
                    "fark yapmaz", "bana uyar", "sıkıntı yok", "aynı tas aynı hamam", "bildiğin gibi", 
                    "rutin işler", "yuvarlanıp gidiyoruz", "standart", "devam", "aynen",
                    "napalım işte", "öyle böyle", "idare eder"
                ],
                "complex_contrast": [
                    "iyi desem değil kötü desem değil", "ne sevindim ne üzüldüm", "kararsız kaldım ama sonra boşverdim", 
                    "önemli gibi duruyor ama beni etkilemedi", "herkes panik ama ben sakinim",
                    "olay büyük ama benim ilgimi çekmedi"
                ]
            },
            "heyecanlı": {
                "medium_actions": [
                    "sabırsızlanıyorum", "yerimde duramıyorum", "kalbim pır pır", "can atıyorum", 
                    "hazırladım", "bekliyorum", "koştum", "uçtum", "sevindim", "coştum",
                    "harekete geçtim", "başladım", "atıldım", "gülümsedim"
                ],
                "contexts": [
                    "yola çıkarken", "konser başlarken", "maç saatinde", "sahneye çıkmadan", 
                    "sonucu beklerken", "yeni işe başlarken", "sürpriz yaparken", "tatile giderken",
                    "sevgiliyle buluşurken", "uçağa binerken", "ödül alırken", "yarışmaya katılırken",
                    "o an gelince", "kapı çalınca", "telefon çalınca"
                ],
                "advanced_imagery": [
                    "adrenalin damarlarımda dolaşıyor", "nefesim hızlandı", "gözlerim parlıyor", 
                    "enerjim taşıyor", "zaman geçmek bilmiyor", "içim içime sığmıyor",
                    "kalbim göğsümü dövüyor", "elektrik çarpmış gibiyim", "gökyüzünde uçuyor gibiyim",
                    "bütün hücrelerim uyandı", "hayat damarlarımda akıyor"
                ],
                "street": [
                    "kopuyoruz", "uçuşa geçtik", "fena gaza geldim", "yerimizde duramıyoruz", 
                    "ateş ediyor", "ortam yanıyor", "sabahlar olmasın", "coşuyoruz",
                    "yıkılıyor", "koptu gidiyor", "tutmayın beni", "dehşetül vahşet"
                ],
                "complex_contrast": [
                    "korkuyorum ama denemek istiyorum", "ellerim titriyor ama hazırım", 
                    "uykum var ama heyecandan uyuyamıyorum", "riskli ama buna değer",
                    "sonu ne olur bilmem ama başlıyorum", "delilik belki ama yapacağım",
                    "herkes dur diyor ben koşuyorum"
                ]
            }
        }
    
    def get_template(self, level, emotion):
        if level == "medium": return self.gen_medium(emotion)
        elif level == "med_adv": return self.gen_med_adv(emotion)
        elif level == "advanced": return self.gen_advanced(emotion)
        elif level == "adv_long": return self.gen_adv_long(emotion)
        elif level == "complex": return self.gen_complex(emotion)
        elif level == "implicit": return self.gen_implicit(emotion)

    def gen_medium(self, emotion):
        bank = self.banks[emotion]
        t = random.choice(self.times)
        c = random.choice(bank["contexts"])
        a = random.choice(bank["medium_actions"])
        
        structures = [
            f"{t} {c}, {a}.", f"{c} gerçekten {a}.", f"{self.capitalize(a)}, çünkü {c}.",
            f"{t} {self.capitalize(a)}.", f"Bu durum karşısında {a}.", f"{c} ve {a}.",
            f"{self.capitalize(c)}, {a}."
        ]
        return random.choice(structures)

    def gen_med_adv(self, emotion):
        bank = self.banks[emotion]
        c = random.choice(bank["contexts"])
        a = random.choice(bank["medium_actions"])
        img = random.choice(bank["advanced_imagery"])
        t = random.choice(self.times)
        
        structures = [
            f"{c} ne yapacağımı bilemedim, sonuçta {a}.",
            f"Olaylar gelişirken {img}, sonunda {a}.",
            f"Her ne kadar beklesem de {c}, {a}.",
            f"{self.capitalize(img)}, çünkü {c}.",
            f"{c} ve bu yüzden {a}.",
            f"{t} {c}, hissettiğim şey şuydu: {a}.",
            f"{c} olmasına rağmen {a}, garip bir durum."
        ]
        return random.choice(structures)

    def gen_advanced(self, emotion):
        bank = self.banks[emotion]
        img = random.choice(bank["advanced_imagery"])
        c = random.choice(bank["contexts"])
        intros = ["Sanki", "Adeta", "Bildiğin", "Hissettim ki", "Fark ettim ki", "Anladım ki"]
        intro = random.choice(intros)
        
        structures = [
            f"{c} {img}.",
            f"{intro} {img}, kelimeler kifayetsiz kaldı.",
            f"{self.capitalize(img)}, tüm dünya sessizliğe büründü.",
            f"Gözlerimi kapattım ve {img}.",
            f"O an {c}, {img}.",
            f"{self.capitalize(img)} ve zaman durdu.",
            f"{c} anında {img}."
        ]
        return random.choice(structures)

    def gen_adv_long(self, emotion):
        bank = self.banks[emotion]
        img = random.choice(bank["advanced_imagery"])
        c = random.choice(bank["contexts"])
        a = random.choice(bank["medium_actions"])
        t = random.choice(self.times)
        
        sentences = [
            f"{t} her şey sıradan görünüyordu.",
            f"Ancak {c} bir anda atmosfer değişti.",
            f"{self.capitalize(img)}.",
            f"Derin bir nefes aldım ve {a}.",
            "Bu anı asla unutmayacağım."
        ]
        
        if random.random() > 0.5: return " ".join(sentences)
        else: return " ".join(sentences[1:])

    def gen_complex(self, emotion):
        bank = self.banks[emotion]
        contrast = random.choice(bank["complex_contrast"])
        structures = [
            f"{contrast}, ne hissedeceğimi şaşırdım.",
            f"İçimde bir savaş var sanki; {contrast}.",
            f"Bir yanım git diyor, diğer yanım kal; {contrast}.",
            f"{contrast}.",
            f"Karmaşık duygular içindeyim, {contrast}."
        ]
        return random.choice(structures)

    def gen_implicit(self, emotion):
        bank = self.banks[emotion]
        s = random.choice(bank["street"])
        c = random.choice(bank["contexts"])
        structures = [
            f"{c} dedim ki: {s}!", f"{s}, başka söze gerek yok.",
            f"Abi {s} ya, inanamıyorum.", f"{c} resmen {s}.",
            f"Durum şu: {s}.", f"{s} yani, anlarsın ya.",
            f"Hani derler ya {s}, aynen öyle."
        ]
        return random.choice(structures)

    def capitalize(self, s):
        if not s: return ""
        return s[0].upper() + s[1:]

def generate_full_dataset():
    gen = TextGenerator()
    dataset = []
    
    distribution = {
        "medium": 700,
        "med_adv": 700,
        "advanced": 700,
        "adv_long": 700,
        "complex": 400,
        "implicit": 400
    }
    
    for emotion in EMOTIONS:
        print(f"Generating for {emotion}...")
        for level, count in distribution.items():
            generated_texts = set()
            attempts = 0
            # Increase attempt limit to find unique combinations
            while len(generated_texts) < count and attempts < count * 20:
                text = gen.get_template(level, emotion)
                if text not in generated_texts:
                    generated_texts.add(text)
                attempts += 1
            
            for text in generated_texts:
                dataset.append({
                    "text": text,
                    "label": emotion
                })
                
    return dataset

if __name__ == "__main__":
    old_file_path = "c:\\Users\\Enes\\Desktop\\Yeni klasör\\emotion_data.json"
    new_data = generate_full_dataset()
    final_dataset = []
    
    try:
        with open(old_file_path, "r", encoding="utf-8") as f:
            old_data = json.load(f)
        
        if isinstance(old_data, dict):
            for emotion, texts in old_data.items():
                for t in texts:
                    final_dataset.append({"text": t, "label": emotion})
        elif isinstance(old_data, list):
            final_dataset.extend(old_data)
            
    except FileNotFoundError:
        print("Existing file not found, creating new one.")
    
    final_dataset.extend(new_data)
    random.shuffle(final_dataset)
    
    with open(old_file_path, "w", encoding="utf-8") as f:
        json.dump(final_dataset, f, ensure_ascii=False, indent=2)
        
    print(f"Total records: {len(final_dataset)}")
