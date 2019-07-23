# def keySearch(L, k):
#     for elem in L:
#         if elem[0] == k: return elem[1]
#     return None

EtoOsh = {'lightning': 'olwaadhi', 'lightnings': 'oombadhi', 'scar': 'oshaadhi', 'scars': 'iiyadhi', 'arms': 
         'omooko', 'birthmark': 'oshaala', 'birthmarks': 'iiyala', 'colour': 'olwaala',
         'color': 'olwaala', 'colours': 'omalwaala', 'colors': 'omalwaala', 'palm': 'oshaale', 'palms': 'iiyale',
         'palm-frond': 'olwaale', 'palm-fronds': 'oombale', 'doctor': 'ndohotola', 'doctors': 'eendohotola',
         'healer': 'omwaaludhi', 'healers': 'aayaludhi', 'nurse': 'omupangi', 'nurses': 'aapangi',
         'medical practitioner': 'omupangi', "medical practitioners": 'aapangi',
         'anthills': 'iiyanda', 'darn': 'oshaando', 'darns': 'iiyando', 'glory': 'eyadhimo', 'splendour':
         'eyadhimo', 'splendor': 'eyadhimo', 'deliriousness': 'eadhuko', 'scabies': 'olwaga', 'August':
         'Auguste', 'court': 'ompangu', 'opening': 'omwaka', 'open space': 'ehalala', 'grabbing': 'eakulo',
         'buttermilk': 'omaale', 'crucifixion': 'ealelo komushigakano', 'nursing mother': 'omwali', 'healing':
         'ealudho', 'curing': 'ealudho', 'eavesdropping': 'eambelo', 'overhearig': 'eambelo', 'support':
         'eambidhidho', 'America': 'Amerika', 'American': 'Omwaamerika', 'Americans': 'Aamerika', 'secretary':
         "amushanga", 'secretaries': 'oohamushanga', 'child': 'okanona', 'children': 'uunona', 'daughter':
         'omwanakadhona', 'daughters': 'oyanakadhona', 'son': ['omwanamati'], 'sons': ['oyanamati'],
         'African Ebony': ['omwandi'], 'African Ebonys': ['oomwandi'], 'African Ebonies': ['oomwandi'],
         'fermentation': ['olwani'], 'ringworm': ['eankadhi'], 'umbilical cord': ['okaankonga'],
         'umbilical cords': ['uuankonga'], 'April': ['Apilili'], 'hide': ['ombanza'], 'pharmacy': ['oapoteka'],
         'pharmacies': ['ooapoteka'], 'apples': ['iiyapula'], 'udder': ['oshawo'],
         'udders': ['iishawo'], 'December': ['Desemba'], 'player': ['omudhani'], 'players': ['aadhani'],
         'dancer': ['omundanisi'], 'dancers': ['aandanisi'], 'game': ['uudhano'], 'games': ['omaudhano'], 'toy':
         ['okadhanitho'], 'boxer': ['omudhengingonyo'], 'boxers': ['aadhengingonyo'], 'beating': ['edhengo'],
         'train': ['eshina lyokolutenda'], 'trains': ['omashinga gokolutenda'], 'trainer': ['omudheuli'],
         'trainers': ['aadheuli'], 'exercise': ['edhewo'], 'exercises': ['omadheo'], 'root': ['omudhi'], 'roots':
         ['omidhi'], 'type': ['oludhi'], 'gender': ['omukakwashike kookantu'], 'sex': ['omukakwashike kookantu'],
         'perseverance': ['eidhidhimiko'], 'efficiency': ['uudhiginini'], 'bird': ['okadhila'], 'birds':
         ['uudhila'], 'plane': ['odhila'], 'planes': ['eedhila'], 'aeroplanes':
         ['eedhila'], 'helicopter': ['edhagadhaga'], 'helicopters': ['omadhagadhaga'], 'idea': ['edhiladhilo'],
         'ideas': ['omadhiladhilo'], 'black crow': ['edhilakola'], 'black crows': ['omadhilakola'], 'soot':
         ['omudhilo'], 'fledgling': ['okadhilona'], 'fledglings': ['uudhilona'], 'corpse': ['omudhimba'],
         'dead body': ['omudhimba'], 'corpses': ['omidhimba'], 'dead bodies': ['omidhimba'], 'remembrance':
         ['edhimbuluko'], 'eraser': ['okadhimitho'], 'erasers': ['uudhimitho'], 'name': ['edhina'], 'names':
         ['omadhina'], 'vicinity': ['omudhingoloko'], 'biltong': ['odhingu'], 'biltongs': ['oodhingu'],
         'despicable': ['dhinwa'], 'despicable person': ['omudhinwa'], 'despicable people': ['aadhinwa'],
         'the killing': ['edhipago'], 'the killings': ['omadhipago'], 'the murder': ['edhipago'], 'knot':
         ['edhita'], 'knots': ['omadhita'], 'killer': ['omudhipagi'], 'killers': ['aadhipagi'], 'murderer':
         ['omudhipagi'], 'murderers': ['aadhipagi'], 'murdered person': ['omudhipagwa'],
         'moon': 'omwedhi', 'the moon': 'omwedhi', 'a moon': 'omwedhi', 'to the moon': 'komwedhi', 'month': 'omwedhi',
         'months': 'oomwedhi', 'end of the month': 'eshulilo lyomwedhi', 'at the end of the month':
         'peshulilo lyomwedhi', 'close the door': 'edhila omweelo', 'the door is closed': 'omweelo ogwa edhila',
         'closed the door': 'okwa edhila omweelo',
         'chance': 'olweedhe', 'first born': 'osheeli', 'door': 'osheelo', 'doors': 'omiyelo', 'entrance': 'osheelo',
         'traveler': 'omweendi', 'travelers': 'aayendi', 'traveller': 'omweendi', 'travellers': 'aayendi',
         'journey': 'olweendo', 'madam': 'efolo', 'thorn': 'okwega', 'thorns': 'omakwega', 'dagger': 'omwele',
         'daggers': 'oomwele', 'knife': 'ombele', 'knives': 'oombele', 'bucket': 'eemele', 'buckets': 'omaemele',
         'cemetery': 'omayendo', 'graveyard': 'omayendo', 'sugar cane': 'omwenge', 'sugar canes': 'oomwenge', 'lizard':
         'eengele', 'lizards': 'omaengele', 'fog': 'oshientsi', 'feather': 'olwenya', 'feathers': 'omalwenya',
         'dry season': 'okwenye', 'dry seasons': 'okwenye', 'life': 'onkalamwenyo', 'soul': 'omwenyo',
         'lives': 'eenkalamwenyo', 'animals': 'iinamwenyo', 'Saturday': 'Olyomakaya', 'on Saturday': 'mOlyomakaya',
         'on a Saturday': 'mOlyomakaya', 'on Saturdays': 'mOmalyomakaya', 'vinegar': 'omaetika', 'Thursday': 'Etine',
         'on Thursday': 'mEtine', 'on a Thursday': 'mEtine', 'on Thursdays': 'mOmatine', 'Wednesday': 'Etitatu',
         'on Wednesday': 'mEtitatu', 'on a Wednesday': 'mEtitatu', 'on Wednesdays': 'mOmatitatu', 'Tuesday': 'Etiyali',
         'on Tuesday': 'mEtiyali', 'on a Tuesday': 'mEtiyali', 'on Tuesdays': 'mOmatiyali', 'farm': 'ofaalama', 'farms':
         'oofaalama', 'introduction': 'efalomo', 'a sale': 'ofanditha', 'the sale': 'ofanditha', 'it"s on sale':
         'oshi li kofanditha', 'it is on sale': 'oshi li kofanditha', 'they are on sale': 'oyi li kofanditha',
         'sold': 'landitha', 'auctioneer': 'omufandithi', 'a drawing': 'ethano', 'the drawing': 'ethano', 'a picture':
         'ethano', 'the picture': 'ethano', 'picture': 'ethano', 'pictures': 'omathano', 'the pictures': 'omathano',
         'drawings': 'omathano', 'the drawings': 'omathano', 'photogragh': 'ethano', 'a photograph': 'ethano',
         'the photograph': 'ethano', 'the photographs': 'omathano', 'photographs': 'omathano', 'photographer':
         'omuthaneki', 'photographers': 'aathaneki', 'a photographer': 'omuthaneki', 'the photographer': 'omuthaneki',
         'the photographers': 'aathaneki', 'explanation': 'efatululo', 'explanations': 'omafatululo', 'commentator':
         'omufatululi', 'commentators': 'aafatululi', 'absenteeism': 'oku faula', 'truant': 'ofaule', 'truants':
         'oofaule', 'a truant': 'ofaule', 'the truants': 'oofaule', 'they are truants': 'oyo oofaule',
         'February': 'Februali', 'in February': 'muFebruali', 'during February': 'muFebruali', 'the suspect':
         'omufekelwa', 'a suspect': 'omufekelwa', 'the suspects': 'aafekelwa', 'snuff': 'ofenya',
         'suspicion': 'efekelo', 'suspicions': 'omafekelo',
         'tax': 'iifendela', 'taxes': 'oompale', 'taxpayer': 'omufendeli', 'taxpayers': 'aafendeli', 'receipt':
         'okafilipi', 'receipts': 'uufilipi', 'slip': 'okaslepa', 'slips': 'uuslepa', 'payslip': 'okalepa komafutilo',
         'payslips': 'uuslepa womafutilo', 'necktie': 'ofilipusa', 'neckties': 'oofilipusa', 'mouth-organ':
         'okafilita', 'mouth-organs': 'uufilita', 'leaf': 'efo', 'leaves': 'omafo', 'turn': 'olufo',
         'turns': 'omalufo', 'opportunity': 'olufo',
         'opportunities': 'oompito', 'foreman': 'folomana', 'foremen': 'oofolomana', 'boss': 'omuhona',
         'bosses': 'aahona', 'furrow': 'ofoola', 'furrows': 'oofoola', 'form': 'ofooloma', 'forms': 'oofooloma',
         'winter': 'okufu', 'winter time': 'ethimbo lyokufu', 'a hypocrite': 'omufudhime', 'hypocrites': 'aafudhime',
         'is a hypocrite': 'omufudhime', 'are hypocrites': 'aafudhime', 'the hypocrites': 'aafudhime',
         'breath': 'omufudho', 'holiday': 'efudho', 'holidays': 'omafudho', 'break': 'okafudho',
         'playtime': 'okafudho', 'hair': 'omafufu',
         'a greedy person': 'omufukentu', 'the bride': 'omufuko', 'a bride': 'omufuko', 'brides': 'aafuko',
         'the brides': 'aafuko', 'ground nut': 'ofukwa', 'ground nuts': 'oofukwa', 'a hole': 'oshilambo', 'the hole':
         'iilambo', 'the holes': 'iilambo', 'holes': 'iilambo', 'a load of': 'ofulaha y', 'hero': 'ependafule',
         'heroes': 'omapendafule', 'heroine': 'ependafule', 'heroines': 'omapendafule', 'the hero': 'ependafule',
         'the heroes': 'omapendafule', 'the heroine': 'ependafule', 'the heroines': 'omapendafule', 'frog': 'efuma',
         'the frog': 'efuma', 'the frogs': 'omafuma', 'frogs': 'omafuma', 'a frog': 'afuma', 'burial': 'efumbiko',
         'funeral': 'efumbiko', 'lies': 'iifundja', 'flood': 'efundja', 'a liar': 'omuniifundja', 'they are liars':
         'yo aaniifundja', 'liars': 'aaniifundja', 'the liars': 'aaniifundja', 'jealousy': 'efupa', 'shortness':
         'uufupi', 'abbreviation': 'efupipiko (oma-)', 'an abbreviation': 'efupipiko', 'abbreviations': 'omafupipiko',
         'the abbreviations': 'omafupipiko', 'payment': 'ofuto', 'payments': 'iifuta', 'the payments': 'iifuta',
         'thief': 'omufuthi', 'thieves': 'aafuthi', 'the thief': 'omufuthi', 'the thieves': 'aafuthi', 'reward':
         'ondjambi', 'rewards': 'oondjambi', 'vanity': 'uufuuli', 'fat': 'ekagadhi', 'butter': 'ombuta', 'oil':
         'omagadhi', 'lotion': 'omagadhi', 'honey': 'omagadhi goonyushi', 'margarine': 'ombuta', 'hat': 'egala',
         'hats': 'omagala', 'a hat': 'egala', 'the hats': 'omagala', 'prayer': 'egalikano', 'prayers': 'omagalikano',
         'a prayer': 'egalikano', 'the prayers': 'omagalikano', 'a return': 'egaluko', 'the return': 'egaluko',
         'his return': 'egaluko lye', 'her return': 'egaluko lye', 'their return': 'egaluko lyawo', 'our return':
         'egaluko lyetu', 'its return': 'egaluko lya sho', 'protector': 'omugameni', 'the protector': 'omugameni',
         'a protector': 'omugameni', 'protectors': 'aagameni', 'protection': 'egameno', 'sworn declaration': 'egano',
         'vow': 'egano', 'vows': 'omagano', 'granary': 'eshisha', 'granaries': 'omashisha', 'donor': 'omugandjishali',
         'donors': 'aagandjishali', 'a donor': 'omugandjishali', 'the donors': 'aagandjishali', 'the handing over':
         'egandjo', 'a handing over': 'egandjo', 'donation': 'iigandjwa', 'domations': 'iigandjwa', 'gifts': 'omagano',
         'presents': 'omagano', 'talents': 'omagano', 'abate': ['lota (o)'], 'abattoir': ['okatomeno (uu-)'],
         'abdomen': ['omumpanya (omi-)', 'oshinena (ii-)'], 'abduction': ['embembopo'], 'ability': ['evulo (oma-)'],
         'able': ['pondola', 'The man is able to build his house=', 'Omusamane okwe shi pondola okutunga egumbo lye'],
         'abscess': ['oshitumbuka (ii-)'], 'absence': ['uukeepo', 'efaulo'], 'abundance': ['(food)', 'eloolo'],
         'academy': ['oakademi'], 'accent': ['oaksende (oo-)'], 'accomodation':  ['ekalwahala'], 'accountability':
         ['eyalulo', 'uupulwankombo'], 'accused': ['(court)', 'omutamanekwa (aa-)'], 'accuser':
         ['omulundili (aa-)', 'omutamaneki (aa-)'], 'acrophobia': ['uugelele'], 'actor': ['omunyandi (aa-)'],
         'accusation': ['elundilo (oma-)'], 'adansonia digitata': ['omukwa (onu-)'],
         'baobab': ['omukwa'], 'addition': ['etulokumwc'], 'accordion': ['enambati (oma-)'], 'addressee':
         ['omutuminwa (aa-)', 'omupopithwa'], 'adenoid': ['omwenge (otagu: oomw-, otadhi)'],  'adjective':
         ['oshityalupe (ii-)'], 'adjournment': ['ezimbuko'], 'adult': ['omukuluntu (aa-)'], 'adulterer':
         ['omuhondeli (aa-)'], 'adulteress': ['omuhondeli (aa-)'], 'adultery': ['oluhondelo (omalu-)'],
         'adversity': ['omupya (omi-)'], 'advertisement': ['etseyitho lyopaipindi(oma-)', 'etseyithilo (oma-)'],
         'advice': ['omayele'], 'aeroplane': ['edhila (oma-)', 'ondhila (oo-)'],  'affiliation': ['ehemukilomumwe'],
         'Afrikaans': ['Oshimbulu'], 'afternoon': ['komatango'], 'age': ['uukokele'], 'agenda':
         ['oagenda (oo-)', 'elandulathano lyiikundathanwa (oma-)'], 'agreement':
         ['euvathano (oma-)', 'euvaneno (oma-)'], 'agriculture': ['uunamapya nuuniimuna'], 'agronomy':
         ['uunongononimapya'], 'agronomist': ['omunongononimapya (aa-)'], 'aim':
         ['oshilalakanenwa (ii-)', 'elalakano (oma-)'], 'air': ['ombepo', 'ewangandjo'], 'air bubble':
         ['ombwimbwi (oo-)'], 'alarm': ['onkugo (oo-)', 'okangendjo'], 'albino': ['ethithi (oma-)', 'ekishi'],
         'albizia anthelmintica': ['omupopo (omi-)'], 'album': ['oalbuma (oo-)', 'embo lyomafano'],
         'alcohol': ['oalkoholi'], 'alcoholic drink': ['oshikolitha'], 'algae': ['onguwi(oo-)'], 'alkali':
         ['oalikali', 'oshimongwa'], 'alliance': ['ondjuvanene(oo-)', 'ehangano(oma-)'], 'allurement': ['oshinge'],
         'aloe': ['(a.esculenta)', 'endombo(oma-)'], 'aluminium': ['oaluminiuma'], 'amateur boxer':
         ['omumbokisilinyanyu(aa-)'], 'ambassador': ['omukalelipo(aa -)'], 'ambush': ['elangelo(oma-)'], 'ammonia':
         ['amoniaka'], 'ammonium sulphate': ['amoniumsulfate'], 'ammunition': ['oshuumbithi(ii-), oshiyumbithi(ii -)'],
         'amnesty': ['esohenda'], 'amount': ['omwaalu(omiyalu)'], 'amulet': ['oshigegeti(ii-)'], 'analysis':
         ['evongokonono(oma -)'], 'anatomy': ['oanatomi'], 'anatree': ['(acacia albida)', 'omuyele(omi-)'],
         'acacia albida': ['omuyele(omi -)'], 'ancestor': ['epipi(oma-)', 'omukulugonale (aa-)'],
         'ancestral spirits': ['aathithi'], 'angular point': ['ekuvu (oma-)'], 'animal': ['oshinamwenyo'],
         'wild animal': ['oshiyamakuti'], 'angel': ['omuyengeli (aa-)'], 'angle':
         ['okolonela (oo-)', 'ekuvu (oma-)', 'onkuvu (oo-)'], 'Anglican church': ['ongeleka yaAngilikana'],
         'anchor': ['ohangela(oo-)'], 'ankle': ['onyugu (oo-)'], 'annexation': ['etendoko'], 'annual function':
         ['okatuthihulitho'], 'answer': ['eyamukulo (oma-)'], 'ant':
         ['ondhindhi (oo-)', 'eteta (oma-)', 'big brown ant = ', 'emboombolo (orna-)', 'small black ant',
          'ombuka (oo-), okacihidhi (uu-)'],
         'ant-bear': ['(African ant-bear)', 'eyamayarna (oma-)'], 'ant-eater': ['(scaly ant-eater)' 'ongaka (oo-)'],
         'anthill': ['oshaanda (iiyanda)', 'oshiyanda (ii-)'], 'ant-hill': ['oshaanda (iiyanda)', 'oshiyanda (ii-)'],
         'anthrax': ['ombuiwa (omukithi gombulwa)'], 'antibiotic': ['oshidhipagimbuto (dhuuvu) (ii-)'], 'anticipation':
         ['etegameno'], 'anus': ['onufu (oo-)'], 'anxiety': ['omahwilili', 'uuhwenge'], 'anvil': ['oshikalo (ii-)'],
         'ape': ['ondjima (oo-)'], 'apoplexy': ['ombanda', 'esilombanda'], 'apparatus': ['oaparate (oo-)'],
         'apparition': ['oshihehelela (ii-)', 'oshikwafa (ii-)'], 'appeal': ['etsikilompangu'], 'appearance':
         ['ondjelo', 'eholoko', 'ombelo', 'She has a beaurful appearance. = ', 'Oku na ondjelo ombwanawa.'],
         'appendicitis': ['okiimili'], 'appendix': ['okiimili (oo-)', 'oshigwedhelwako (ii-)'], 'appetite':
         ['omwamwa', 'appetite for porridge', 'omwamwa gwoshithima'], 'applause': ['ehakelo', 'ekugililo'],
         'apple': ['oshiapula', 'oshiyapula (ii-)'], 'application':
         ['eindilo (oma-)', 'application form = ' 'ofolomaindilo'], 'appointment': ['oshilage (ii—)'], 'apron':
         ['oshitetahema (ii-)'], 'aquarium': ['oakwariuma'], 'Arab': ['Omwaarabia (Aayarabia)'], 'arbitrator':
         ['omupongololi (aa-)'], 'architect': ['omuthanekingulu (aa-)', 'omusindingulu (aa-)', 
         'omusindigumbo (aa-)'], 'archeology': ['uunongononi wiikulunima'], 'area': 
         ['ondjalo (oo-)', 'omuyabo (omi-)', 'ehala'], 'argument': ['oontamanana'], 'arm':
         ['okwaako', 'okwooko', 'okooko (omaako)'], 'armpit': ['onkwapa (oo-)'], 'armament': ['ehomato (oma-)'],  'arrangement': 
         ['elongekidho (oma-)', 'eilongekidho'], 'arrival': ['eyo (oma-)', 'ethiko (oma-)'], 'arrogance': 
         ['elundu'], 'arrow': ['oshikuti (ii-)', 'arro tip = ', 'omuvi (omi-)', 'wooden tipped arrow = ',
         'ehongo (oma-)', 'arrow head = ', 'eholongo (oma-), ondjindja (oo-)'], 'artery':
         ['onkandjambinzi (oo-)'], 'article': ['oshinima (ii-)', 'okatendo (uu-)'], 'artisan': 
         ['engomba (lyiilonga)'], 'artist': ['omunongo (aa-)', 'onkulungu (oo-)'],
         'arts': ['uunkulungu (omau-)', 'uunongo', 'uungongi'], 'asbestos': ['oasbesa'],
         'Asia': ['Asia'], 'Asian': ['Omwaasia (Aayasia)'], 'ash': ['omutoko (omi-)'], 'arrest': ['ekwatopo'],
         'army': ['etangakwiita (oma-)', 'etanga lyaakwiita'], 'aroma': ['ezimba'],  'asking': ['okupula'],
         'aspect': ['oshinima'], 'assegai': ['egonga (oma-)'], 'assembly': ['omutumba (omi-)'], 'assignment':
         ['oshitopolwa shiilonga', 'oshitopolwailonga (ii-)'],  'assistant': ['omuyakuli (aa-)', 'omupeha (aa-)'],
         'assistance': ['ekwatho (oma-)', 'eyambidhidho (oma-)'], 'association': ['ehangano (oma-)'], 'asthma':
         ['oasma'], 'astonishment': ['onkumwe'],  'atom': ['oatoma (oo-)'],  'Atlantic': ['Atlantika'],
         'atlas': ['oatilasa (oo-)', 'oatlasa (oo-)'], 'atmosphere': ['ombepo (oo-)', 'ongandjombepo',
         'ewangandjo'], 'attack': ['eponokelo'], 'attacker': ['omuhomoni (aa-)', 'omumatukili (aa-)', 
         'omutondokeli (aa-)', 'omuponokeli (aa-)'], 'attempt': ['ekambadhalo ', 'onkambadhala'], 'attention':
         ['eimweneneno', 'pay attention = ', 'ndhindhilika (e)'], 'attentiveness': ['oonkoto'], 'attitude':
         ['omikalo', 'oohedhi'], 'attraction': ['ohokwe (oo-)'], 'auction': ['ofanditha (oo-)', 'elanditho (oma-)'],
         'auctioneer': ['omulandithi (aa-)'], 'August': ['Auguste'], 'aunt': ['kuku (-oo)', 'memegona (-oo)'],
         'Australia': ['Australia'], 'Australian': ['Omwaaustralia (Aayaustralia)'], 'Austria': ['Austria'],
         'Austrian': ['Omwaaustria (Aayaustria)'], 'authority': ['oompango', 'oonkondo'], 'autumn':
         ['(April - May)', 'oshikufuthinge (ii-)'], 'avocado': ['oshiavokado (iiy-)'], 'awl': ['oniho (oo-)'],
         'axe': ['ekuya (oma-)'], 'axle': ['oakiseli (oo-)', 'oakisa (oo-) '], 'axis': ['oakiseli (oo-)'],
         'awareness': ['enongelo'], 'awakening': ['ependuko']
         }

