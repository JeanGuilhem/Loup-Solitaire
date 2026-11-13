import os

# Limites de l'inventaire (cf. règles "Combien d'objets pouvez-vous transporter")
MAX_WEAPONS = 2
MAX_BACKPACK = 8
MAX_PURSE = 50

# Catalogue des objets du Tome 1. Les clés sont les noms canoniques : les pages peuvent écrire
# "Repas", "REPAS" ou "repas", inventory.canonical_name() retrouve toujours la bonne entrée.
#   type            : "weapon" (2 max), "backpack" (Sac à Dos, 8 max) ou "special" (Objets Spéciaux)
#   mastery         : arme de référence pour la Maîtrise des armes (ex: LANCE DE GLOK -> LANCE)
#   heal            : ENDURANCE rendue quand l'objet est utilisé (consommé)
#   combat_hability : bonus d'HABILETÉ pour la durée d'un combat (consommé)
#   combat_bonus    : bonus d'HABILETÉ à chaque combat tant que l'objet est porté (non consommé)
#   endurance_bonus : bonus au total d'ENDURANCE tant que l'objet est porté
#   slots           : {tome: places} places prises dans le Sac à Dos dans ce tome (1 sinon)
#   ranged          : arme de tir (Arc) : inutile au corps à corps
#   bow_bonus       : arc qui ajoute ce bonus au chiffre de la Table de Hasard à chaque tir
ITEMS = {
    # --- Armes ---
    "POIGNARD": {"type": "weapon", "mastery": "POIGNARD", "description": "Arme."},
    "LANCE": {"type": "weapon", "mastery": "LANCE", "description": "Arme."},
    "MASSE D'ARMES": {"type": "weapon", "mastery": "MASSE D'ARMES", "description": "Arme."},
    "SABRE": {"type": "weapon", "mastery": "SABRE", "description": "Arme."},
    "MARTEAU DE GUERRE": {"type": "weapon", "mastery": "MARTEAU DE GUERRE", "description": "Arme."},
    "ÉPÉE": {"type": "weapon", "mastery": "ÉPÉE", "description": "Arme."},
    "HACHE": {"type": "weapon", "mastery": "HACHE", "description": "Arme."},
    "BÂTON": {"type": "weapon", "mastery": "BÂTON", "description": "Arme."},
    "GLAIVE": {"type": "weapon", "mastery": "GLAIVE", "description": "Arme."},
    "LANCE DE GLOK": {"type": "weapon", "mastery": "LANCE", "description": "Une lance de Glok."},
    "ÉPÉE DU PRINCE": {"type": "weapon", "mastery": "ÉPÉE", "description": "L'épée du Prince Pellagayo."},
    # --- Sac à Dos ---
    "REPAS": {
        "type": "backpack",
        "description": "S'il ne vous reste plus de vivres lorsque vous devez prendre un Repas, "
        "vous perdez 3 points d'ENDURANCE. Chaque Repas compte pour un objet.",
    },
    "POTION DE GUÉRISON": {
        "type": "backpack",
        "heal": 4,
        "description": "Vous rend 4 points d'ENDURANCE. Une seule dose.",
    },
    "LAUMSPUR": {
        "type": "backpack",
        "heal": 3,
        "description": "Herbe rare aux vertus curatives. Chaque dose vous rend 3 points d'ENDURANCE.",
    },
    "TORCHE": {"type": "backpack", "description": "Un fagot de branches enduit de poix."},
    "LANTERNE": {"type": "backpack", "description": "Une lanterne pour éclairer les lieux obscurs."},
    "BRIQUET À AMADOU": {"type": "backpack", "description": "Pour allumer un feu ou une torche."},
    "SAVON PARFUMÉ": {"type": "backpack", "description": "Un morceau de savon parfumé."},
    "MESSAGE": {"type": "backpack", "description": "Un message écrit sur une peau d'animal."},
    "PIERRE PRÉCIEUSE": {
        "type": "backpack",
        "description": "Une Pierre de cette taille doit valoir une bonne centaine de Couronnes.",
    },
    # --- Objets Spéciaux ---
    "CARTE GÉOGRAPHIQUE": {
        "type": "special",
        "description": "Une carte de la région, rangée dans une poche intérieure de votre tunique.",
    },
    "CASQUE": {
        "type": "special",
        "endurance_bonus": 2,
        "description": "Il ajoute 2 points d'ENDURANCE à votre total. Vous en êtes coiffé.",
    },
    "COTTE DE MAILLES": {
        "type": "special",
        "endurance_bonus": 4,
        "description": "Elle ajoute 4 points d'ENDURANCE à votre total. Vous en êtes vêtu.",
    },
    "CLÉ D'ARGENT": {"type": "special", "description": "Une petite clé faite en argent."},
    "CLÉ D'OR": {"type": "special", "description": "Une clé en or."},
    "PARCHEMIN": {"type": "special", "description": "Un rouleau de parchemin."},
    "PENDENTIF À L'ÉTOILE DE CRISTAL": {
        "type": "special",
        "description": "Symbole de la Confrérie de l'Étoile de Cristal, offert par Banedon.",
    },
    "PIERRES PRÉCIEUSES": {
        "type": "special",
        "description": "Vingt Pierres Précieuses, rangées dans votre bourse.",
    },
    # --- Tome 2 : Sac à Dos ---
    "PETITE POTION DE GUÉRISON": {
        "type": "backpack",
        "heal": 3,
        "description": "Potion de Guérison : une dose qui vous redonne 3 points d'ENDURANCE si vous la buvez après un combat.",
    },
    "FIOLE DE LAUMSPUR": {
        "type": "backpack",
        "heal": 5,
        "description": "Une puissante potion de guérison : 5 points d'ENDURANCE si vous la buvez après un combat. Une seule dose.",
    },
    "MOISSON DE LAUMSPUR": {
        "type": "backpack",
        "description": "L'équivalent d'un Repas, qui vous rendra 3 points d'ENDURANCE lorsque vous le prendrez.",
    },
    "COUVERTURE": {"type": "backpack", "description": "Une couverture."},
    "COUVERTURE DE FOURRURE": {
        "type": "backpack",
        "slots": {3: 2},
        "description": "De chaudes couvertures de fourrure. À Kalte, elles prennent la place de 2 objets.",
    },
    "CORDE": {
        "type": "backpack",
        "slots": {3: 2},
        "description": "Un long rouleau de corde. À Kalte, elle prend la place de 2 objets.",
    },
    "ANNEAU D'OR": {"type": "backpack", "description": "Un anneau d'or."},
    "FIOLE DE LIQUIDE ORANGE": {"type": "backpack", "description": "Une fiole d'un liquide orange."},
    # --- Tome 2 : Objets Spéciaux ---
    "GLAIVE DE SOMMER": {
        "type": "special",
        "weapon": True,
        "mastery": "ÉPÉE",
        "combat_bonus": 8,
        "description": "L'Épée du Soleil : +8 points d'HABILETÉ au combat (+10 avec la Maîtrise de l'Épée). "
        "Elle annule la magie ennemie et double les pertes d'ENDURANCE des morts vivants.",
    },
    "LANCE MAGIQUE": {
        "type": "special",
        "weapon": True,
        "mastery": "LANCE",
        "description": "Une lance de métal gravée de runes, aussi légère que du bois. Elle peut blesser les Monstres d'Enfer.",
    },
    "BILLET DE DILIGENCE": {"type": "special", "description": "Un billet de diligence pour Port Bax."},
    "LAISSEZ-PASSER BLANC": {
        "type": "special",
        "description": "Un laissez-passer de marchand, valable sept jours.",
    },
    "LAISSEZ-PASSER ROUGE": {
        "type": "special",
        "description": "Le laissez-passer qui ouvre le quartier maritime de Port Bax.",
    },
    "DOCUMENTS": {
        "type": "special",
        "description": "Une enveloppe de papiers officiels (ou qui semblent tels) pour obtenir un laissez-passer rouge.",
    },
    "SCEAU D'HAMMARDAL": {
        "type": "special",
        "description": "Un anneau que vous portez à un doigt de votre main droite.",
    },
    "BOUCLIER": {
        "type": "special",
        "combat_bonus": 2,
        "description": "Il vous donne 2 points d'HABILETÉ supplémentaires lorsque vous en faites usage "
        "au cours d'un combat.",
    },
    # --- Tome 3 : Sac à Dos ---
    "POTION DE LAUMSPUR": {
        "type": "backpack",
        "heal": 4,
        "description": "Potion de Guérison : 4 points d'ENDURANCE si vous la buvez à la fin d'un combat. Une seule dose.",
    },
    "TENTE": {"type": "backpack", "slots": {3: 3}, "description": "Une tente polaire. Elle prend la place de 3 objets."},
    "POTION D'ALETHER": {
        "type": "backpack",
        "combat_hability": 4,
        "description": "Potion de Force : +4 points d'HABILETÉ pour la durée d'un seul combat. À boire juste avant.",
    },
    "POTION DE BROSSE À POTENCES": {
        "type": "backpack",
        "description": "Potion verte de « Dent de Sommeil » : un puissant somnifère.",
    },
    "POTION DE RONCES DES CIMETIÈRES": {
        "type": "backpack",
        "description": "Potion noire de Ronces des Cimetières distillées : un poison puissant.",
    },
    # --- Tome 3 : Objets Spéciaux ---
    "GILET DE CUIR MATELASSÉ": {
        "type": "special",
        "endurance_bonus": 2,
        "description": "Il ajoute 2 points d'ENDURANCE à votre total. Vous le portez sur vous.",
    },
    "POTION ROUGE DE LAUMSPUR": {
        "type": "special",
        "heal": 5,
        "description": "Décoction concentrée de Laumspur : 5 points d'ENDURANCE. Une seule dose.",
    },
    "CASQUE D'ARGENT": {
        "type": "special",
        "combat_bonus": 2,
        "description": "Un casque magique, léger malgré sa taille : +2 points d'HABILETÉ au combat.",
    },
    "ÉPÉE D'OS": {
        "type": "special",
        "weapon": True,
        "mastery": "ÉPÉE",
        "description": "Une épée taillée dans l'os par les Barbares des Glaces.",
    },
    "DISQUE DE PIERRE BLEUE": {"type": "special", "description": "Un étrange disque de pierre bleue."},
    "TRIANGLE DE PIERRE BLEUE": {
        "type": "special",
        "description": "Un petit triangle de pierre bleue, attaché à une chaînette passée à votre cou.",
    },
    "BRACELET D'OR": {
        "type": "special",
        "description": "Un bracelet lisse, sans marque ni inscription, en or massif. Vous le portez au poignet.",
    },
    "EFFIGIE": {
        "type": "special",
        "description": "Une statuette de pierre représentant une étrange créature dotée de tentacules.",
    },
    "DIAMANT": {
        "type": "special",
        "description": "Un magnifique diamant qui vaudrait des milliers de Couronnes au Sommerlund.",
    },
    "SPHÈRE DE FEU": {
        "type": "special",
        "description": "Deux demi-sphères de métal qui renferment un feu perpétuel.",
    },
    "PIERRE RAYONNANTE": {"type": "special", "description": "Une pierre tiède aux facettes étincelantes."},
    # --- Tome 4 : Sac à Dos ---
    "FOUET": {"type": "backpack", "description": "Un fouet trouvé suspendu à une porte de fer."},
    "PELLE": {"type": "backpack", "slots": {4: 2}, "description": "Une pelle de mineur. Elle prend la place de 2 objets."},
    "PIOCHE": {"type": "backpack", "slots": {4: 2}, "description": "Une pioche de mineur. Elle prend la place de 2 objets."},
    "SABLIER": {"type": "backpack", "description": "Un sablier."},
    "FIOLE D'ALÉTHER": {
        "type": "backpack",
        "combat_hability": 2,
        "description": "Potion d'Aléther : +2 points d'HABILETÉ pour la durée d'un seul combat.",
    },
    # --- Tome 4 : Armes ---
    "ÉPÉE DE GAYAL": {
        "type": "weapon",
        "mastery": "ÉPÉE",
        "description": "Une épée de la cavalerie du Sommerlund gravée « Capitaine Rinir Gayal, régiment de la Garde du Roi ».",
    },
    "AMULETTE DE BOIS": {
        "type": "backpack",
        "description": "Un petit poisson de bois, symbole de l'Ordre Saint des Rédempteurs.",
    },
    # --- Tome 5 ---
    "GRANDE ÉPÉE": {"type": "weapon", "mastery": "ÉPÉE", "description": "Arme."},
    "HUILE DE LARNUMA": {"type": "backpack", "heal": 2, "description": "Huile de Larnuma : 2 points d'ENDURANCE par dose."},
    "ÉLIXIR DE RENDALIM": {"type": "backpack", "heal": 6, "description": "Élixir de Rendalim : 6 points d'ENDURANCE par dose."},
    "KOURSHAH": {"type": "backpack", "heal": 4, "description": "Une bouteille de Kourshah : 4 points d'ENDURANCE."},
    "POTION D'HERBE À POTENCE": {"type": "backpack", "description": "Chaque dose procure un sommeil d'une ou deux heures."},
    "TEINTURE DE CALACENA": {"type": "backpack", "description": "Une dose produit de terribles hallucinations pendant une heure ou deux."},
    "SARBACANE": {"type": "backpack", "description": "Une sarbacane de guerrier vassagonien."},
    "FLÈCHE DE SOMMEIL": {"type": "backpack", "description": "Une fléchette de sarbacane enduite d'un puissant somnifère."},
    "SERVIETTE": {"type": "backpack", "slots": {5: 2}, "description": "Une grande serviette de bain. Elle prend la place de 2 objets."},
    "PEIGNE D'ARGENT": {"type": "backpack", "description": "Un peigne d'argent."},
    "SIFFLET DE CUIVRE": {"type": "backpack", "description": "Un sifflet de cuivre attaché à une chaîne."},
    "GOURDE": {"type": "backpack", "description": "Une gourde d'eau."},
    "PALETOT": {"type": "backpack", "description": "Un paletot criard en toile grossière, à rayures roses et orange."},
    "HERBE D'OEDE": {
        "type": "special",
        "heal": 10,
        "description": "Herbe d'Oede : elle guérit de nombreuses maladies mortelles, ou rend 10 points d'ENDURANCE.",
    },
    "BRASSARD NOIR": {"type": "special", "description": "Un brassard de crêpe noir, porté en signe de deuil."},
    "PRISME": {"type": "special", "description": "Un prisme de cristal."},
    "MASQUE D'HERBES": {"type": "special", "description": "Un petit masque d'herbes à l'odeur agréable, qui protège la bouche."},
    "CLÉS DU GEÔLIER": {"type": "special", "description": "Les clés du geôlier, accrochées à votre ceinture."},
    "CUBE DE CRISTAL NOIR": {"type": "special", "description": "Un cube de cristal noir trouvé sur un Drakkar."},
    "MASSE D'ARMES INCRUSTÉE": {
        "type": "special",
        "weapon": True,
        "mastery": "MASSE D'ARMES",
        "description": "Une masse d'armes incrustée de pierreries : une arme magique.",
    },
    "LIVRE DU MAGNAKAÏ": {
        "type": "special",
        "description": "Le Livre du Magnakaï, recueil perdu de la sagesse des grands Maîtres Kaï.",
    },
    # --- Tome 4 : Objets Spéciaux ---
    "MÉDAILLON D'ONYX": {"type": "special", "description": "Un magnifique médaillon d'onyx, arraché à l'armure d'un guerrier ennemi."},
    "EAU BÉNITE": {"type": "special", "description": "Un petit flacon de terre cuite rempli d'Eau Bénite."},
    "ROULEAU DE PARCHEMIN": {
        "type": "special",
        "description": "Le parchemin du vieux devin : une prophétie sur la vierge aux cheveux blonds et les morts du gouffre de Maaken.",
    },
    "CLÉ DE CUIVRE": {"type": "special", "description": "Une clé de cuivre."},
    "CLÉ DE FER": {"type": "special", "description": "Une clé de fer."},
    "POIGNARD DE VASHNA": {
        "type": "special",
        "description": "L'arme maudite de Vashna : tant que vous la possédez, le Maître des Ténèbres et ses légions "
        "restent prisonniers du gouffre maudit.",
    },
    "ESSENCE D'ALETHER": {
        "type": "special",
        "combat_hability": 2,
        "description": "Augmente votre HABILETÉ de 2 points pendant toute la durée d'un affrontement. Une seule dose.",
    },
    # --- Tome 6 ---
    "ARC": {
        "type": "weapon",
        "mastery": "ARC",
        "ranged": True,
        "description": "Arme de tir : il faut un Carquois et des flèches. Au corps à corps, il ne sert à rien "
        "(vous combattez à mains nues, -4 HABILETÉ).",
    },
    "CARQUOIS": {
        "type": "special",
        "arrows": 6,
        "description": "Il contient des flèches pour votre Arc (6 au plus). Vous le portez en bandoulière.",
    },
    "CUIRASSE DE CUIR": {
        "type": "special",
        "endurance_bonus": 2,
        "description": "Elle ajoute 2 points d'ENDURANCE à votre total. Vous la portez sur vous.",
    },
    "ARC EN CHÊNE": {
        "type": "weapon",
        "mastery": "ARC",
        "ranged": True,
        "bow_bonus": 3,
        "description": "Le prix du tournoi de tir à l'arc (l'« Arc en Argent » de Duadon) : +3 au chiffre de la "
        "Table de Hasard à chaque tir.",
    },
    "MARTEAU DE GUERRE DE BRONIN": {
        "type": "weapon",
        "mastery": "MARTEAU DE GUERRE",
        "combat_bonus": 1,
        "description": "Un marteau en bronin, métal qui ne se ternit jamais : +1 HABILETÉ quand vous combattez avec.",
    },
    "EAU DE TAUNOR": {
        "type": "backpack",
        "heal": 6,
        "description": "Un flacon d'eau de la source de Taunor, aux vertus régénérantes : 6 points d'ENDURANCE.",
    },
    "FLACON DE LAUMSPUR": {
        "type": "backpack",
        "heal": 3,
        "description": "Un flacon de Potion de Laumspur trouvé sur Chanda : 3 points d'ENDURANCE.",
    },
    "BAIES D'ALETHER": {
        "type": "backpack",
        "combat_hability": 2,
        "description": "Une poignée de baies d'Alether : +2 HABILETÉ pour un combat (une poignée par combat).",
    },
    "CONCENTRÉ DE CHIENDENT DES CIMETIÈRES": {"type": "backpack", "description": "Un poison foudroyant."},
    "PASS": {"type": "special", "description": "Un carton bleu daté du jour : il donne accès à Amory pour la journée."},
    "CLÉ EN ARGENT": {"type": "special", "description": "La clé que vous a remise Gwynian."},
    "PLAN DE VARETTA": {"type": "special", "description": "Un plan de la ville de Varetta."},
    "PLAN DE TEKARO": {"type": "backpack", "description": "Un plan de la ville de Tekaro, dans un étui de cuir."},
    "CARTE DE TEKARO": {"type": "backpack", "description": "Une carte de Tekaro, achetée à Luyen."},
    "CARTE DE LUYEN": {"type": "backpack", "description": "Une carte de Luyen."},
    "CARTE DU SOMMERLUND": {"type": "backpack", "description": "Une carte du Sommerlund."},
    "BAGUE EN RUBIS": {"type": "special", "description": "Une bague ornée d'un rubis."},
    "BROCHE EN ARGENT": {"type": "special", "description": "Une broche en argent."},
    "BOUTEILLE DE VIN": {"type": "backpack", "description": "Une bouteille de vin."},
    "MIROIR": {"type": "backpack", "description": "Un petit miroir."},
    "BILLET POUR LUYEN": {"type": "special", "description": "Billet du bateau Kazonara, de Soren à Luyen."},
    "BILLET POUR RHEM": {"type": "special", "description": "Billet du bateau Kazonara, de Soren à Rhem."},
    "BILLET POUR EULA": {"type": "special", "description": "Billet du bateau Kazonara, de Soren à Eula."},
    # --- Tome 7 ---
    "GRAINE DE FEU": {
        "type": "special",
        "description": "Jetée sur une surface dure, elle explose puis brûle d'un feu vif. Vous les gardez dans votre poche.",
    },
    "CLÉ DE POUVOIR": {"type": "special", "description": "Une clé chargée de magie, remise par les Anciens Mages."},
    "AMULETTE EN PLATINE": {
        "type": "special",
        "description": "Portée au poignet, elle vous protège contre toute exposition à de très hautes températures.",
    },
    "PASSE-PARTOUT": {"type": "special", "description": "Une clé qui ouvre bien des serrures."},
    "SIFFLET D'ARGENT": {"type": "special", "description": "Un sifflet d'argent au bout d'une chaîne : aucun son n'en sort."},
    "BOUTEILLE D'EAU": {"type": "backpack", "description": "Une bouteille d'eau."},
    "FIOLE DE PILULES BLEUES": {"type": "backpack", "description": "Une fiole de petites pilules bleues."},
    "SACHET D'HERBES": {"type": "backpack", "description": "Un sachet d'herbes inconnues."},
    "ADGANA": {
        "type": "backpack",
        "combat_hability": 6,
        "description": "Feuilles d'Adgana : +6 HABILETÉ pour un combat. Elles créent une accoutumance : après le combat, "
        "un 0 ou un 1 à la Table de Hasard vous fait perdre 4 points d'ENDURANCE définitivement.",
    },
    "HABIT ROUGE": {"type": "backpack", "description": "Un habit rouge à capuchon, trouvé sur un mercenaire Kakush."},
    "FLASQUE DE VIN": {"type": "backpack", "description": "Une flasque de vin."},
    "POTION DE LAUMSPUR CONCENTRÉE": {
        "type": "backpack",
        "heal": 8,
        "description": "Une grosse bouteille de solution concentrée de Laumspur : 8 points d'ENDURANCE.",
    },
}

