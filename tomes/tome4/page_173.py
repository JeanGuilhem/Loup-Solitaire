import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=173, book=4)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Le pilier de bois est épais et solide. Pour l'abattre, il faudra le
frapper avec force.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez le Glaive de Sommer, rendez-vous au :'))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome4/page_275.py", label="275", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_275.py", label="275", icon="📄", disabled=True)

        st.write_stream(stream_text("Sinon, utilisez la Table de Hasard pour obtenir un chiffre. Si vous disposez d'une Pioche ou d'une Pelle, vous ajouterez 2 au chiffre que vous aurez tiré."))
        roll = hazard_roll()
        if roll is not None:
            tool = has_item("PIOCHE") or has_item("PELLE")
            total = roll + (2 if tool else 0)
            if tool:
                st.write(f"*Pioche ou Pelle : +2, soit un total de {total}.*")
            if total <= 6:
                st.write_stream(stream_text('Si vous obtenez un total de 0 à 6, rendez-vous au :'))
                st.page_link("tomes/tome4/page_143.py", label="143", icon="📄")
            else:
                st.write_stream(stream_text('De 7 à 11, rendez-vous au :'))
                st.page_link("tomes/tome4/page_179.py", label="179", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
