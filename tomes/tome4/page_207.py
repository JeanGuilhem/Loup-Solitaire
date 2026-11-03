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

check_inventory(current_page_number=207, book=4)

fr_text = """
Vous saisissez une flèche dans un carquois accroché au mur et
vous tendez votre arc de toutes vos forces. Un des brigands à
cheval galope dans la plaine en brandissant un javelot. Il vise un
soldat blessé du Sommerlund qui est tombé de la barricade et
reste étendu là, incapable de se défendre. Le brigand s'apprête à
lancer son javelot lorsque vous tirez votre flèche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si vous possédez la Discipline Kaï de la Maîtrise des Armes (quelle que soit l'arme dont il s'agit), vous ajouterez 2 au chiffre que vous aurez tiré."))
    roll = hazard_roll()
    if roll is not None:
        total = roll + (2 if has_kai("La Maîtrise des armes") else 0)
        if has_kai("La Maîtrise des armes"):
            st.write(f"*Maîtrise des Armes : +2, soit un total de {total}.*")
        if total <= 4:
            st.write_stream(stream_text('Si vous obtenez un total de 0 à 4, rendez-vous au :'))
            st.page_link("tomes/tome4/page_336.py", label="336", icon="📄")
        else:
            st.write_stream(stream_text('De 5 à 11, rendez-vous au :'))
            st.page_link("tomes/tome4/page_218.py", label="218", icon="📄")


    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
