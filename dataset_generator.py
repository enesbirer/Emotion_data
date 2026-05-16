import json
import random

# Turkish Emotion Dataset Generator

def generate_dataset():
    # ---------------------------------------------------------
    # DATA POOLS
    # ---------------------------------------------------------
    
    # Common subjects and objects
    subjects = ["Bu ürün", "Aldığım hizmet", "Gelen paket", "Müşteri temsilcisi", "Sonuç", "Yaşananlar", "Bu durum", "Arkadaşımın tavrı", "Filmin sonu", "Yediğim yemek"]
    time_markers = ["dün", "bugün", "geçen hafta", "sabah saatlerinde", "akşamüzeri"]
    
    # ---------------------------------------------------------
    # 1. MUTLU (HAPPY)
    # ---------------------------------------------------------
    mutlu_medium_templates = [
        "{subj} gerçekten harikaydı, çok mutlu oldum.",
        "{subj} beklentimin çok üzerindeydi, teşekkürler.",
        "{subj} yüzümü güldürdü, harika bir deneyimdi.",
        "Hayatımda gördüğüm en iyi {noun} diyebilirim, çok sevindim.",
        "{subj} sayesinde günüm aydınlandı.",
        "İnanılmaz derecede memnun kaldım, {subj} süperdi.",
        "{subj} beni çok neşelendirdi.",
        "Kesinlikle tekrar tercih edeceğim, {subj} muhteşemdi.",
        "Her şey tam istediğim gibi oldu, mutluluktan uçuyorum.",
        "{subj} o kadar güzel ki anlatamam."
    ]
    
    mutlu_med_adv_templates = [
        "Başta tereddüt etmiştim ama {subj} beni yanıltarak çok mutlu etti.",
        "{time} yaşadığım olumsuzluklara rağmen {subj} moralimi düzeltti.",
        "Uzun zamandır aradığım kaliteyi {subj} ile buldum, çok memnunum.",
        "{subj} detaylarına bayıldım, insanı özel hissettiriyor.",
        "Her kuruşuna değdi, {subj} beni benden aldı diyebilirim.",
        "{subj} beklediğimden biraz geç geldi ama performansı o kadar iyi ki çok mutluyum.",
        "Sadece {subj} değil, sunulan ilgi ve alaka da beni çok memnun etti.",
        "Böylesine özenli bir {noun} ile karşılaşmak beni gerçekten sevindirdi.",
        "Zor bir gün geçiriyordum ki {subj} imdadıma yetişti ve beni gülümsetti.",
        "{subj} konusunda şüphelerim vardı fakat sonuç mükemmel oldu."
    ]
    
    mutlu_advanced_templates = [
        "Pencereden süzülen güneş ışığı gibi içimi ısıtan bir haber aldım, tarif edilemez bir huzur kapladı her yanımı.",
        "Yıllardır görmediğim bir dostumla karşılaşmışçasına içten bir sevinç dalgası yayıldı tüm bedenime.",
        "Emeğimin karşılığını nihayet aldığım o an, omuzlarımdan koca bir yükün kalktığını hissettim.",
        "Odanın içindeki atmosfer bir anda değişti, herkesin gözlerindeki parıltı bana her şeyin yolunda olduğunu fısıldıyordu.",
        "Sabahın erken saatlerinde denizin o sakin maviliğine bakarken hissettiğim o dinginlik paha biçilemezdi.",
        "Küçük bir jestin dünyaları değiştirebileceğini o an anladım, kalbimde kelebekler uçuşmaya başladı.",
        "Başardığımı gördüğümde kelimeler boğazımda düğümlendi, sadece derin bir nefes alıp anın tadını çıkardım.",
        "O sahneyi izlerken dudaklarımın kenarında istemsiz bir tebessüm belirdi, içim kıpır kıpır oldu.",
        "Sanki bahar gelmiş de her yer çiçek açmış gibi, içimde yeni umutlar yeşerdi.",
        "Gökyüzüne baktığımda bulutların arasından sızan ışık, bana her şeyin çok güzel olacağını müjdeliyordu."
    ]

    # ---------------------------------------------------------
    # 2. ÜZGÜN (SAD)
    # ---------------------------------------------------------
    uzgun_medium_templates = [
        "{subj} beni gerçekten çok üzdü.",
        "Beklediğim gibi olmadı, {subj} hayal kırıklığı yarattı.",
        "{subj} yüzünden moralim bozuldu.",
        "Maalesef {subj} hiç hoşuma gitmedi, üzücü.",
        "{subj} kalbimi kırdı.",
        "Keşke {subj} böyle olmasaydı, üzgünüm.",
        "{subj} beni derinden yaraladı.",
        "Sonuç hüsran oldu, {subj} kötüydü.",
        "{subj} ile ilgili yaşadığım sorun canımı sıktı.",
        "Böyle bir {noun} beklemiyordum, çok yazık."
    ]
    
    uzgun_med_adv_templates = [
        "{subj} için çok heveslenmiştim ama sonuç tam bir hayal kırıklığı oldu.",
        "Elimden geleni yapmama rağmen {subj} istediğim gibi sonuçlanmadı, üzgünüm.",
        "{subj} o kadar kötüydü ki bütün hevesim kursağımda kaldı.",
        "Ne yazık ki {subj} beklentilerimin çok altında kaldı ve beni üzdü.",
        "Olayların bu noktaya gelmesi {subj} nedeniyle beni gerçekten yıprattı.",
        "Güzel başlayan günüm {subj} yüzünden hüzünlü bitti.",
        "{subj} konusunda daha hassas olunmasını beklerdim, kırıldım.",
        "İyi niyetimin karşılığı bu olmamalıydı, {subj} beni üzdü.",
        "{subj} deneyimim maalesef gözyaşıyla bitti.",
        "Büyük umutlarla başladığım iş {subj} yüzünden hüsranla sonuçlandı."
    ]
    
    uzgun_advanced_templates = [
        "Odaya girdiğimde hissettiğim o ağır hava, boğazımda bir yumru oluşmasına neden oldu, yutkunamadım.",
        "Gözlerimden süzülen yaşlara engel olamıyordum, içimde kocaman bir boşluk vardı sanki.",
        "Her şeyin bittiğini anladığım o an, dünyam başıma yıkılmış gibi hissettim.",
        "Pencereden dışarıdaki yağmuru izlerken, gökyüzünün de benimle ağladığını düşündüm.",
        "Eski fotoğraflara bakarken içimden bir parçanın koptuğunu hissettim, geri gelmeyecek anılar canımı yaktı.",
        "Sessizlik o kadar gürültülüydü ki, yalnızlığımın çığlıklarını bastırıyordu.",
        "Kalbimdeki ağırlık her geçen saniye daha da artıyor, nefes almamı zorlaştırıyordu.",
        "Bir zamanlar kahkahaların yankılandığı bu evde şimdi sadece anıların tozu ve hüznün gölgesi vardı.",
        "Veda etmenin bu kadar zor olacağını tahmin etmemiştim, arkama bakmadan yürümek imkansız gibiydi.",
        "Kelimelerin kifayetsiz kaldığı, sadece susup için için ağlamak istediğim bir andı."
    ]

    # ---------------------------------------------------------
    # 3. KIZGIN (ANGRY)
    # ---------------------------------------------------------
    kizgin_medium_templates = [
        "{subj} beni deli etti!",
        "Bu ne rezalet, {subj} kabul edilemez.",
        "{subj} karşısında çok sinirlendim.",
        "Derhal telafi edilmeli, {subj} berbat.",
        "Sabrımı taşırdı, {subj} çok kötü.",
        "Buna tahammül edemiyorum, {subj} rezillik.",
        "{subj} beni çileden çıkardı.",
        "Hakkımı helal etmiyorum, {subj} tam bir fiyasko.",
        "Bir daha asla, {subj} beni çok öfkelendirdi.",
        "Bu kadar sorumsuzluk olmaz, {subj} iğrenç."
    ]
    
    kizgin_med_adv_templates = [
        "{subj} için defalarca uyarmama rağmen aynı hatanın yapılması beni çileden çıkardı.",
        "Paramızla rezil olduk resmen, {subj} tam bir dolandırıcılık.",
        "Müşteri memnuniyeti sıfır, {subj} konusunda muhatap bile bulamadım, çok öfkeliyim.",
        "Bu kadar ilgisizlik ve {subj} hatası kabul edilemez, şikayet edeceğim.",
        "İnsanları aptal yerine koymayın, {subj} açıklaması tam bir saçmalık.",
        "{subj} yüzünden bütün planlarım alt üst oldu, çok sinirliyim.",
        "Yaptığınız saygısızlık ve {subj} bardağı taşıran son damla oldu.",
        "Bu iş bilmezlik, {subj} konusundaki beceriksizlik beni deli ediyor.",
        "Nezaketimi korumaya çalışıyorum ama {subj} karşısında sakin kalmak imkansız.",
        "Sorumluların derhal cezalandırılmasını istiyorum, {subj} skandalı örtbas edilemez."
    ]
    
    kizgin_advanced_templates = [
        "Ellerim titriyor, dişlerimi sıkmaktan çeneme ağrılar girdi, bu yapılanı asla affetmeyeceğim.",
        "Gözüm döndü resmen, damarlarımdaki kanın çekildiğini ve yerini saf bir öfkenin aldığını hissettim.",
        "Böyle bir hadsizlik karşısında susup oturmamı beklemeyin, ortalığı birbirine katarım.",
        "Sabrın da bir sonu var ve siz o sınırı çoktan aştınız, artık nezaket beklemeyin.",
        "İçimde patlamaya hazır bir volkan var sanki, tek bir yanlış kelime daha duyarsam ne olacağını kestiremiyorum.",
        "Bu saygısızlık sadece bana değil, tüm değerlerime yapılmış bir hakaret, hesabını vereceksiniz.",
        "Yüzüme baka baka yalan söylenmesi beni çıldırtıyor, insan zekasıyla bu kadar alay edilmez.",
        "Öfkemden kelimeleri toparlayamıyorum, sadece bağırıp çağırmak, her şeyi yıkıp dökmek istiyorum.",
        "Bardağı taşıran o son damla düştü, artık geri dönüşü olmayan bir yola girdik.",
        "Gözlerimden ateş çıkıyor desem yeridir, bu yapılan haksızlığa sessiz kalmayacağım."
    ]

    # ---------------------------------------------------------
    # 4. KORKMUŞ (FEARFUL)
    # ---------------------------------------------------------
    korkmus_medium_templates = [
        "{subj} beni çok korkuttu.",
        "İçim ürperdi, {subj} korkunçtu.",
        "{subj} yüzünden tir tir titredim.",
        "Çok endişeliyim, {subj} tehlikeli görünüyor.",
        "Kalbim yerinden çıkacak gibi oldu, {subj} çok aniydi.",
        "Kabus gibiydi, {subj} beni dehşete düşürdü.",
        "{subj} karşısında donup kaldım.",
        "Güvende hissetmiyorum, {subj} korkutucu.",
        "Tüylerim diken diken oldu, {subj} ürkütücü.",
        "{subj} paniğe kapılmama neden oldu."
    ]
    
    korkmus_med_adv_templates = [
        "{subj} sesini duyunca elim ayağım birbirine dolaştı, çok korktum.",
        "Gece yarısı gelen {subj} beni dehşete düşürdü, hala etkisindeyim.",
        "Sanki biri beni izliyormuş gibi hissettim, {subj} ortamı çok gergindi.",
        "{subj} olayı sonrası evde tek başıma kalmaya korkuyorum.",
        "Bir an nefes alamadım, {subj} beni panik atak krizine soktu.",
        "{subj} görüntüsü gözümün önünden gitmiyor, rüyalarıma giriyor.",
        "Her an kötü bir şey olacakmış hissi var içimde, {subj} beni çok tedirgin etti.",
        "Karanlıkta beliren {subj} silüeti aklımı başımdan aldı.",
        "Bu tehditkar {subj} karşısında ne yapacağımı bilemedim, çok çaresiz hissettim.",
        "{subj} riski beni o kadar korkutuyor ki adım atamıyorum."
    ]
    
    korkmus_advanced_templates = [
        "Kalp atışlarım kulaklarımda yankılanıyordu, gölgelerin içinden bir şeyin bana doğru yaklaştığını hissettim.",
        "Soğuk bir ter boşaldı sırtımdan, ayaklarım yere çivilenmiş gibi hareket edemiyordum.",
        "Nefesim kesildi, boğazımda bir el varmış gibi sıkıyordu, dehşetin buz gibi nefesini ensemde hissettim.",
        "Her gıcırtı, her fısıltı beni yerimden sıçratıyordu, bu sessizlikte saklanan bir tehlike vardı.",
        "Gözlerimi kapattığımda bile o görüntüyü görüyorum, sanki karanlık beni içine çekiyor.",
        "Bilinmeze doğru giden bu yolda her adımım tereddütle dolu, içimdeki korku büyüdükçe büyüyor.",
        "Kapının kolu yavaşça aşağı indiğinde kanım dondu, kaçacak hiçbir yerim yoktu.",
        "Zaman durmuş gibiydi, sadece yaklaşan tehlikenin ayak seslerini duyabiliyordum.",
        "Karanlığın içinde parlayan o iki göz, ruhumun en derinliklerine korku saldı.",
        "Titreyen ellerimle telefonu tutmaya çalıştım ama korkudan parmaklarım hissizleşmişti."
    ]

    # ---------------------------------------------------------
    # 5. ŞAŞKIN (SURPRISED)
    # ---------------------------------------------------------
    saskin_medium_templates = [
        "{subj} beni çok şaşırttı.",
        "İnanamıyorum, {subj} gerçek mi?",
        "{subj} beklemediğim bir sürpriz oldu.",
        "Hadi canım, {subj} nasıl olur?",
        "Şok oldum, {subj} hiç beklemiyordum.",
        "{subj} karşısında nutkum tutuldu.",
        "Gerçekten mi? {subj} çok ilginç.",
        "Bunu hiç tahmin etmezdim, {subj} şaşırtıcı.",
        "Gözlerime inanamadım, {subj} inanılmaz.",
        "{subj} beni hayretler içinde bıraktı."
    ]
    
    saskin_med_adv_templates = [
        "{subj} sonucunu görünce donup kaldım, böyle bir şey beklemiyordum.",
        "Yıllar sonra {subj} ile karşılaşmak beni benden aldı, çok şaşırdım.",
        "Herkesin imkansız dediği {subj} gerçekleşti, hayret verici.",
        "{subj} o kadar ani oldu ki tepki bile veremedim.",
        "Planladığımızdan tamamen farklı bir {subj} çıktı, şaşkınlığımı gizleyemiyorum.",
        "Bir anda {subj} olunca ne yapacağımı şaşırdım.",
        "Bu kadarını beklemiyordum, {subj} beni ters köşe yaptı.",
        "Nasıl olur da {subj} bu hale gelir, aklım almıyor.",
        "Hiç ummadığım bir anda gelen {subj} haberi beni şoke etti.",
        "{subj} detayını öğrenince ağzım açık kaldı."
    ]
    
    saskin_advanced_templates = [
        "Duyduklarım karşısında bir an algılayamadım, sanki dünya bir anlığına durdu ve tersine dönmeye başladı.",
        "Gördüğüm manzara karşısında kelimeler anlamını yitirdi, beynim bu görüntüyü işlemekte zorlanıyordu.",
        "Böyle bir tesadüfün milyonda bir ihtimal olduğunu düşünürdüm, ama işte tam karşımdaydı.",
        "O anın şokuyla olduğum yere çakıldım, gerçeklik algım sarsıldı.",
        "Beklemediğim bir anda gelen bu itiraf, bildiğim her şeyi sorgulamama neden oldu.",
        "Gözlerimi ovuşturdum, rüyada olup olmadığımı kontrol etme ihtiyacı hissettim.",
        "Mantığımın bittiği yerdeyim, bu olayın rasyonel bir açıklaması olamazdı.",
        "Birdenbire değişen olayların hızı karşısında başım döndü, ne olduğunu anlamaya çalışıyordum.",
        "Bu haber adeta gökten düştü, hayatımın akışını bir saniyede değiştirecek kadar beklenmedikti.",
        "Sessizliğin içinden gelen o ses, beni olduğum yerde dondurdu, neye uğradığımı şaşırdım."
    ]

    # ---------------------------------------------------------
    # 6. İĞRENMİŞ (DISGUSTED)
    # ---------------------------------------------------------
    igrenmis_medium_templates = [
        "{subj} midemi bulandırdı.",
        "Öğk, {subj} çok iğrenç.",
        "{subj} berbat kokuyordu.",
        "Görmek bile istemiyorum, {subj} tiksindirici.",
        "{subj} yüzünden iştahım kaçtı.",
        "Bu ne pislik, {subj} rezalet.",
        "{subj} midemi alt üst etti.",
        "Tiksindim resmen, {subj} çok kötü.",
        "{subj} içimi kaldırdı.",
        "Dayanamıyorum, {subj} çok itici."
    ]
    
    igrenmis_med_adv_templates = [
        "{subj} içinden çıkanlar midemi ağzıma getirdi, kusmamak için zor durdum.",
        "Bu kadar pis bir {subj} hayatımda görmedim, hijyen sıfır.",
        "{subj} kokusu o kadar ağırdı ki ortamdan kaçmak zorunda kaldım.",
        "Yemeğin içindeki {subj} detayını fark edince her şeyden tiksindim.",
        "İnsanların bu kadar duyarsız ve {subj} olması midemi bulandırıyor.",
        "Gördüğüm manzara karşısında içim kalktı, {subj} dayanılmazdı.",
        "{subj} dokusu o kadar yapış yapış ve kötüydü ki elimi yıkamak istedim.",
        "Bu görüntü hafızamdan silinsin istiyorum, {subj} çok rahatsız edici.",
        "Nasıl bu kadar {subj} olabilirler, midem kaldırmıyor.",
        "{subj} tadı o kadar kötüydü ki gün boyu etkisinden çıkamadım."
    ]
    
    igrenmis_advanced_templates = [
        "Genzimi yakan o keskin ve ağır koku, nefes almamı imkansız hale getiriyordu, öğürmekten konuşamadım.",
        "Karşılaştığım manzara insanlık dışıydı, içimdeki tüm yaşama sevincini sömüren bir tiksinme hissi uyandırdı.",
        "O yapışkan hissi tenimden atmak için derimi kazımak istedim, kirlenmiş hissediyordum.",
        "Gözlerimi kaçırmak istedim ama o çirkin detaylar zihnime kazınmıştı bir kere, midem kasıldı.",
        "Çürümüşlüğün ve kokuşmuşluğun simgesi gibiydi, yanına yaklaşmak bile cesaret isterdi.",
        "Böyle bir şeye şahit olmak bile beni kirletmiş gibi hissettirdi, hemen duş almak istedim.",
        "Tabağımdaki o şeyi fark ettiğimde boğazımda acı bir tat oluştu, masadan kalkıp lavaboya koştum.",
        "Ortamdaki o basık ve kirli hava ciğerlerime doldukça kendimi zehirlenmiş gibi hissediyordum.",
        "Yüzündeki o sinsi ve itici ifade, bana yılanları hatırlattı, tüylerim ürperdi ama korkudan değil tiksintiden.",
        "Çöplerin arasındaki o görüntü, medeniyetten ne kadar uzaklaşıldığının iğrenç bir kanıtıydı."
    ]

    # ---------------------------------------------------------
    # 7. NÖTR (NEUTRAL)
    # ---------------------------------------------------------
    notr_medium_templates = [
        "{subj} elime ulaştı.",
        "{subj} hakkında bilgim yok.",
        "Sıradan bir {subj} idi.",
        "{subj} ne iyi ne kötü.",
        "Sadece {subj} yaptım.",
        "Durum {subj} ile ilgili.",
        "{subj} orada duruyor.",
        "Bugün {subj} oldu.",
        "{subj} standartlara uygun.",
        "Farklı bir şey yok, {subj} aynı."
    ]
    
    notr_med_adv_templates = [
        "{subj} beklentilerimi ne aştı ne de altında kaldı, ortalama bir deneyimdi.",
        "Siparişim geldi, kutuyu açtım ve {subj} olduğunu gördüm.",
        "Bu konuda henüz bir karar vermedim, {subj} incelemesi yapıyorum.",
        "{subj} işlevini yerine getiriyor, ekstra bir özelliği yok.",
        "Günlük rutinime devam ettim, {subj} dışında her şey olağandı.",
        "Toplantıda {subj} konuşuldu ve notlar alındı.",
        "{subj} rengi fotoğraftaki gibi, ne soluk ne canlı.",
        "Fiyat performans açısından bakarsak {subj} makul seviyede.",
        "Herhangi bir sorun yaşamadım ama {subj} beni büyülemedi de.",
        "Sadece gerekli olduğu için {subj} aldım, duygusal bir bağım yok."
    ]
    
    notr_advanced_templates = [
        "Sabah kalkıp kahvemi demledim, pencereden dışarıdaki trafiği izledim ve işe gitmek üzere hazırlandım.",
        "Dosyaları masanın üzerine bıraktı, saatin tik takları dışında odada ses yoktu, çalışmaya devam ettik.",
        "Marketten ekmek ve süt aldım, kasiyerle kısa bir selamlaşmanın ardından eve doğru yürüdüm.",
        "Hava durumu raporlarına göre yarın yağmur bekleniyor, şemsiyemi kapının yanına hazırladım.",
        "Kitabın son sayfasını çevirdi, kapağını kapattı ve rafına geri yerleştirdi, sonra ışığı söndürdü.",
        "Otobüs durağında beklerken gelen geçen arabaları saydım, zaman yavaşça akıp gidiyordu.",
        "Talimatları okudum ve belirtilen adımları sırasıyla uygulayarak kurulumu tamamladım.",
        "Gözlemlerime göre sistem stabil çalışıyor, verilerde herhangi bir anormallik tespit edilmedi.",
        "Yemeğimi yedikten sonra bulaşıkları makineye dizdim ve televizyonun karşısına geçtim.",
        "Kargo paketini teslim aldım, imza attım ve paketi antreye bırakıp içeri geçtim."
    ]

    # ---------------------------------------------------------
    # 8. HEYECANLI (EXCITED)
    # ---------------------------------------------------------
    heyecanli_medium_templates = [
        "{subj} için sabırsızlanıyorum!",
        "Çok heyecanlıyım, {subj} harika olacak.",
        "{subj} beni motive etti.",
        "Yerimde duramıyorum, {subj} süper.",
        "Kalbim pır pır atıyor, {subj} geliyor.",
        "{subj} haberi beni uçurdu.",
        "Enerjim tavan yaptı, {subj} sayesinde.",
        "Hadi başlayalım, {subj} çok heyecan verici.",
        "{subj} için gün sayıyorum.",
        "Gözlerim parlıyor, {subj} müthiş."
    ]
    
    heyecanli_med_adv_templates = [
        "{subj} projesine başlamak için can atıyorum, fikirlerim dolup taşıyor.",
        "Beklenen gün geldi çattı, {subj} için hazırlıklarım tamam, çok istekliyim.",
        "{subj} duyurusunu görünce çığlık attım, inanamıyorum!",
        "Bu fırsat kaçmaz, {subj} ile hayatım değişebilir, çok umutluyum.",
        "Adrenalinim yükseldi, {subj} deneyimi efsane olacak.",
        "{subj} biletlerini aldım, konser için günleri iple çekiyorum.",
        "Yeni işimdeki ilk günüm için {subj} hazırladım, çok hevesliyim.",
        "Tatil planı kesinleşti, {subj} rotası beni şimdiden havaya soktu.",
        "Sonucu öğrenmek için {subj} sayfasını sürekli yeniliyorum, kalbim güm güm.",
        "Bu yarışmaya katılmak {subj} açısından büyük şans, kazanmayı çok istiyorum."
    ]
    
    heyecanli_advanced_templates = [
        "İçimdeki enerjiye engel olamıyorum, sanki kanatlarım varmış da uçacakmışım gibi hissediyorum.",
        "Yarınki büyük gün için gözüme uyku girmiyor, yatakta dönüp duruyorum, hayaller kuruyorum.",
        "Ellerim terliyor, nefesim hızlanıyor, sahneye çıkacağım anı düşündükçe midemde kelebekler uçuşuyor.",
        "Uzun zamandır beklediğim o an nihayet geldi, her saniyesini dolu dolu yaşamak için hazırım.",
        "Geleceğe dair planlarım beni o kadar motive ediyor ki, sabahları yataktan fırlayarak kalkıyorum.",
        "Bu yolculuk beni bilinmeyene götürecek olsa da keşfetme arzusuyla doluyum, korku değil merak var içimde.",
        "Kalabalığın coşkusuna kapıldım, sesim kısılana kadar bağırmak, bu anı ölümsüzleştirmek istiyorum.",
        "Her yeni bildirim sesiyle irkiliyorum, beklediğim o güzel haberin gelmesi an meselesi.",
        "Gözlerimi kapattığımda bile o anı yaşıyorum, zaferin tadını şimdiden damağımda hissedebiliyorum.",
        "Hayatımda yeni bir sayfa açılıyor ve ben kalemi elime almak için sabırsızlanıyorum."
    ]

    # Map emotions to their templates
    emotions_map = {
        "mutlu": (mutlu_medium_templates, mutlu_med_adv_templates, mutlu_advanced_templates),
        "üzgün": (uzgun_medium_templates, uzgun_med_adv_templates, uzgun_advanced_templates),
        "kızgın": (kizgin_medium_templates, kizgin_med_adv_templates, kizgin_advanced_templates),
        "korkmuş": (korkmus_medium_templates, korkmus_med_adv_templates, korkmus_advanced_templates),
        "şaşkın": (saskin_medium_templates, saskin_med_adv_templates, saskin_advanced_templates),
        "iğrenmiş": (igrenmis_medium_templates, igrenmis_med_adv_templates, igrenmis_advanced_templates),
        "nötr": (notr_medium_templates, notr_med_adv_templates, notr_advanced_templates),
        "heyecanlı": (heyecanli_medium_templates, heyecanli_med_adv_templates, heyecanli_advanced_templates),
    }

    # Nouns to fill in templates randomly
    nouns = ["telefon", "bilgisayar", "araba", "yemek", "film", "kitap", "proje", "oda", "manzara", "elbise", "ayakkabı", "çanta", "oyun", "hizmet", "davranış", "söz", "bakış", "hava", "ortam", "müzik"]

    dataset = {}

    # banks for long-nitelikli generation
    long_banks = {
        "mutlu": {
            "settings": [
                "Sabahın serinliğinde sokağa adım attığımda",
                "Rüzgarın hafifçe perdeyi dalgalandırdığı o anda",
                "Güneş ışığı pencere eşiğine vururken",
                "Sessiz bir odada kitap sayfaları arasında geziniyorken",
                "Yol kenarındaki ağaçların gölgesinde yürürken"
            ],
            "details": [
                "adımlarımın ritmi fark edilmeden hızlandı",
                "omuzlarımdaki ağırlık yerini hafif bir esintiye bıraktı",
                "zihnimdeki gürültü yavaşça dağılıp berrak bir boşluğa dönüştü",
                "dudaklarımın kenarında küçük bir kıvrım yerleşip kaldı",
                "kalbimde düzenli ve sakin bir akış hissedilir oldu"
            ],
            "images": [
                "pencereden sızan ışık toz zerrelerini parlatıyor",
                "sokağın sonundaki kedi usulca merdivenlere tırmanıyor",
                "taze kahve kokusu mutfağın kapısına kadar yayılıyor",
                "saatin tik takları arka planda ince bir ritim tutuyor",
                "duvardaki tablo renklerini daha canlı gösteriyor"
            ],
            "closure": [
                "o anın sade akışına kendimi bıraktım",
                "içimdeki sessiz uyumun farkına varıp derin bir nefes aldım",
                "günün sıradan çizgisi beklenmedik biçimde güzelleşti",
                "kalemim sayfada daha rahat ilerledi",
                "zamana direnmeden kapının kolunu çevirip dışarı çıktım"
            ]
        },
        "üzgün": {
            "settings": [
                "Gri bulutlar şehrin üzerine ağır bir perde gibi çökmüşken",
                "Pencere kenarında yağmur izlerini takip ederken",
                "Koridorda yankılanan ayak sesleri uzaklaştığında",
                "Eski fotoğrafların tozlu kenarlarına dokunurken",
                "Gece lambasının solgun ışığında masaya yaslanmış halde"
            ],
            "details": [
                "boğazımda sabit bir düğüm varmış gibi yutkundum",
                "adımlarımın ucu yere daha sert değdi",
                "kelimeler aklıma gelip kapının önünde durdu",
                "zaman ağırlaşarak pencere camına yapıştı",
                "içimde boş bir oda kapısı aralık kaldı"
            ],
            "images": [
                "duvardaki takvim bir sayfayı daha sessizce bıraktı",
                "çay bardağındaki buhar ince bir çizgi halinde kayboldu",
                "rüzgar posta kutusunun kapağını hafifçe salladı",
                "masa üzerinde unutulmuş bir mektubun köşesi kıvrıldı",
                "merdiven boşluğunda eski bir şarkı çok uzaktan duyuldu"
            ],
            "closure": [
                "kapıyı kapatırken içeriden yayılan sessizliğe kulak verdim",
                "derin bir nefes alıp perdeleri biraz daha kapattım",
                "saatin yavaş vuruşlarını saymayı bıraktım",
                "ışığı kısıp sandalye üzerinde biraz daha bekledim",
                "raflara dokunmadan odadan çıktım"
            ]
        },
        "kızgın": {
            "settings": [
                "Telefonun ekranı bir uyarıyla aniden parladığında",
                "Masadaki kalemin ucu kağıdı çizdiği anda",
                "Kapı eşiğinde bekleyen gölge belirginleşirken",
                "Sözlerin havada keskin bir çizgi oluşturduğu anlarda",
                "Toplantı odasının havası ağırlaşıp cam buğulandığında"
            ],
            "details": [
                "çenem fark etmeden kasıldı",
                "nefesim kısa aralıklarla sertleşti",
                "yumruğumun içi istemsizce kapandı",
                "ensede ince bir gerilim dalgası yürüdü",
                "omuz çizgim yukarı doğru gerginleşti"
            ],
            "images": [
                "kalem ucu kağıtta iz bıraktı ve aniden durdu",
                "duvarda asılı saat bir an sanki sesini yükseltti",
                "camın ardındaki siluet birkaç saniye hareketsiz kaldı",
                "masa kenarında duran dosya hafifçe yer değiştirdi",
                "bir cümle oda içinde yankılanıp kesildi"
            ],
            "closure": [
                "bakışlarımı bir noktaya sabitleyip cümleyi sonuna kadar kurdum",
                "sandalyeyi geri itip derin bir nefes saldım",
                "kapı kolunu ölçülü bir hareketle kavradım",
                "kağıdı dikkatle katlayıp masanın köşesine bıraktım",
                "adımlarımı sayarak odadan çıkmayı seçtim"
            ]
        },
        "korkmuş": {
            "settings": [
                "Koridor ışığı aniden titrediğinde",
                "Merdiven boşluğundan gelen ince bir çıtırtı duyulduğunda",
                "Gece penceresi dışarıdaki karanlığı içeri sızdırırken",
                "Asansör kapısı beklenmedik bir gecikmeyle açılmadığında",
                "Zil sesi beklenenden uzun sürdüğünde"
            ],
            "details": [
                "sırtımdan soğuk bir çizgi geçti",
                "adımlarım geri doğru tartılarak kısaldı",
                "parmak uçlarım kapı kenarını aradı",
                "gözlerim karanlığın içine odaklanıp alışmaya çalıştı",
                "nefesim ölçüsüz bir tempoyla dalgalandı"
            ],
            "images": [
                "kapı kolu yerinden milim oynamadan durdu",
                "duvardaki gölge iki saniye büyüyüp küçüldü",
                "paspasın kenarı hafifçe kıvrıldı",
                "koridorun sonunda bir ışık çizgisi belirdi ve söndü",
                "pencerede kendi yansımam bir an tanınmaz oldu"
            ],
            "closure": [
                "ayaklarımı sessizce döndürüp ışığa doğru ilerledim",
                "kapı eşiğinde durup derin bir nefes aldım",
                "anahtarı yavaşça çevirip içeriyi yokladım",
                "adımlarımı sayarak merdivenleri indim",
                "duvar boyunca ilerleyip köşeyi dikkatle döndüm"
            ]
        },
        "şaşkın": {
            "settings": [
                "Ekranda beliren satır beklenmedik bir sembol gösterdiğinde",
                "Sokağın köşesinde ansızın tanıdık bir yüz göründüğünde",
                "Plan defterindeki tarih ile kapıdaki afiş çakıştığında",
                "Tam konuşacakken cümlenin başka bir yere evrildiği anda",
                "Kutu açıldığında içinden beklenmedik bir parça çıktığında"
            ],
            "details": [
                "algım bir anlığına yer değiştirdi",
                "adımlarım oldukları yerde durdu",
                "bakışlarım bir noktadan diğerine hızla sıçradı",
                "zaman sanki kenarlardan yavaşladı",
                "kelimeler birbirini iterek sıra dışı bir dizilim aldı"
            ],
            "images": [
                "takvim yaprağı rüzgarla ters yöne kıvrıldı",
                "yol tabelası parıltıyla okunmaz hale geldi ve yeniden netleşti",
                "not defterindeki satırların arası bir an genişledi",
                "paket içindeki köpükler beklenmedik bir şekilde dağıldı",
                "kapı zili tek bir uzun ses olarak yankılandı"
            ],
            "closure": [
                "olayı zihnimde birkaç kez çevirip yeni bir yerleştirme yaptım",
                "derin bir nefes alıp ritmi yeniden kurdum",
                "kısa bir duraksamanın ardından kaldığım yerden devam ettim",
                "gördüklerimi not edip sayfayı kapattım",
                "adımlarımı yeniden toplayıp yürümeyi sürdürdüm"
            ]
        },
        "iğrenmiş": {
            "settings": [
                "Mutfağın köşesinde duran kap açık kaldığında",
                "Sokağın kenarında birikmiş suyun yüzeyi dalgalandığında",
                "Karton kutu kaldırıldığında altından beklenmedik bir görüntü çıktığında",
                "Asansörün metal yüzeyi parmak izleriyle dolduğunda",
                "Lavaboda duran su uzun süre hareket etmediğinde"
            ],
            "details": [
                "genzimi yakan keskin bir iz bıraktı",
                "parmak uçlarım yapışkan bir hisle geri çekildi",
                "boğazımda acı bir tat dolaştı",
                "gözlerim istemsizce başka bir noktaya kaçtı",
                "ciğerlerime dolan hava yoğun ve ağırlaştı"
            ],
            "images": [
                "zemindeki lekeler ışık altında kabartılı göründü",
                "koku kapının eşiğine kadar sızdı",
                "paketin içinden çıkan parça beklenmedik biçimde parlaktı",
                "metal yüzeydeki izler kısa süreli bir desen oluşturdu",
                "lavabonun kenarında birikinti ince bir halka bıraktı"
            ],
            "closure": [
                "musluğu açıp suyu bir süre akıttım",
                "pencereyi ardına kadar açıp hava akışını değiştirdim",
                "elimi hızla yıkayıp havluyla kurulayıp geri çekildim",
                "kutuyu kapatıp kenara aldım",
                "odadan çıkıp kapıyı tamamen kapattım"
            ]
        },
        "nötr": {
            "settings": [
                "Sabah bilgisayarı açıp günlük kayıtları kontrol ederken",
                "Toplantı notlarını sırayla düzenlerken",
                "Depo listesini tarayıp eksikleri işaretlerken",
                "Mutfağa gidip su ısıtıcısını çalıştırdıktan sonra",
                "Gün sonu raporunu tablo halinde tamamlarken"
            ],
            "details": [
                "adımları standart bir sırayla uyguladım",
                "verileri kronolojik olarak hizaladım",
                "önceliklere göre küçük düzeltmeler yaptım",
                "ara başlıklar ekleyip dosyayı yeniden kaydettim",
                "ölçümleri iki kez kontrol edip tutarlılığı sağladım"
            ],
            "images": [
                "ekrandaki grafik çizgileri düzgün bir eğri oluşturdu",
                "sayfanın altındaki imza alanı boş kaldı",
                "tablolarda hücre renkleri sabit bir tona geçti",
                "klavyenin sesi düzenli aralıklarla duyuldu",
                "zaman damgası dosya adının yanına işlendi"
            ],
            "closure": [
                "dosyayı kapatıp bir sonraki maddeye geçtim",
                "çıktıyı yazdırmadan önce son kez gözden geçirdim",
                "listeyi arşiv klasörüne taşıdım",
                "notları senkronize edip uygulamadan çıktım",
                "raporun başına tarih ekledim"
            ]
        },
        "heyecanlı": {
            "settings": [
                "Kalabalığın uğultusu salonun tavanına kadar yükselirken",
                "Ekranda beklediğim satırın gelmesine saniyeler kalmışken",
                "Sahne ışıkları yavaşça açılıp perde kıpırdadığında",
                "Uçağın tekerleri pistte hizalanıp hızlanmaya başladığında",
                "Kargo takip ekranındaki çubuk son bölüme ulaştığında"
            ],
            "details": [
                "kalp ritmim belirginleşip adımlarımın önüne geçti",
                "ellerim hafifçe terledi ve parmaklarım titredi",
                "nefesim daha kısa aralıklarla akmaya başladı",
                "bakışlarım tek bir noktaya kilitlenip çevreyi unuttu",
                "zaman dar bir tünel gibi uzayıp kısaldı"
            ],
            "images": [
                "ışık çizgileri duvarda dalgalı desenler oluşturdu",
                "ekranda küçük bir ikon yanıp sönerek ilerlemeyi gösterdi",
                "kalabalığın ritmi tek bir ses dalgasına dönüştü",
                "pistin kenarındaki işaretler hızla geriye akıp gitti",
                "takip çubuğunun son bölümü parlayıp sabit kaldı"
            ],
            "closure": [
                "dudaklarımı ıslatıp gözlerimi kırpmadan ileriye baktım",
                "nefesimi derleyip omuzlarımı gevşettim",
                "adımı atıp çizgiyi geçtim",
                "kemeri kontrol edip başımı arkaya yasladım",
                "ekrandaki bildirimi açıp satırları hızla okudum"
            ]
        }
    }

    def build_long_text(emotion):
        bank = long_banks[emotion]
        parts = [
            random.choice(bank["settings"]),
            random.choice(bank["details"]),
            random.choice(bank["images"]),
            random.choice(bank["closure"]),
        ]
        return f"{parts[0]}, {parts[1]}; {parts[2]} ve {parts[3]}."

    for emotion, (med, med_adv, adv) in emotions_map.items():
        dataset[emotion] = []
        
        # Helper to fill templates
        def fill_templates(templates, count):
            results = []
            while len(results) < count:
                tmpl = random.choice(templates)
                subj = random.choice(subjects)
                noun = random.choice(nouns)
                time_val = random.choice(time_markers)
                
                filled = tmpl.replace("{subj}", subj).replace("{noun}", noun).replace("{time}", time_val)
                results.append(filled)
            return results

        dataset[emotion].extend(fill_templates(med, 300))
        dataset[emotion].extend(fill_templates(med_adv, 300))

        adv_generated = []
        prefixes = ["Dürüst olmak gerekirse, ", "Şunu söylemeliyim ki, ", "Anlatması zor ama, ", "O an, ", "Bazen, "]
        while len(adv_generated) < 300:
            base = random.choice(adv)
            prefix = random.choice(prefixes)
            if random.random() > 0.5:
                adv_generated.append(prefix + base)
            else:
                adv_generated.append(base + " " + prefix.replace(",","").strip() + ".")
        dataset[emotion].extend(adv_generated)

        long_generated = []
        while len(long_generated) < 300:
            long_generated.append(build_long_text(emotion))
        dataset[emotion].extend(long_generated)

    return dataset

if __name__ == "__main__":
    data = generate_dataset()
    
    # Save to file
    file_path = "c:\\Users\\Enes\\Desktop\\Yeni klasör\\emotion_data.json"
    
    # Write to file
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print("Dataset generated successfully!")
