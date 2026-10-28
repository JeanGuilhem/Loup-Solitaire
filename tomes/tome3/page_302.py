import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=302, book=3)

fr_text = """
Vous descendez une hauteur de 60 mètres avant d'atteindre le
fond de la crevasse. Il y règne une totale obscurité, à l'exception
d'une petite lueur que l'on peut apercevoir au loin. Vous vous
dirigez vers cette lueur, mais vous n'avancez que lentement et
péniblement. De gros fragments de roc et de glace sont répandus
çà et là sur le sol et, dans l'obscurité, vous vous y cognez sans
cesse, en tombant quelquefois.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï du Sixième Sens, vous pouvez ajouter 2 au chiffre que vous aurez tiré."))
    roll = hazard_roll()
    if roll is not None:
        total = roll + (2 if has_kai("Le Sixième Sens") else 0)
        if has_kai("Le Sixième Sens"):
            st.write(f"*Sixième Sens : +2, soit un total de {total}.*")
        if total <= 1:
            st.write_stream(stream_text("Si le total obtenu est de 0 ou 1, rendez-vous au :"))
            st.page_link("tomes/tome3/page_37.py", label="37", icon="📄")
        elif total <= 7:
            st.write_stream(stream_text("De 2 à 7, rendez-vous au :"))
            st.page_link("tomes/tome3/page_193.py", label="193", icon="📄")
        else:
            st.write_stream(stream_text("De 8 à 11, rendez-vous au :"))
            st.page_link("tomes/tome3/page_243.py", label="243", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
