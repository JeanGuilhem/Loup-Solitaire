import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=196, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Le roi Alin IV est assis, seul, dans sa tour surmontée d'un dôme et
contemple les montagnes à travers une haute fenêtre aux vitres de
couleur. Un huissier vous annonce, Lord Axim et vous-même, puis
vous pénétrez dans la Chambre Royale en vous inclinant
respectueusement devant Sa Majesté. Lord Axim retire alors le Sceau
d'Hammardal de votre doigt et s'approche du roi. Tous deux
s'entretiennent pendant presque une heure, leur visage soucieux
exprimant toute la gravité de la situation. Enfin, après un bref silence,
le roi Alin se lève soudain de son trône et, pour la première fois, vous
adresse la parole. « Hélas, dit-il, les Maîtres des Ténèbres se sont levés
à nouveau et, à nouveau, le Royaume du Sommerlund vient demander
notre aide. J'ai longtemps prié le ciel que mon règne soit placé sous le
signe de la paix et de l'harmonie, mais au fond de mon cœur, j'avais
malheureusement la certitude qu'il en serait autrement. » Le roi tire
alors d'une poche de sa pelisse blanche une clé d'or qu'il introduit dans
la serrure d'un coffre de marbre posé sur une estrade au centre de la
pièce. Un faible bourdonnement s'élève aussitôt, tandis que le
couvercle du coffre glisse latéralement, laissant apparaître le pommeau
d'une épée en or massif.
« Prend ce glaive, Loup Solitaire, commande le roi, car il est dit que
seul un vrai fils du Sommerlund saura révéler la puissance qui se cache
dans sa lame. » Lorsque vous empoignez le pommeau étincelant, un
frémissement vous parcourt le bras puis se répand dans tout votre
corps.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        if not has_item("GLAIVE DE SOMMER"):
            add_to_inventory("GLAIVE DE SOMMER")
    st.success("Le Glaive de Sommer est rangé dans vos Objets Spéciaux.")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome2/page_79.py", label="79", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_79.py", label="79", icon="📄", disabled=True)

    st.write_stream(stream_text("Dans le cas contraire, rendez-vous au :"))
    st.page_link("tomes/tome2/page_123.py", label="123", icon="📄", disabled=has_kai("Le Sixième Sens"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
