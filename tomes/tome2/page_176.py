import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=176, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous avez chevauché pendant trois jours et trois nuits le long du grand
chemin qui remonte la vallée du Durenon. Au loin, vous apercevez le
sommet des monts d'Hammardal, l'une des plus hautes chaînes de
montagnes de Magnamund. La capitale du royaume de Durenor est
nichée au creux de ces montagnes. L'aube vient de se lever sur le
quatorzième jour de votre quête. Vous avez établi votre camp près
d'une chute d'eau ; à cet endroit, les flots du fleuve Durenon plongent
au bas d'un à-pic de 40 mètres de hauteur. Vous vous apprêtez à vous
remettre en route lorsque six cavaliers au visage encapuchonné
apparaissent sur la route forestière et vous bloquent le passage. Le
Lieutenant Général Rhygar leur intime l'ordre de vous laisser passer en
leur précisant que vous êtes porteur d'une dépêche royale. Au royaume
de Durenor, faire obstacle au passage d'un messager du roi est
considéré comme un acte de trahison ; malheureusement,
l'avertissement du Lieutenant Général laisse indifférents les six
cavaliers qui refusent de bouger d'un pouce. « Si vous ne voulez pas
entendre raison, nos épées vous convaincront peut-être», dit alors
Rhygar. Il dégaine aussitôt son arme et ordonne à ses hommes de
passer à l'attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez prêter main forte à Rhygar, rendez-vous au :"))
    st.page_link("tomes/tome2/page_45.py", label="45", icon="📄")

    st.write_stream(stream_text("Si vous préférez ne pas attaquer les cavaliers, rendez-vous au :"))
    st.page_link("tomes/tome2/page_277.py", label="277", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :"))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome2/page_322.py", label="322", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_322.py", label="322", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
