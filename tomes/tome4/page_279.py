import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=279, book=4)

fr_text = """
Tandis que vous déroulez le parchemin dont vous commencez à
lire la sinistre prophétie, le baron se lève avec difficulté et répète
mot pour mot chaque vers de la terrible strophe, sa voix s'élevant
comme un écho de la vôtre :
Au soir de pleine lune, en un temple profond
Sacrifice viendra à jamais réveiller
Les légions d'un seigneur trop longtemps oublié.
Quand mourra sur l'autel la vierge aux cheveux blonds,
Des gorges de Maaken les morts se lèveront
Pour exiger enfin la rançon des guerriers.
« Il faut que vous la sauviez, Loup Solitaire, dit le baron d'une
voix tremblante d'émotion ; il faut que vous empêchiez le
sacrifice ».
« Sauver qui ? Qui doit-il sauver ? » interroge le capitaine Gayal
tout en essayant de calmer le baron en émoi.
« Ma fille Madelon, répond ce dernier. Barraka a découvert le
Poignard de Vashna et il projette de sacrifier ma fille sur l'autel
du temple pour libérer les morts des gorges de Maaken. »
Le baron explique alors qu'au temps de la Lune Noire le roi
Ulnar du Sommerlund tua Vashna, le plus puissant des Maîtres
des Ténèbres à l'aide du Glaive de Sommer, l'Épée du Soleil. Le
corps du chef ennemi ainsi que les cadavres de tous ses soldats
furent précipités dans les abîmes sans fond des gorges de
Maaken. « Barraka veut réveiller ces légions, poursuit le baron, et les
amener à la victoire en conquérant tout d'abord le Sommerlund,
puis l'ensemble des Fins de Terre. » Vous observez le baron dans
un silence impressionnant. Si Barraka parvient à accomplir le
sacrifice, tout sera perdu. Quelle armée de mortels pourrait en
effet résister aux légions des morts ? Le capitaine Gayal vous
entraîne ensuite hors de la pièce, dont il referme la porte derrière
lui. « Je craignais qu'il ne soit fou, dit-il, mais votre parchemin vient
hélas ! confirmer mon pire cauchemar ; il dit bien la vérité. »
Tandis que vous repensez à l'effroyable signification de ces
quelques vers, votre sombre méditation est soudain interrompue
par le son aigu d'une corne de guerre. Le capitaine Gayal
s'approche d'une meurtrière et scrute la plaine. Lorsqu'il se
tourne à nouveau vers vous, il a le teint gris comme la cendre. «
Les brigands, murmure-t-il, ils lancent une attaque. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez l'Épée du capitaine Gayal, rendez-vous au :"))
    if has_item("ÉPÉE DE GAYAL"):
        st.page_link("tomes/tome4/page_327.py", label="327", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_327.py", label="327", icon="📄", disabled=True)
    st.write_stream(stream_text('Sinon, rendez-vous au :'))
    st.page_link("tomes/tome4/page_289.py", label="289", icon="📄", disabled=has_item("ÉPÉE DE GAYAL"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