def translateWord(word, dictionary):
    notInDictionary = 'Word not in dictionary'
    if word in dictionary:
        return dictionary[word]
    else:
        return notInDictionary
    
""" def translate(sentence):
    translation = ''
    word = ''
    punctMarks = ' .,;:!()/?'
    punctuation = ''
   
    for c in sentence:
        if c not in punctMarks:
            word = word + c

        else:
##            if c in punctMarks:
                punctuation = c
                translation = translation + translateWord(word, EtoOsh) + punctuation
                punctuation = ''              
                word = ''

    return translation[:] + ' ' + translateWord(word, EtoOsh) + punctuation
 """
##print(translate('John, sometimes, eats bread.'))
##print(translate('Eric: drinks wine!'))
##print(translate('Everyone (likes) 6.00?'))
loopControl = 'p'
while loopControl != 'x': #A condition to keep the program looping after a translation
    EngWord = input('Enter an English word: ')
    OshWord = translateWord(EngWord, EtoOsh)
    print(OshWord)

##def toChars(s):
##    import string
##    s = string.lower(s)
##    ans = ''
##    for c in s:
##        if c in string.lowercase:
##            ans = ans + c
##    return ans
##
##def isPal(s):
##    if len(s) <= 1:
##        return True
##    else:
##        return s[0] == s[-1] and isPal(s[1:-1])
##
##def isPalindrome(s):
##    """Returns True if s is a palindrome and False otherwise"""
##    return isPal(toChars(s))
##
####print isPalindrome('Guttag')
####print isPalindrome('Guttug')
####print isPalindrome('Able was I ere I saw Elba')
####print isPalindrome('Are we not drawn onward, we few, drawn onward to new era?')
##
##def fib(x):
##    """assumes x an int >= 0
##        Returns Fibonacci of x"""
##    assert type(x) == int and x >=  0
##    if x == 0 or x == 1:
##        return 1
##    else:
##        return fib(x-1) + fib(x-2)
##
##def testFib(n):
##    for i in range(n+1):
##        print ('fib of', i, '=', fib(i))