# Table de Hasard (0 à 9) -> arme maîtrisée (cf. "La Maîtrise des armes")
WEAPON_MASTERY_TABLE = [
    "POIGNARD",
    "LANCE",
    "MASSE D'ARMES",
    "SABRE",
    "MARTEAU DE GUERRE",
    "ÉPÉE",
    "HACHE",
    "ÉPÉE",
    "BÂTON",
    "GLAIVE",
]

# Table de Hasard (0 à 9) -> objet trouvé dans les ruines du monastère (cf. "Équipement")
STARTING_ITEM_TABLE = {
    1: "ÉPÉE",
    2: "CASQUE",
    3: "REPAS",  # deux Repas
    4: "COTTE DE MAILLES",
    5: "MASSE D'ARMES",
    6: "POTION DE GUÉRISON",
    7: "BÂTON",
    8: "LANCE",
    9: 12,  # douze Couronnes
    0: "GLAIVE",
}

# Les tomes de la série : dossier des pages (tomes/tome<N>/), titre, paragraphe final (= victoire)
BOOKS = {
    1: {"title": "Les Maîtres des Ténèbres", "final_page": 350},
    2: {"title": "La Traversée Infernale", "final_page": 350},
    3: {"title": "Les Grottes de Kalte", "final_page": 350},
    4: {"title": "Le Gouffre Maudit", "final_page": 350},
    5: {"title": "Le Tyran du Désert", "final_page": 400},
    6: {"title": "La Pierre de la Sagesse", "final_page": 350},
    7: {"title": "La Forteresse Maudite", "final_page": 350},
}

