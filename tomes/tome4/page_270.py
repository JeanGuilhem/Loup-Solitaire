import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

fr_unknown_item = "Vous ne possédez pas cet objet."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=270, book=4)

fr_text = """
La pluie et l'obscurité dissimulent votre approche, vous
permettant d'atteindre les marches de marbre sans être vu.
L'escalier est envahi de mauvaises herbes et de moisissures, mais
un chemin y a été tracé qui permet de descendre dans les
ténèbres d'une vaste cave voûtée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous possédez une Torche dans votre Sac à Dos, rendez-vous au :'))
    if has_item("TORCHE"):
        st.page_link("tomes/tome4/page_29.py", label="29", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_29.py", label="29", icon="📄", disabled=True)
    st.write_stream(stream_text('Si vous possédez une Sphère de Feu, rendez-vous au :'))
    if has_item("SPHÈRE DE FEU"):
        st.page_link("tomes/tome4/page_168.py", label="168", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_168.py", label="168", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous n'avez ni l'une ni l'autre, vous pouvez poursuivre votre chemin dans l'obscurité en vous rendant au :"))
    st.page_link("tomes/tome4/page_246.py", label="246", icon="📄", disabled=has_item("TORCHE") or has_item("SPHÈRE DE FEU"))
    st.write_stream(stream_text("Il vous est également possible de quitter la cave pour essayer d'entrer dans le temple par la porte de la crypte ; rendez-vous pour cela au :"))
    st.page_link("tomes/tome4/page_183.py", label="183", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
