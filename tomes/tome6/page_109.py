import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=109, book=6)

fr_text = """
Quelques hommes se mettent à rire et à vous dévisager comme si
vous étiez fou. Cependant, l'un d'entre eux vous fait un signe
et vous remet un long cylindre en cuir. « Voici un plan de
Tekaro, murmure-t-il en grimaçant de douleur. Je... je ne sais
pas comment on peut pénétrer dans la ville... mais si toutefois
vous y arrivez, cette carte pourra vous être utile. » Après
avoir remercié le blessé, vous sortez de la tente. A moins que
vous ne possédiez déjà un plan de Tekaro, conservez l'étui de
cuir que l'homme vient de vous donner et inscrivez-le dans la
case Sac à Dos de votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_item("PLAN DE TEKARO"):
        st.caption("Vous possédez déjà un plan de Tekaro.")
    else:
        pickup_button("PLAN DE TEKARO", key="plan", label="Conserver l'étui de cuir (Plan de Tekaro)")

    st.write_stream(stream_text("Rendez-vous ensuite au :"))
    st.page_link("tomes/tome6/page_70.py", label="70", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