# Jalons : 3 paragraphes par tome où se croisent la plupart des routes (passages obligés vers la
# fin du tome, ou à défaut les plus fréquentés). Le héros y est sauvegardé à son arrivée ; s'il meurt
# plus loin, il peut reprendre au dernier jalon atteint (cf. save.save_milestone).
MILESTONES = {
    1: [157, 303, 129],
    2: [197, 150, 349],
    3: [235, 323, 56],
    4: [120, 200, 148],
    5: [67, 221, 272],
    6: [39, 127, 249],
    7: [164, 100, 282],
}

# Équipement reçu au début de chaque tome à partir du 2 (cf. « Équipement »), par les héros venus
# du tome précédent comme par les nouveaux (cf. book_start.py).
#   gold_base       : Couronnes = gold_base + Table de Hasard, ajoutées à celles déjà possédées
#   items           : {libellé du choix: (NOM, quantité)}, items_to_choose au choix
#                     (up_to : « jusqu'à » items_to_choose, sinon exactement)
#   special         : Objets Spéciaux remis d'office (sauf s'ils sont déjà possédés)
#   origin          : provenance des objets (fiche de l'écran d'équipement), special_origins par objet
#   place, journey, start_label : textes de la page de départ
BOOK_EQUIPMENT = {
    2: {
        "gold_base": 10,
        "items_to_choose": 2,
        "items": {
            "ÉPÉE": ("ÉPÉE", 1),
            "SABRE": ("SABRE", 1),
            "2 REPAS": ("REPAS", 2),
            "COTTE DE MAILLES": ("COTTE DE MAILLES", 1),
            "MASSE D'ARMES": ("MASSE D'ARMES", 1),
            "POTION DE GUÉRISON": ("POTION DE GUÉRISON", 1),
            "BÂTON": ("BÂTON", 1),
            "LANCE": ("LANCE", 1),
            "GLAIVE": ("GLAIVE", 1),
            "BOUCLIER": ("BOUCLIER", 1),
        },
        # « Au départ de votre quête, vous êtes en possession du Sceau d'Hammardal » et d'une carte
        "special": ["SCEAU D'HAMMARDAL", "CARTE GÉOGRAPHIQUE"],
        "origin": "Tome 2 : Arsenal du Palais de Holmgard, avant le départ pour Durenor.",
        "special_origins": {
            "SCEAU D'HAMMARDAL": "Tome 2 : confié par le roi du Sommerlund pour obtenir l'aide de Durenor.",
        },
        "place": "l'Arsenal",
        "journey": "partir à Durenor",
        "start_label": "Partir pour Durenor",
    },
    3: {
        "gold_base": 10,
        "items_to_choose": 2,
        "items": {
            "ÉPÉE": ("ÉPÉE", 1),
            "SABRE": ("SABRE", 1),
            "GILET DE CUIR MATELASSÉ": ("GILET DE CUIR MATELASSÉ", 1),
            "LANCE": ("LANCE", 1),
            "MASSE D'ARMES": ("MASSE D'ARMES", 1),
            "MARTEAU DE GUERRE": ("MARTEAU DE GUERRE", 1),
            "HACHE": ("HACHE", 1),
            "POTION DE LAUMSPUR": ("POTION DE LAUMSPUR", 1),
            "BÂTON": ("BÂTON", 1),
            "RATIONS SPÉCIALES (1 Repas)": ("REPAS", 1),
            "GLAIVE": ("GLAIVE", 1),
        },
        # bottes, tunique, cape et moufles polaires (sans effet de jeu) et une carte de Kalte
        "special": ["CARTE GÉOGRAPHIQUE"],
        "origin": "Tome 3 : remis à l'Hôtel de Ville d'Anskaven, avant le départ pour Kalte.",
        "special_origins": {},
        "place": "l'Hôtel de Ville",
        "journey": "partir pour Kalte",
        "start_label": "Embarquer pour Kalte",
    },
    # La page « Équipement » du PDF est celle du tome 5 (Barrakeesh). Liste du tome 4 d'après
    # l'édition originale (Project Aon, « The Chasm of Doom ») : jusqu'à 6 objets.
    4: {
        "gold_base": 10,
        "items_to_choose": 6,
        "up_to": True,
        "items": {
            "MARTEAU DE GUERRE": ("MARTEAU DE GUERRE", 1),
            "POIGNARD": ("POIGNARD", 1),
            "2 POTIONS DE LAUMSPUR": ("POTION DE LAUMSPUR", 2),
            "ÉPÉE": ("ÉPÉE", 1),
            "LANCE": ("LANCE", 1),
            "5 RATIONS SPÉCIALES (5 Repas)": ("REPAS", 5),
            "MASSE D'ARMES": ("MASSE D'ARMES", 1),
            "COTTE DE MAILLES": ("COTTE DE MAILLES", 1),
            "BOUCLIER": ("BOUCLIER", 1),
        },
        "special": ["CARTE GÉOGRAPHIQUE"],
        "origin": "Tome 4 : Armurerie Royale de Holmgard, avant le départ pour Ruanon.",
        "special_origins": {},
        "place": "l'Armurerie Royale",
        "journey": "partir pour Ruanon",
        "start_label": "Partir pour Ruanon",
    },
    5: {
        "gold_base": 10,
        "items_to_choose": 6,
        "up_to": True,
        "items": {
            "POIGNARD": ("POIGNARD", 1),
            "POTION DE LAUMSPUR": ("POTION DE LAUMSPUR", 1),
            "ÉPÉE": ("ÉPÉE", 1),
            "LANCE": ("LANCE", 1),
            "2 RATIONS SPÉCIALES (2 Repas)": ("REPAS", 2),
            "MASSE D'ARMES": ("MASSE D'ARMES", 1),
            "BOUCLIER": ("BOUCLIER", 1),
        },
        "special": ["CARTE GÉOGRAPHIQUE"],  # une carte de la Vassagonie
        "origin": "Tome 5 : remis à Holmgard, avant le départ pour Barrakeesh.",
        "special_origins": {},
        "place": "Holmgard",
        "journey": "partir pour Barrakeesh",
        "start_label": "Embarquer pour Barrakeesh",
    },
    6: {
        "gold_base": 10,
        "items_to_choose": 6,
        "up_to": True,
        "items": {
            "ÉPÉE": ("ÉPÉE", 1),
            "POTION DE LAUMSPUR": ("POTION DE LAUMSPUR", 1),
            "MARTEAU DE GUERRE": ("MARTEAU DE GUERRE", 1),
            "ARC": ("ARC", 1),
            "CARQUOIS (6 flèches)": ("CARQUOIS", 1),
            "4 RATIONS SPÉCIALES (4 Repas)": ("REPAS", 4),
            "BÂTON": ("BÂTON", 1),
            "CUIRASSE DE CUIR": ("CUIRASSE DE CUIR", 1),
            "CORDE": ("CORDE", 1),
            "POIGNARD": ("POIGNARD", 1),
            "BRIQUET À AMADOU": ("BRIQUET À AMADOU", 1),
            "HACHE": ("HACHE", 1),
        },
        "special": ["CARTE GÉOGRAPHIQUE"],  # une carte des pays de la Storn
        "origin": "Tome 6 : acheté au Sommerlund, avant le départ pour Varetta.",
        "special_origins": {},
        "place": "Holmgard",
        "journey": "partir en quête de la Pierre de la Sagesse",
        "start_label": "Partir pour les pays de la Storn",
    },
    7: {
        "gold_base": 10,
        "items_to_choose": 5,
        "up_to": True,
        "items": {
            "ÉPÉE": ("ÉPÉE", 1),
            "ARC": ("ARC", 1),
            "CARQUOIS (6 flèches)": ("CARQUOIS", 1),
            "POTION DE LAUMSPUR": ("POTION DE LAUMSPUR", 1),
            "CORDE": ("CORDE", 1),
            "POIGNARD": ("POIGNARD", 1),
            "LANTERNE": ("LANTERNE", 1),
            "MASSE D'ARMES": ("MASSE D'ARMES", 1),
            "3 RATIONS SPÉCIALES (3 Repas)": ("REPAS", 3),
            "3 GRAINES DE FEU": ("GRAINE DE FEU", 3),
        },
        "special": ["CARTE GÉOGRAPHIQUE"],  # une carte du pays des Anciens Mages
        "origin": "Tome 7 : offert par les Anciens Mages d'Elzian.",
        "special_origins": {},
        "place": "Elzian",
        "journey": "partir en quête de la Pierre de la Sagesse de Herdos",
        "start_label": "Partir pour Herdos",
    },
}

