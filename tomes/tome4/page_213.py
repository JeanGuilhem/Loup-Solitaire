import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=213, book=4)

fr_text = """
Une fouille systématique vous permet de trouver les objets
suivants :
- 1 Pioche,
- 1 Pelle,
- 1 Hache,
- 1 Torche,
- 1 Briquet à Amadou,
- 1 Sablier,

Si vous souhaitez conserver un ou plusieurs de ces objets, notez-les
sur votre Feuille d'Aventure (la Pioche et la Pelle comptent
chacune pour deux objets). Tous ces objets, si vous les prenez,
doivent être inscrits dans la case Sac à Dos. Après avoir vérifié
qu'il n'y a rien d'autre à découvrir dans le hangar, vous ordonnez
à vos hommes de mettre à l'eau le bateau à rames.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("PIOCHE", key="pioche", label="Prendre la Pioche")
    pickup_button("PELLE", key="pelle", label="Prendre la Pelle")
    pickup_button("HACHE", key="hache", label="Prendre la Hache")
    pickup_button("TORCHE", key="torche", label="Prendre la Torche")
    pickup_button("BRIQUET À AMADOU", key="briquet", label="Prendre le Briquet à Amadou")
    pickup_button("SABLIER", key="sablier", label="Prendre le Sablier")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_180.py", label="180", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
