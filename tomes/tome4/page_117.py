import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=117, book=4)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous arrivez bientôt à un endroit du tunnel où des travaux sont
en cours. Le sol s'est effondré et une passerelle de bois vermoulu
enjambe un trou béant.
Vous êtes fatigué et vous ne remarquez pas que votre Torche est
sur le point de s'éteindre. Vous vous trouvez au milieu de la
passerelle lorsque la flamme vacille puis meurt. Vous êtes alors
plongé dans les ténèbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous disposez d'une autre Torche, rendez-vous au :"))
    if has_item("TORCHE"):
        st.page_link("tomes/tome4/page_22.py", label="22", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_22.py", label="22", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous n'avez pas de Torche de secours, vous devrez avancer sur le pont dans une totale obscurité. Utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez les Disciplines Kaï du Sixième Sens ou de l'Orientation, ajoutez 3 au chiffre que vous aurez tiré."))
    if has_item("TORCHE"):
        st.info("*Vous possédez une Torche de secours : rendez-vous au 22.*")
    else:
        roll = hazard_roll()
        if roll is not None:
            bonus = 3 if has_kai("Le Sixième Sens") or has_kai("L'Orientation") else 0
            total = roll + bonus
            if bonus:
                st.write(f"*Sixième Sens ou Orientation : +3, soit un total de {total}.*")
            if total <= 6:
                st.write_stream(stream_text('Si votre total est de 0 à 6, rendez-vous au :'))
                st.page_link("tomes/tome4/page_99.py", label="99", icon="📄")
            else:
                st.write_stream(stream_text('De 7 à 12, rendez-vous au :'))
                st.page_link("tomes/tome4/page_256.py", label="256", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