KAI = {
    "Le Camouflage": """
Cette technique permet au Seigneur Kaï de se fondre dans le
paysage. A la campagne, il peut se cacher parmi les arbres et les
rochers et se rendre de cette façon invisible à l'ennemi même s'il
passe tout près de lui. Dans une ville, cette discipline donnera à
celui qui l'utilise la faculté d'avoir l'air d'un habitant du cru, tant
par l'apparence que par l'accent ou la langue employée. On peut
ainsi trouver un abri où se cacher en toute sécurité..
""",
    "La Chasse": """Cette discipline donne au Seigneur Kaï l'assurance qu'il ne
mourra jamais de faim même s'il se trouve dans un
environnement hostile. Il aura toujours la possibilité de chasser
pour se procurer de la nourriture, sauf dans les déserts et les
autres régions arides. Cette technique permet également de se
déplacer sans bruit en pistant une proie.
Chasse.
 
 **Vous êtes dispensé de Repas chaque fois
qu'il est obligatoire de manger.**""",
    "Le Sixième Sens": """Grâce à cette technique, le Seigneur Kaï devine les dangers
imminents qui le menacent. Ce Sixième Sens peut également lui
révéler les intentions véritables d'un inconnu ou la nature d'un
objet étrange rencontré au cours d'une aventure.
""",
    "L'Orientation": """
Chaque fois qu'il se trouvera dans l'obligation de décider quelle
direction il doit prendre, le Seigneur Kaï fera toujours le bon
choix grâce à cette technique. Il saura ainsi quel chemin il
convient d'emprunter dans une forêt et il pourra également, dans
une ville, découvrir l'endroit où sont cachés une personne ou un
objet. Par ailleurs, il saura interpréter chaque trace de pas,
chaque empreinte qui pourrait lui permettre de remonter une
piste.
    """,
    "La Guérison": """Cette discipline donne la faculté de récupérer des points
d'ENDURANCE perdus lors d'un combat. Si vous maîtrisez cette
technique, vous pourrez ajouter 1 point d'ENDURANCE à votre
total à chaque fois qu'il vous sera possible d'aller d'un bout à
l'autre d'un paragraphe sans avoir à combattre un ennemi. (Vous
n'aurez droit d'utiliser cette technique de la Guérison que lorsque
vos points d'ENDURANCE seront tombés au-dessous de votre
total initial. Rappelez-vous que vos points d'ENDURANCE ne
peuvent en aucun cas excéder votre total de départ).

**1 point d'ENDURANCE pour chaque paragraphe
parcouru sans combat (automatiquement rendu)**.
""",
    "La Maîtrise des armes": """En entrant au Monastère Kaï, chaque élève a la possibilité d'être
initié au maniement d'une arme. Si vous choisissez d'avoir la
Maîtrise d'une arme, il sera déterminé au hasard quelle(s) arme(s) profiteront de cette Maîtrise.

**Vous en aurez dès lors la parfaite Maîtrise  et chaque fois que vous combattrez avec elle, vous aurez
droit à 2 points d'HABILETÉ supplémentaires**.

Voici la liste des armes disponibles: la lance, le poignard, la masse d'arme, le sabre, le marteau de guerre, l'épée, la hache, le baton et le glaive.
Le fait que vous possédiez la maîtrise d'une arme ne signifie
nullement que vous disposerez de cette arme dès le départ de
votre aventure. Sauf exception, c'est au cours de celle-ci que les
occasions vous seront données de vous procurer les armes qui
vous conviennent.
""",
    "Bouclier psychique": """
Les Maîtres des Ténèbres et les nombreuses créatures
malfaisantes qui leur obéissent ont la faculté de vous porter
atteinte en faisant usage de leur force psychique. La technique du
Bouclier psychique vous permet cependant de ne pas perdre de
points d'ENDURANCE lorsque vous vous trouvez soumis à une
telle agression.""",
    "Puissance psychique": """Cette technique permet au Seigneur Kaï d'attaquer un ennemi en
se servant de la force de son esprit. 

**On peut l'utiliser en même
temps qu'une arme de combat habituelle et l'on dispose alors de
2 points supplémentaires d'HABILETÉ**.
 
Cette puissance
psychique, cependant, n'est pas forcément efficace avec toutes les
créatures: il se peut que certaines d'entre elles y soient
insensibles. Si le cas se présente, vous en serez averti au cours de
votre mission.""",
    "Communication Animale": """Grâce à cette technique, un Seigneur Kaï peut communiquer avec
certains animaux et deviner les intentions de certains autres.""",
    "Maîtrise Psychique de la Matière": """C'est une technique qui donne à un Seigneur Kaï la faculté de
déplacer de petits objets par le simple pouvoir de sa
concentration mentale. Si vous choisissez cette discipline,
inscrivez : Maîtrise Psychique de la Matière sur votre Feuille
d'Aventure. Si vous remplissez avec succès la mission qui vous
est assignée dans ce premier livre de la série du Loup Solitaire,
vous aurez le droit d'ajouter une Discipline Kaï supplémentaire à
celles que vous possédez déjà. Lorsque vous vous lancerez dans
la nouvelle aventure que vous propose le prochain volume de la
série (intitulé La Traversée Infernale), vous pourrez ainsi faire
usage de six disciplines Kaï (les cinq premières étant acquises
une bonne fois pour toutes), de même que des Objets Spéciaux
que vous aurez décidé de conserver au cours de votre première
mission. Sachez en effet que, de livre en livre, votre expérience
grandira chaque fois que vous aurez accompli une mission : vous
pourrez, de cette façon, espérer atteindre un jour la complète
maîtrise de l'art et de la science des Moines Kaï."""
}

