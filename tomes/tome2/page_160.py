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

check_inventory(current_page_number=160, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
« Pardonnez-moi, my lord, je ne voulais pas vous faire peur. »
L'homme semble inquiet et la main ouverte qu'il tend vers vous ne
cesse de trembler. Sans vous départir de votre prudence, vous acceptez
son geste amical et quelques instants plus tard vous vous asseyez avec
lui à l'une des tables de l'auberge dans laquelle vous êtes entré par une
porte latérale. L'endroit est désert, à l'exception d'un couple de souris
qui rongent un gros morceau de fromage.
« Le capitaine Kelman m'a chargé de vous amener à bord du Sceptre
Vert mais je dois tout d'abord m'assurer que vous êtes bien le Seigneur
Kaï qu'on appelle le Loup Solitaire, dit l'homme ; pouvez-vous donner
la preuve de votre identité ? » Le meilleur moyen de prouver que vous
êtes bien le Loup Solitaire consiste à faire la démonstration que vous
maîtrisez l'une des Disciplines Kaï.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous avez le choix entre les Disciplines suivantes :"))

    st.write_stream(stream_text("Guérison : rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome2/page_16.py", label="16", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_16.py", label="16", icon="📄", disabled=True)

    st.write_stream(stream_text("Puissance Psychique : rendez-vous au :"))
    if has_kai("Puissance psychique"):
        st.page_link("tomes/tome2/page_133.py", label="133", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_133.py", label="133", icon="📄", disabled=True)

    st.write_stream(stream_text("Maîtrise des Armes : rendez-vous au :"))
    if has_kai("La Maîtrise des armes"):
        st.page_link("tomes/tome2/page_255.py", label="255", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_255.py", label="255", icon="📄", disabled=True)

    st.write_stream(stream_text("Communication Animale : rendez-vous au :"))
    if has_kai("Communication Animale"):
        st.page_link("tomes/tome2/page_203.py", label="203", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_203.py", label="203", icon="📄", disabled=True)

    st.write_stream(stream_text("Maîtrise Psychique de la Matière : rendez-vous au :"))
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome2/page_48.py", label="48", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome2/page_48.py", label="48", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            "Si vous ne maîtrisez aucune des Disciplines de cette liste, ou si vous ne souhaitez pas "
            "faire de démonstration, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome2/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
