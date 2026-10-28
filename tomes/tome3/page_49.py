import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    lose_backpack,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=49, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous escaladez la paroi rocheuse sur une distance de 5 mètres
environ et vous atteignez une corniche de glace mince. De là,
vous voyez clairement la fissure. Il vous semble avoir aperçu une
silhouette lorsque, soudain, la glace se dérobe sous vos pieds et
vous précipite tête la première dans un éboulement de granite et
de neige. Vous vous attendez à faire une chute de quelques
mètres, et vous vous préparez à vous recevoir le moins
brutalement possible, mais en fait vous tombez droit dans une
crevasse cachée sous une couche de neige poudreuse. Vous
atterrissez enfin quelque 30 mètres plus bas sur un énorme tas
de neige. Aveuglé, étourdi et suffoquant à moitié, vous vous
efforcez de vous dégager de cet amas et, lorsque vous y parvenez
enfin, le spectacle qui s'offre à vos yeux vous laisse bouche bée.
Un immense tunnel s'étend devant vous, aussi loin que votre
regard peut porter. De gigantesques stalactites de cristal pendent
du plafond de glace et la neige fondante qui tombe goutte à
goutte emplit la caverne d'une étrange musique. Vous appelez au
secours à grands cris jusqu'à ce que vous ayez la gorge sèche et
douloureuse ; vos guides, cependant, ne vous entendent pas.
Vous avez toujours votre arme (ou vos armes) avec vous, ainsi
que vos Pièces d'Or et vos Objets Spéciaux, mais vous n'avez plus
votre Sac à Dos qui est resté sous la tente. En levant les yeux,
vous vous apercevez que le trou dans lequel vous êtes tombé n'est
plus qu'un point minuscule sur la voûte du souterrain. La
lumière qui éclaire la caverne semble provenir de grandes coupes
de pierre suspendues au plafond. Ce sont des coupes de M'iare,
une source de lumière éternelle, découverte il y a des siècles par
les Anciens. Vous vous rendez bientôt compte que vos guides ne
découvriront probablement jamais l'endroit où vous avez atterri
et vous décidez donc d'avancer le long du vaste tunnel dans
l'espoir de trouver une sortie. Au bout de deux heures de marche,
vous arrivez à une bifurcation.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_backpack()
    st.caption("Votre Sac à Dos et tout son contenu sont restés sous la tente.")

    st.write_stream(stream_text('Si vous souhaitez emprunter le passage de gauche, rendez-vous au :'))
    st.page_link("tomes/tome3/page_284.py", label="284", icon="📄")

    st.write_stream(stream_text('Si vous préférez suivre celui de droite, rendez-vous au :'))
    st.page_link("tomes/tome3/page_199.py", label="199", icon="📄")

    st.write_stream(stream_text("Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome3/page_342.py", label="342", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_342.py", label="342", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