# Cartes du choix des Disciplines Kaï (création du héros) : icône et résumé d'une ligne.
# Le texte complet de chaque Discipline reste dans KAI (onglet « Maîtrise Kaï »).
KAI_CARDS = {
    "Le Camouflage": ("🍃", "Vous fondre dans le paysage ou passer pour un habitant."),
    "La Chasse": ("🏹", "Ne jamais manquer de nourriture, et vous déplacer sans bruit."),
    "Le Sixième Sens": ("👁️", "Pressentir les dangers et deviner les intentions cachées."),
    "L'Orientation": ("🧭", "Toujours trouver le bon chemin, même sans carte."),
    "La Guérison": ("🌿", "Regagner 1 point d'ENDURANCE à chaque paragraphe sans combat."),
    "La Maîtrise des armes": ("⚔️", "+2 HABILETÉ avec l'arme tirée au sort pendant votre initiation."),
    "Bouclier psychique": ("🛡️", "Ne rien perdre face aux attaques mentales de l'ennemi."),
    "Puissance psychique": ("🧠", "+2 HABILETÉ en combat en frappant aussi par la pensée."),
    "Communication Animale": ("🐺", "Comprendre certains animaux et leur parler."),
    "Maîtrise Psychique de la Matière": ("🔮", "Déplacer de petits objets par la seule force de l'esprit."),
}

