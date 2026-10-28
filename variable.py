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
        "description": "Une carte des Fins de Terre, rangée dans une poche intérieure de votre tunique.",
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
    "CLÉ D'OR": {"type": "special", "description": "Clé obtenue du Serpent de Pierre."},
    "PARCHEMIN": {"type": "special", "description": "Un rouleau de parchemin trouvé sur un Glok."},
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
    "COUVERTURE DE FOURRURE": {"type": "backpack", "description": "Une chaude couverture de fourrure."},
    "CORDE": {"type": "backpack", "description": "100 mètres de corde."},
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
    "ESSENCE D'ALETHER": {
        "type": "special",
        "combat_hability": 2,
        "description": "Augmente votre HABILETÉ de 2 points pendant toute la durée d'un affrontement. Une seule dose.",
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
}

# Équipement reçu au début du tome 2 (cf. « Équipement »), par les héros venus du tome 1 comme
# par les nouveaux. Les héros du tome 1 peuvent échanger une ou deux de leurs armes.
BOOK2_EQUIPMENT = {
    "gold_base": 10,  # Couronnes : 10 + Table de Hasard, ajoutées à celles déjà possédées
    "items_to_choose": 2,
    "items": [
        "ÉPÉE",
        "SABRE",
        "REPAS",  # deux Repas
        "COTTE DE MAILLES",
        "MASSE D'ARMES",
        "POTION DE GUÉRISON",
        "BÂTON",
        "LANCE",
        "GLAIVE",
        "BOUCLIER",
    ],
    # « Au départ de votre quête, vous êtes en possession du Sceau d'Hammardal » et d'une carte
    "special": ["SCEAU D'HAMMARDAL", "CARTE GÉOGRAPHIQUE"],
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
