import re
from difflib import get_close_matches

class ChatbotMaroc:
    def __init__(self):
        self.connaissances = {
            "casablanca": {
                "mots_cles": ["casablanca", "casa", "dar el beida", "الدار البيضاء"],
                "reponse": """🏙️ **CASABLANCA (الدار البيضاء)**

**Informations générales :**
- Population : ~3,8 millions d'habitants (1ère ville du Maroc)
- Région : Casablanca-Settat
- Capitale économique du Maroc

**Points d'intérêt :**
- 🕌 Mosquée Hassan II : 3ème plus grande mosquée au monde
- 🏖️ Corniche Ain Diab : front de mer avec restaurants et cafés
- 🏛️ Place Mohammed V : architecture art déco
- 🛍️ Morocco Mall : l'un des plus grands centres commerciaux d'Afrique
- 🎭 Quartier des Habous : architecture traditionnelle

**Économie :**
- Port de Casablanca : 1er port du Maroc
- Centre financier et commercial
- Industries : textile, automobile, agroalimentaire

**Culture :**
- Film "Casablanca" (1942) avec Humphrey Bogart
- Mélange architecture mauresque et art déco
- Vie nocturne animée"""
            },
            "rabat": {
                "mots_cles": ["rabat", "الرباط", "capitale"],
                "reponse": """🏛️ **RABAT (الرباط)**

**Informations générales :**
- Population : ~580,000 habitants
- Région : Rabat-Salé-Kénitra
- Capitale politique et administrative du Maroc

**Sites UNESCO :**
- 🏰 Kasbah des Oudayas (12ème siècle)
- 🗼 Tour Hassan et Mausolée Mohammed V
- 🏛️ Site archéologique de Chellah
- 🏘️ Ville nouvelle (architecture moderne)

**Points d'intérêt :**
- 👑 Palais Royal
- 🎨 Musée Mohammed VI d'art moderne
- 🌳 Jardins exotiques
- 🏖️ Plage de Rabat

**Caractéristiques :**
- Ville calme et organisée
- Sièges des institutions gouvernementales
- Centre diplomatique (nombreuses ambassades)
- Patrimoine historique riche"""
            },
            "marrakech": {
                "mots_cles": ["marrakech", "marrakesh", "مراكش", "perle du sud"],
                "reponse": """🌴 **MARRAKECH (مراكش)**

**Informations générales :**
- Population : ~1 million d'habitants
- Région : Marrakech-Safi
- Surnommée "Perle du Sud" ou "Ville Rouge"

**Médina (UNESCO) :**
- 🎪 Place Jemaa el-Fna : cœur battant, acrobates, conteurs
- 🕌 Mosquée Koutoubia : minaret emblématique (77m)
- 🏛️ Palais de la Bahia : architecture somptueuse
- 🌺 Jardins Majorelle : créés par Yves Saint Laurent
- 🏛️ Tombeaux Saadiens

**Souks célèbres :**
- Souk des teinturiers
- Souk des épices
- Souk des bijoutiers

**Tourisme :**
- Destination touristique n°1 du Maroc
- Riads traditionnels
- Gastronomie marocaine authentique
- Proximité Atlas et stations de ski (Oukaïmeden)

**Climat :** Chaud et sec, hiver doux"""
            },
            "fes": {
                "mots_cles": ["fes", "fès", "fez", "فاس"],
                "reponse": """📚 **FÈS (فاس)**

**Informations générales :**
- Population : ~1,2 million d'habitants
- Région : Fès-Meknès
- Capitale spirituelle et culturelle du Maroc

**Médina de Fès el-Bali (UNESCO) :**
- Plus grande zone piétonne au monde
- Plus de 9,000 ruelles
- Fondée au 9ème siècle

**Sites majeurs :**
- 🎓 Université Al Quaraouiyine : plus ancienne université au monde (859)
- 🏫 Medersa Bou Inania : chef-d'œuvre architecture mérinide
- 🎨 Tanneries Chouara : tannage traditionnel du cuir
- 🕌 Mosquée Al-Andalous
- 🏛️ Palais Royal (Dar el-Makhzen)

**Artisanat :**
- Cuir de Fès (maroquinerie)
- Céramique et zellige
- Broderie traditionnelle

**Culture :**
- Festival de Fès des Musiques Sacrées du Monde
- Centre d'enseignement religieux important"""
            },
            "tanger": {
                "mots_cles": ["tanger", "tangier", "طنجة"],
                "reponse": """⚓ **TANGER (طنجة)**

**Informations générales :**
- Population : ~950,000 habitants
- Région : Tanger-Tétouan-Al Hoceïma
- Porte de l'Afrique (14 km de l'Europe)

**Géographie :**
- Située au détroit de Gibraltar
- Confluence Méditerranée et Atlantique
- Vue sur côtes espagnoles

**Points d'intérêt :**
- 🏰 Kasbah de Tanger : musée d'art marocain
- 🏛️ Grottes d'Hercule : site mythologique
- 🌊 Cap Spartel : point de rencontre deux mers
- 🎭 Grand Socco : place animée
- 🏖️ Plages : Malabata, Achakkar

**Histoire :**
- Zone internationale (1923-1956)
- Refuge d'artistes : Paul Bowles, William Burroughs
- Port Tanger Med : 1er port en Méditerranée

**Économie :**
- Hub logistique international
- Zone franche industrielle
- Tourisme balnéaire"""
            },
            "agadir": {
                "mots_cles": ["agadir", "أكادير"],
                "reponse": """🏖️ **AGADIR (أكادير)**

**Informations générales :**
- Population : ~680,000 habitants
- Région : Souss-Massa
- Station balnéaire principale du Maroc

**Caractéristiques :**
- 300 jours de soleil par an
- Plage de 10 km
- Ville moderne (reconstruite après séisme 1960)

**Attractions :**
- 🏰 Kasbah d'Agadir Oufella : vue panoramique
- 🐪 Vallée des Oiseaux : parc zoologique
- 🏄 Sports nautiques et surf
- 🐪 Excursions vers Souss-Massa
- 🛍️ Souk El Had : grand marché

**Économie :**
- Tourisme balnéaire international
- Pêche maritime (1er port sardinier du monde)
- Agriculture : agrumes, primeurs

**Proximité :**
- Essaouira (170 km)
- Parc National Souss-Massa
- Villages berbères de l'Atlas"""
            },
            "meknes": {
                "mots_cles": ["meknès", "meknes", "مكناس"],
                "reponse": """👑 **MEKNÈS (مكناس)**

**Informations générales :**
- Population : ~630,000 habitants
- Région : Fès-Meknès
- Ville impériale du Maroc

**Patrimoine UNESCO :**
- Ville historique de Meknès (1996)
- Capitale sous le sultan Moulay Ismail (17ème siècle)

**Monuments :**
- 🚪 Bab Mansour : plus belle porte du Maroc
- 🏛️ Mausolée Moulay Ismail
- 🏛️ Heri es-Souani : greniers et écuries royales
- 🏊 Bassin de l'Agdal
- 🕌 Médina fortifiée

**Proximité :**
- 🏛️ Volubilis : site romain (UNESCO) à 30 km
- 🏘️ Moulay Idriss Zerhoun : ville sainte

**Économie :**
- Agriculture : olives, vin (région Meknès)
- Artisanat : fer forgé, broderie

**Atmosphère :** Plus calme que Fès, authentique"""
            },
            "essaouira": {
                "mots_cles": ["essaouira", "الصويرة", "mogador"],
                "reponse": """🌊 **ESSAOUIRA (الصويرة)**

**Informations générales :**
- Population : ~78,000 habitants
- Région : Marrakech-Safi
- Ancien nom : Mogador

**Médina (UNESCO) :**
- Fortifications du 18ème siècle
- Architecture portugaise et berbère
- Ville côtière fortifiée

**Points d'intérêt :**
- 🏰 Skala de la Ville : remparts avec canons
- 🎨 Port de pêche : bateaux bleus pittoresques
- 🎭 Galeries d'art et ateliers d'artistes
- 🏖️ Plage : windsurf et kitesurf
- 🎵 Festival Gnaoua et Musiques du Monde

**Atmosphère :**
- Ville bohème et artistique
- Climat venteux et frais
- Ambiance décontractée

**Artisanat :**
- Travail du thuya (bois précieux)
- Peinture et art contemporain
- Bijoux berbères

**Proximité :** Îles Purpuraires (ornithologie)"""
            },
            "oujda": {
                "mots_cles": ["oujda", "وجدة"],
                "reponse": """🌅 **OUJDA (وجدة)**

**Informations générales :**
- Population : ~550,000 habitants
- Région : L'Oriental
- Située à la frontière algérienne (15 km)

**Caractéristiques :**
- Carrefour commercial historique
- Porte de l'Orient marocain
- Ville universitaire importante

**Points d'intérêt :**
- 🕌 Grande Mosquée
- 🌳 Parc Lalla Aicha
- 🏛️ Place du 16 Août
- 🎭 Médina traditionnelle
- 🛍️ Boulevard Mohammed V

**Proximité :**
- 🏖️ Saïdia : station balnéaire (60 km)
- 🌊 "Perle Bleue" de la Méditerranée
- 🏞️ Grottes du Chameau

**Culture :**
- Musique raï très présente
- Influence andalouse et orientale
- Festival International Gharnati

**Économie :** Commerce, agriculture, université"""
            },
            "geographie": {
                "mots_cles": ["géographie", "superficie", "frontières", "régions", "climat"],
                "reponse": """🗺️ **GÉOGRAPHIE DU MAROC**

**Situation :**
- Afrique du Nord-Ouest
- Atlantique (ouest) et Méditerranée (nord)
- Détroit de Gibraltar (14 km de l'Europe)

**Superficie :** ~710,850 km² (avec Sahara occidental)

**Frontières :**
- Nord : Espagne (Ceuta et Melilla)
- Est : Algérie
- Sud : Mauritanie

**Relief :**
- 🏔️ Chaînes de l'Atlas : Haut Atlas (4,167m - Toubkal), Moyen Atlas, Anti-Atlas
- 🏜️ Désert du Sahara (sud)
- 🏖️ Plaines côtières atlantiques
- 🏞️ Vallées : Souss, Drâa, Ziz

**Climat :**
- Méditerranéen (nord)
- Océanique (côte atlantique)
- Continental (intérieur)
- Saharien (sud)

**12 Régions :**
Tanger-Tétouan-Al Hoceïma, L'Oriental, Fès-Meknès, Rabat-Salé-Kénitra, Béni Mellal-Khénifra, Casablanca-Settat, Marrakech-Safi, Drâa-Tafilalet, Souss-Massa, Guelmim-Oued Noun, Laâyoune-Sakia El Hamra, Dakhla-Oued Ed-Dahab"""
            },
            "histoire": {
                "mots_cles": ["histoire", "historique", "dynasties", "protectorat", "indépendance"],
                "reponse": """📜 **HISTOIRE DU MAROC**

**Dynasties principales :**
- 788-974 : Idrissides (1ère dynastie islamique)
- 1062-1147 : Almoravides
- 1147-1269 : Almohades (âge d'or)
- 1269-1465 : Mérinides
- 1554-1659 : Saadiens
- 1666-aujourd'hui : Alaouites (dynastie actuelle)

**Période coloniale :**
- 1912-1956 : Protectorat français et espagnol
- Tanger : zone internationale

**Indépendance :**
- 18 novembre 1956 : indépendance du Maroc
- Mohammed V : premier roi de l'indépendance
- Hassan II : 1961-1999
- Mohammed VI : depuis 1999

**Événements clés :**
- 1975 : Marche Verte (récupération Sahara)
- 2011 : Nouvelle Constitution (monarchie constitutionnelle)

**Patrimoine :**
- 9 sites UNESCO au Maroc
- Carrefour des civilisations (berbère, arabe, africaine, européenne)"""
            },
            "culture": {
                "mots_cles": ["culture", "traditions", "festivals", "musique", "artisanat"],
                "reponse": """🎭 **CULTURE MAROCAINE**

**Langues :**
- Arabe (officielle)
- Amazigh/Berbère (officielle depuis 2011)
- Français (très répandu)
- Darija (arabe dialectal marocain)

**Festivals majeurs :**
- 🎵 Festival de Fès des Musiques Sacrées
- 🎬 Festival International du Film de Marrakech
- 🎶 Festival Gnaoua d'Essaouira
- 🌹 Festival des Roses (Kelâat M'Gouna)
- 🏜️ Festival du Désert (Merzouga)

**Musique :**
- Gnaoua, Chaabi, Malhoun
- Raï (oriental)
- Musique andalouse
- Musique amazighe

**Artisanat :**
- 🎨 Zellige (mosaïque)
- 🧶 Tapis berbères
- 🏺 Poterie de Fès et Safi
- 🪵 Thuya d'Essaouira
- 👜 Maroquinerie
- 🪙 Dinanderie

**Gastronomie :**
- Couscous (vendredi)
- Tajine, Pastilla, Harira
- Thé à la menthe (rituel)"""
            },
            "economie": {
                "mots_cles": ["économie", "pib", "industries", "tourisme", "agriculture"],
                "reponse": """💼 **ÉCONOMIE DU MAROC**

**Indicateurs :**
- PIB : ~150 milliards $ (2024)
- Monnaie : Dirham marocain (MAD)
- Économie la plus diversifiée du Maghreb

**Secteurs clés :**

🏭 **Industrie :**
- Automobile (Renault, PSA à Kénitra et Casablanca)
- Aéronautique (Boeing, Bombardier)
- Textile et cuir
- Phosphates (1er exportateur mondial)

🌾 **Agriculture :**
- 14% du PIB
- Agrumes, tomates, olives
- Plan Maroc Vert

✈️ **Tourisme :**
- 10% du PIB
- ~13 millions de visiteurs/an
- Emplois : ~500,000 directs

🏗️ **Infrastructure :**
- TGV Al Boraq (Casa-Tanger)
- Ports : Tanger Med, Casablanca
- Aéroports internationaux modernes

🔋 **Énergies renouvelables :**
- Centrale solaire Noor (Ouarzazate)
- Parcs éoliens (Tarfaya)
- Objectif 52% d'énergie verte d'ici 2030"""
            },
            "sahara": {
                "mots_cles": ["sahara", "désert", "merzouga", "erg chebbi", "zagora", "dunes"],
                "reponse": """🏜️ **DÉSERT DU SAHARA MAROCAIN**

**Principales destinations :**

🐪 **Merzouga & Erg Chebbi :**
- Dunes orangées jusqu'à 150m de hauteur
- Lever/coucher de soleil spectaculaires
- Nuits dans camps berbères
- Excursions chamelières

🌅 **Zagora & M'Hamid :**
- Porte du désert
- Vallée du Drâa
- Kasbahs authentiques
- Panneau "Tombouctou 52 jours"

🏰 **Ouarzazate :**
- "Hollywood d'Afrique"
- Studios de cinéma (Gladiator, Game of Thrones)
- Kasbah Aït Ben Haddou (UNESCO)

**Activités :**
- Randonnées chamelières
- 4x4 dans les dunes
- Sandboard
- Astronomie (ciel pur)
- Rencontre avec nomades

**Climat :**
- Très chaud l'été (+45°C)
- Froid la nuit en hiver
- Meilleure période : oct-avril

**Route des Kasbahs :** Marrakech → Ouarzazate → Vallée du Dadès → Todra → Merzouga"""
            }
        }
        
        self.salutations = ["bonjour", "salut", "hello", "salam", "salam alaykoum", "hi", "bonsoir"]
        self.au_revoir = ["au revoir", "bye", "salut", "à bientôt", "aurevoir", "besslama"]
        
    def normaliser_texte(self, texte):
        """Normalise le texte"""
        texte = texte.lower().strip()
        texte = re.sub(r'[?!.,:;]+', ' ', texte)
        return texte
    
    def trouver_correspondance(self, question):
        """Trouve la meilleure correspondance"""
        question_norm = self.normaliser_texte(question)
        
        # Vérifier les salutations
        if any(salut in question_norm for salut in self.salutations):
            return "salutation"
        
        # Vérifier les au revoir
        if any(bye in question_norm for bye in self.au_revoir):
            return "au_revoir"
        
        # Rechercher dans les mots-clés
        meilleur_score = 0
        meilleur_sujet = None
        
        for sujet, contenu in self.connaissances.items():
            score = sum(1 for mot_cle in contenu["mots_cles"] if mot_cle in question_norm)
            if score > meilleur_score:
                meilleur_score = score
                meilleur_sujet = sujet
        
        return meilleur_sujet if meilleur_score > 0 else None
    
    def obtenir_reponse(self, question):
        """Génère une réponse"""
        correspondance = self.trouver_correspondance(question)
        
        if correspondance == "salutation":
            return """مرحبا بك! Bienvenue ! 🇲🇦

Je suis votre guide virtuel sur le Maroc. Je peux vous renseigner sur :

🏙️ **Villes principales :**
Casablanca, Rabat, Marrakech, Fès, Tanger, Agadir, Meknès, Essaouira, Oujda

📍 **Thématiques :**
- Géographie et régions
- Histoire et dynasties
- Culture et traditions
- Économie
- Désert du Sahara

Comment puis-je vous aider ?"""
        
        if correspondance == "au_revoir":
            return "بسلامة ! Au revoir ! Bon voyage au Maroc ! 🇲🇦✨"
        
        if correspondance and correspondance in self.connaissances:
            return self.connaissances[correspondance]["reponse"]
        
        return f"""Je n'ai pas trouvé d'information spécifique sur ce sujet.

🏙️ **Villes disponibles :**
Casablanca, Rabat, Marrakech, Fès, Tanger, Agadir, Meknès, Essaouira, Oujda

📚 **Autres sujets :**
- Géographie du Maroc
- Histoire et dynasties
- Culture et traditions
- Économie marocaine
- Désert du Sahara

Reformulez votre question avec l'un de ces termes !"""
    
    def afficher_menu(self):
        """Affiche le menu des options"""
        print("\n" + "="*70)
        print("📍 SUJETS DISPONIBLES :")
        print("="*70)
        print("\n🏙️  VILLES :")
        print("   • Casablanca  • Rabat       • Marrakech  • Fès")
        print("   • Tanger      • Agadir      • Meknès     • Essaouira")
        print("   • Oujda")
        print("\n📚 THÉMATIQUES :")
        print("   • Géographie  • Histoire    • Culture    • Économie")
        print("   • Sahara/Désert")
        print("="*70 + "\n")
    
    def lancer(self):
        """Lance le chatbot"""
        print("=" * 70)
        print("      🇲🇦 CHATBOT MAROC - DÉCOUVREZ LE ROYAUME 🇲🇦")
        print("=" * 70)
        print("\nمرحبا! Bienvenue dans votre guide sur le Maroc et ses villes!")
        print("\nCommandes :")
        print("  • 'menu' ou 'aide' : voir tous les sujets")
        print("  • 'quitter' : sortir du chatbot\n")
        
        while True:
            try:
                question = input("Vous : ").strip()
                
                if not question:
                    continue
                
                if question.lower() in ['quitter', 'exit', 'quit', 'q']:
                    print("\nBot : بسلامة ! Bon voyage au Maroc ! 🇲🇦🌟")
                    break
                
                if question.lower() in ['aide', 'menu', 'help']:
                    self.afficher_menu()
                    continue
                
                reponse = self.obtenir_reponse(question)
                print(f"\nBot : {reponse}\n")
                
            except KeyboardInterrupt:
                print("\n\nBot : بسلامة ! Au revoir !")
                break
            except Exception as e:
                print(f"\nErreur : {e}\n")

# Lancement du chatbot
if __name__ == "__main__":
    chatbot = ChatbotMaroc()
    chatbot.lancer()