# --------------------------------------------------------------------------------------
# Série Magnakaï (à partir du tome 6) : seules les Disciplines Magnakaï comptent, les Disciplines
# Kaï restent sur la Feuille d'Aventure sans effet (règle officielle).
# --------------------------------------------------------------------------------------
MAGNAKAI_FROM = 6
MAGNAKAI_START = 3  # Disciplines Magnakaï au tome 6, une de plus par tome terminé
MAGNAKAI_WEAPONS_START = 3  # armes de la Science des Armes au tome 6, une de plus par tome terminé
MAGNAKAI_WEAPON_TABLE = [
    "POIGNARD", "LANCE", "MASSE D'ARMES", "SABRE", "MARTEAU DE GUERRE",
    "ARC", "HACHE", "ÉPÉE", "BÂTON", "GLAIVE",
]
MAGNAKAI = {
    "Science des Armes": """Cette Discipline permet à un Maître Kaï d'être habile au
maniement de toutes sortes d'armes. Le rang de Maître Kaï Supérieur qui est le vôtre au début
de cette série des Magnakaï indique que vous avez la parfaite maîtrise de trois armes, à choisir
parmi : le poignard, la lance, la masse d'armes, le sabre, le marteau de guerre, l'arc, la hache,
l'épée, le bâton et le glaive.

**Chaque fois que vous combattrez avec l'une de ces armes, vous aurez droit à 3 points
d'HABILETÉ supplémentaires.** Avec l'Arc, ajoutez 3 au chiffre tiré dans la Table de Hasard.

A chaque fois que vous accomplirez avec succès une mission de la série des Magnakaï, vous
pourrez ajouter une arme à votre liste.""",
    "Contrôle Animal": """Grâce à cette technique, un Maître Kaï peut communiquer avec
certains animaux et deviner les intentions de certains autres. Il peut, en outre, combattre à
cheval dans des conditions très avantageuses.""",
    "Science Médicale": """Cette Discipline donne la faculté de récupérer des points
d'ENDURANCE perdus lors d'un combat. Elle permet aussi à un Maître Kaï de soigner certaines
maladies, de guérir la cécité et toutes sortes de blessures, et lui fait connaître les propriétés
des plantes, des herbes, des racines et des potions.

**1 point d'ENDURANCE pour chaque paragraphe parcouru sans combat (automatiquement rendu)**.""",
    "Invisibilité": """Cette technique permet au Maître Kaï de se fondre dans le
paysage, même dans les terrains les plus exposés. Elle lui donne la possibilité de masquer la
chaleur et l'odeur de son corps, d'adopter les mœurs et de parler le dialecte de n'importe quelle
ville qu'il visite.""",
    "Art de la Chasse": """Cette Discipline donne au Maître Kaï l'assurance qu'il ne mourra
jamais de faim, même dans les déserts et autres régions arides. Par ailleurs, elle lui permet de
se déplacer très vite et avec agilité, et lui évite de perdre des points d'HABILETÉ lors d'une
attaque surprise ou d'une embuscade.

**Vous êtes dispensé de Repas chaque fois qu'il est obligatoire de manger.**""",
    "Exploration": """C'est la technique qui permet à un Maître Kaï de toujours choisir
le bon chemin, même en territoire inconnu ; il pourra aussi lire les langues étrangères,
décrypter les symboles, reconnaître les empreintes et autres traces et déceler la présence de la
plupart des pièges. Enfin, elle lui permettra de repérer intuitivement le nord.""",
    "Foudroiement Psychique": """Grâce à cette technique, le Maître Kaï peut attaquer un
ennemi par la seule force de son esprit.

**Puissance Psychique : +2 points d'HABILETÉ, sans perte d'ENDURANCE.**

**Foudroiement Psychique : +4 points d'HABILETÉ, mais vous perdez 2 points d'ENDURANCE à chaque
Assaut.** Il ne peut pas être utilisé si votre ENDURANCE est de 6 points ou moins.

Il n'est pas forcément efficace contre toutes les créatures : il se peut que certaines d'entre
elles y soient insensibles. Si le cas se présente, vous en serez averti.""",
    "Écran Psychique": """Certaines créatures malfaisantes de Magnamund ont la faculté de
vous atteindre en faisant usage de leur force psychique.

**Cette Discipline vous évite de perdre des points d'ENDURANCE lors d'une semblable
agression** et elle augmente vos moyens de défense contre l'hypnose et les illusions
supranaturelles.""",
    "Nexus": """La Maîtrise de cette Discipline donne à un Maître Kaï la faculté de
supporter des chaleurs et des froids extrêmes sans perte de point d'ENDURANCE et permet de
déplacer les objets par le seul pouvoir de la concentration mentale.""",
    "Intuition": """C'est la technique qui permet au Maître Kaï de deviner les dangers
imminents qui le menacent et les intentions véritables d'un inconnu ou la nature d'un objet
étrange. L'Intuition donne également la possibilité de communiquer par télépathie avec une autre
personne et de sentir si une créature dispose de pouvoirs psychiques.""",
}
MAGNAKAI_CARDS = {
    "Science des Armes": ("⚔️", "+3 HABILETÉ avec les 3 armes que vous choisissez."),
    "Contrôle Animal": ("🐎", "Parler aux animaux et combattre à cheval."),
    "Science Médicale": ("🌿", "Regagner 1 point d'ENDURANCE à chaque paragraphe sans combat, et soigner."),
    "Invisibilité": ("🍃", "Vous fondre dans le paysage ou passer pour un habitant."),
    "Art de la Chasse": ("🏹", "Ne jamais manquer de nourriture, ni être surpris."),
    "Exploration": ("🧭", "Trouver le bon chemin, lire les langues et déceler les pièges."),
    "Foudroiement Psychique": ("🧠", "+2 HABILETÉ par la pensée, ou +4 au prix de 2 ENDURANCE par assaut."),
    "Écran Psychique": ("🛡️", "Ne rien perdre face aux attaques mentales de l'ennemi."),
    "Nexus": ("🔥", "Résister au feu et au froid, déplacer les objets par l'esprit."),
    "Intuition": ("👁️", "Pressentir les dangers, deviner les intentions, télépathie."),
}
# Cercles de Savoir : Disciplines nécessaires, bonus (HABILETÉ, ENDURANCE) ajoutés aux totaux
LORE_CIRCLES = {
    "Cercle de Feu": (["Art de la Chasse", "Science des Armes"], 1, 2),
    "Cercle de la Lumière": (["Contrôle Animal", "Science Médicale"], 0, 3),
    "Cercle de Solaris": (["Invisibilité", "Art de la Chasse", "Exploration"], 1, 3),
    "Cercle de l'Esprit": (["Foudroiement Psychique", "Écran Psychique", "Nexus", "Intuition"], 3, 3),
}
# Rangs Magnakaï (nombre de Disciplines -> titre)
MAGNAKAI_RANKS = {
    1: "Maître Kaï", 2: "Maître Kaï d'ordre intermédiaire", 3: "Maître Kaï d'ordre supérieur",
    4: "Maître primat", 5: "Maître tutélaire", 6: "Maître principal", 7: "Maître mentor",
    8: "Maître éminent", 9: "Maître transcendant", 10: "Grand Maître Kaï",
}
AI_INSTRUCTION = """
Vous êtes un expert Python/Streamlit. 
Votre tâche est de convertir le contenu brut d'un chapitre du livre "Loup Solitaire" en un script Python 3 formaté pour Streamlit. Vous devez respecter STRICTEMENT toutes les règles de formatage ci-dessous.

1.  Structure Générale: Utiliser la structure de ce template fournie, sans commentaires: 
    #TEMPLATE#

2.  Page Number: Utiliser la variable 'current_page_number' du chapitre fourni en cours.

3.  Texte: Placer le texte narratif dans la variable 'fr_text'. Les choix de redirection doivent en être exclus. Format le text dedans pour ne pas faire qu'une seule ligne en variable.

4.  Redirections Standard: Utiliser 'st.page_link' (fi, fi_1, fi_2, etc.) pour chaque choix.

5.  Actions Uniques (Or, Endurance): Toute action qui modifie l'état (gain/perte d'ENDURANCE, gain d'or) doit être encapsulée dans la condition anti-rerun :
    if st.session_state.last_page_number != st.session_state.current_page_number:
        # Action ici

6.  Gain/Perte d'ENDURANCE: utiliser change_endurance(delta) (importé de inventory), qui gère le plafond et la mort,
    et afficher avec st.metric(label="Endurance", value=..., delta=... ).

    Exemple (pour une perte de 2 ENDURANCE):
    if st.session_state.last_page_number != st.session_state.current_page_number:
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)


7.  Or (Couronnes), importés de inventory :
    * Or donné d'office par le texte (récompense, bourse trouvée...) : receive_gold(montant). Il gère tout seul
      l'anti-rerun et l'affichage (bourse + gain + pop-up) : pas de condition ni de st.metric autour.
    * Or que le joueur « peut prendre » : pickup_gold(montant, key="gold").
    * Paiement : spend_gold(montant) renvoie False si la bourse ne suffit pas. Un choix qui demande de payer
      se fait avec un st.button : if st.button("Payer 10 Couronnes", disabled=st.session_state.purse < 10):
      spend_gold(10) puis st.switch_page("tomes/tome1/page_XXX.py").

8.  Objets à Ramasser: utiliser pickup_button(name, key, label) (importé de inventory). Il gère tout seul
    l'anti-rerun, les limites (8 objets dans le Sac à Dos, 2 armes) et le rangement (Armes, Sac à Dos ou Objets Spéciaux).
    Chaque objet a une key différente ; des boutons qui partagent la même key forment un choix « l'un ou l'autre ».
    Les noms d'objets sont ceux du livre, en majuscules (REPAS, LAUMSPUR, POIGNARD, CLÉ D'OR, SAC À DOS...).
    Exemple (pour deux doses de LAUMSPUR):
        st.write("Vous pouvez ajouter les doses de Laumspur à votre inventaire :")
        pickup_button("LAUMSPUR", key="laumspur_1", label="Prendre une dose de Laumspur")
        pickup_button("LAUMSPUR", key="laumspur_2", label="Prendre une dose de Laumspur")
    Exemple (prendre au choix le Poignard OU une Lance):
        pickup_button("POIGNARD", key="weapon_choice", label="Prendre le Poignard")
        pickup_button("LANCE", key="weapon_choice", label="Prendre une Lance")

8bis. Objets imposés ou perdus (importés de inventory), toujours dans la condition anti-rerun :
    * add_to_inventory("NOM") / remove_from_inventory("NOM") : gagner / perdre un objet précis.
    * has_item("NOM") : tester la possession d'un objet (ex: "Si vous possédez une Clé d'Or").
    * lose_all_weapons() : « vous avez perdu vos Armes ».
    * lose_backpack() : « vous avez perdu votre Sac à Dos » (le sac et son contenu).
    * empty_backpack() : « tout le contenu de votre Sac à Dos est perdu ».
    * choose_item_to_lose(candidats, key="lose") : le joueur choisit l'objet perdu (vol, arme brisée).
      Renvoie True quand c'est réglé ; n'afficher les liens de sortie qu'à ce moment-là.
      Ex (« on vous vole un objet du Sac à Dos, ou une arme si vous n'avez plus de Sac à Dos ») :
        candidats = st.session_state.backpack if st.session_state.backpack else st.session_state.weapons
        if choose_item_to_lose(list(candidats), key="theft"):
            st.page_link("tomes/tome1/page_XXX.py", label="XXX", icon="📄")


9.  Discipline Kaï (Choix):
    * Utiliser la variable 'fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."' en haut du fichier.
    * Pour un choix conditionnel Kai (ex: "rendez-vous au 198"), utiliser has_kai (importé de inventory):
        if has_kai("NOM DE LA DISCIPLINE"):
            st.page_link("tomes/tome1/page_XXX.py", label="XXX", icon="📄")
        else:
            st.write_stream(stream_text(fr_unkown_kai))
            st.page_link("tomes/tome1/page_XXX.py", label="XXX", icon="📄", disabled=True)

    Exemple (pour la Discipline Kaï du Sixième Sens vers 198):
        if has_kai("Le Sixième Sens"):
            st.page_link("tomes/tome1/page_198.py", label="198", icon="📄")
        else:
            st.write_stream(stream_text(fr_unkown_kai))
            st.page_link("tomes/tome1/page_198.py", label="198", icon="📄", disabled=True)

    
10. Combat: utiliser combat() (from combat import combat). Elle affiche l'ennemi, les bonus, les boutons d'assaut
    et de fuite, met à jour l'ENDURANCE et gère la mort. Elle renvoie None tant que le combat n'est pas fini, puis
    "win", "fled", "rounds_over" ou "wounded". N'ajoute aucune autre variable d'état (done_fighting...).

    def combat(
        enemies,                      # [("NOM", HABILETÉ, ENDURANCE), ...] combattus l'un après l'autre
        key="combat",                 # à changer seulement si la page contient deux combats distincts
        hability_modifier=0,          # bonus/malus d'HABILETÉ imposé par le texte pour tout le combat
        first_round_modifier=0,       # bonus/malus pour le premier assaut seulement
        psychic_immune=False,         # "insensible à la Discipline Kaï de la Puissance Psychique"
        psychic_attack=False,         # l'ennemi utilise sa Puissance Psychique (-2 HABILETÉ sans Bouclier psychique)
        psychic_attack_from_round=1,  # assaut à partir duquel l'attaque psychique compte
        flee_after=None,              # None: fuite interdite, 0: à tout moment, N: après N assauts
        max_rounds=None,              # "si après N assauts il est toujours vivant" -> "rounds_over"
        stop_when_wounded=False,      # "si vous perdez des points d'ENDURANCE au cours du combat" -> "wounded"
    )

    Ne compte JAMAIS toi-même dans hability_modifier : la Maîtrise des armes, la Puissance psychique, le malus
    de -4 sans arme, l'attaque psychique et les objets de combat (Essence d'Alether) sont gérés automatiquement.
    Un malus qui dépend d'un objet s'écrit avec has_item, ex: hability_modifier=0 if has_item("TORCHE") else -3.

    Exemple (KRAAN, HABILETÉ 16, ENDURANCE 24, "réduisez d'un point votre total d'HABILETÉ"):
        outcome = combat([("KRAAN", 16, 24)], hability_modifier=-1)
        if outcome == "win":
            st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au :"))
            st.page_link("tomes/tome1/page_XXX.py", label="XXX", icon="📄")

    Exemple (tuer en 4 assauts ou moins -> 94, sinon -> 203, fuite après 2 assauts -> 7):
        outcome = combat([("VOLEUR", 13, 20)], max_rounds=4, flee_after=2)
        if outcome == "win":
            st.page_link("tomes/tome1/page_94.py", label="94", icon="📄")
        elif outcome == "rounds_over":
            st.page_link("tomes/tome1/page_203.py", label="203", icon="📄")
        elif outcome == "fled":
            st.page_link("tomes/tome1/page_7.py", label="7", icon="📄")

    Exemple (deux Gloks à tour de rôle):
        outcome = combat([("Premier GLOK", 13, 10), ("Deuxième GLOK", 12, 10)])


10bis. Si le joueur doit consommer un repas, tu as juste à ajouter un appel à la fonction handle_repas() du fichier utils.py.
    Tout est déjà prévu et géré dans la méthode, donc ne fait rien d'autres que ca pour la gestion des repas.
    Exemple:
    "Vous vous sentez fatigué et affamé, et il vous faut faire une halte
    pour prendre un Repas"

    tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

    with tab1:
        st.write(fr_text)
        handle_repas()


11. Mort: Si la phrase 'Votre mission s'achève ici' apparaît, appeler ls_death() après l'affichage du message.

11bis. Illustrations: la dernière ligne du bloc 'with tab1:' est TOUJOURS show_illustrations() (importé de inventory),
    après les choix de destination. Elle affiche l'illustration du paragraphe s'il en a une, sinon ne fait rien.

12. Fin de Page: Le code doit OBLIGATOIREMENT se terminer par (hors de tout bloc, sans indentation) :
    end_page()

13. Tu ne retourneras que le contenu de la page, sans rien d'autres ni aucun commentaire de ta part. Ton retour sera copié collé directement dans une fichier python.

14. Table de Hasard: utiliser hazard_roll() (from utils import hazard_roll). Le bouton ne tire qu'une fois par visite
    et renvoie le chiffre du livre, de 0 à 9 (None tant que le joueur n'a pas tiré). Si la page a deux tirages
    distincts, leur donner des key différentes : hazard_roll(key="premier").
    Ex: "Utilisez la Table de Hasard. Si vous tirez entre 0 et 4, rendez-vous au 181. Entre 5 et 9, rendez-vous au 145."

    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("tomes/tome1/page_181.py", label="181", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome1/page_145.py", label="145", icon="📄")

"""
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
