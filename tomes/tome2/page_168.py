import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    spend_gold,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=168, book=2)

fr_text = """
Un par un, les autres voyageurs s'approchent et contemplent avec
horreur le corps du cocher de la diligence. « Il faut l'enterrer », dit le
moine. Vous hochez la tête en signe d'approbation et vous creusez une
tombe pour y déposer le corps. Lorsque le malheureux est enterré, tous
les voyageurs et vous-même revenez près de la diligence pour décider
de ce qu'il convient de faire. «Je connais la route de Port Bax, je peux
remplacer le cocher», propose Halvorc. «J'espère qu'on ne nous
accusera pas de l'avoir tué», dit le moine avec inquiétude. « Ce sont les
dieux qui ont décidé de sa mort», assure Dorier. «J'en porterai
témoignage», déclare Ganon, les Chevaliers de la Montagne Blanche ne
mentent jamais. Il est vrai qu'au royaume de Durenor un authentique
chevalier dit toujours la vérité, qu'elle lui soit ou non favorable. Ses
paroles semblent avoir rassuré le moine et bientôt la diligence fait route
à nouveau en direction de l'est. L'après-midi touche à sa fin lorsque
vous arrivez au relais d'un petit village côtier connu sous le nom de
Crique en Gorn et dont la population se compose essentiellement de
repris de justice, de voleurs et de Squalls. Les villageois se montrent
soupçonneux lorsqu'on leur annonce la mort du cocher, mais Dorier
parvient à les convaincre qu'il s'agit bel et bien d'un accident. Il n'y a
qu'une seule auberge dans tout le village; c'est une taverne qui porte un
nom peu engageant : L'Espoir Déçu. Son état de délabrement est
typique de la pauvreté qui règne dans ce village du bord de mer où
abondent les masures en ruines. Une chambre pour la nuit coûte 1 Pièce
d'Or.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous avez les moyens de vous offrir une chambre, rendez-vous au :"))
    if st.button("Payer 1 Couronne (314)", disabled=st.session_state.purse < 1):
        if spend_gold(1):
            st.switch_page("tomes/tome2/page_314.py")

    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    st.page_link("tomes/tome2/page_25.py", label="25", icon="📄", disabled=st.session_state.purse >= 1)
    if st.session_state.purse >= 1:
        st.caption("Vous avez les moyens de vous offrir une chambre.")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
