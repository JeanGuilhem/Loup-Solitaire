import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    lose_all_weapons,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=124, book=5)

fr_text = """
Vous sautez du rebord de la fenêtre et vous tombez violemment,
les pieds en avant, sur les Gardes qui vont rouler au sol sans
comprendre ce qui leur arrive. Avant qu'ils se relèvent, vous
passez rapidement à l'attaque et vous en tuez trois. Mais les
bruits de la bataille parviennent jusqu'à la cantine : une douzaine
de soldats du Zakhan accourent à la rescousse et vous succombez
rapidement sous le nombre. C'est uniquement par respect pour
votre courage que vos adversaires vous laissent la vie sauve. Ils
vous désarment, puis vous conduisent de force dans un cachot où
l'on vous laisse jusqu'à ce que le Zakhan veuille bien vous
recevoir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        lose_all_weapons()
    st.write("*Vous avez perdu vos armes.*")

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome5/page_18.py", label="18", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
