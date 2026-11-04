import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=253, book=5)

fr_text = """
Tout à coup, la douleur disparaît mais un nouveau spectacle
effrayant s'offre à vos yeux : semblant surgir des ténèbres, un
tourbillon de vapeurs vertes se forme lentement et, petit à petit,
prend la forme d'un monstre scintillant ressemblant
étrangement à un serpent. Un brouillard gris sort tout droit de la
bouche du Seigneur des Ténèbres et entoure le cœur de l'horrible
créature, lui insufflant son pouvoir mortel. Le serpent se tord de
douleur et est secoué de convulsions au fur et à mesure que le
nuage gris emplit son corps. Ce qui n'était qu'illusion il y a
quelques secondes, devient à présent cauchemar vivant ! Deux
petits points cramoisis brillent dans les yeux du monstre tandis
qu'il ondule vers vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez une Masse d'Armes incrustée de pierreries, vous pouvez ajouter 5 points à votre total d'HABILETÉ pour toute la durée du combat, car c'est une arme magique, particulièrement efficace contre ce genre de créatures."))
    outcome = combat(
        [("DHORGAAN", 20, 40)],
        hability_modifier=5 if has_item("MASSE D'ARMES INCRUSTÉE") else 0,
    )
    if outcome == "win":
        st.write_stream(stream_text("Si vous remportez ce combat, rendez-vous au :"))
        st.page_link("tomes/tome5/page_335.py", label="335", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
