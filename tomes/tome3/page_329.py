import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=329, book=3)

fr_no_oil = "Vous ne vous êtes pas enduit d'huile de Bakanal."
fr_oil = "Vous êtes enduit d'huile de Bakanal : les Languabarbs vous ont déjà flairé."

fr_text = """
Ce sont des Languabarbs que vous entendez et ils sont trois en
tout. Il s'agit là de créatures malfaisantes qui habitent les
montagnes de Kalte. Prédateurs redoutables, leur gibier préféré
est le Bakanal.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous vous êtes enduit le corps d'huile de Bakanal, rendez-vous au :"))
    if has_flag("huile de Bakanal"):
        st.page_link("tomes/tome3/page_202.py", label="202", icon="📄")
    else:
        st.write_stream(stream_text(fr_no_oil))
        st.page_link("tomes/tome3/page_202.py", label="202", icon="📄", disabled=True)
    st.write_stream(stream_text("Sinon, vous pouvez éviter les Languabarbs en revenant sur vos pas, vers l'entrée de l'autre tunnel. Rendez-vous pour cela au :"))
    if not has_flag("huile de Bakanal"):
        st.page_link("tomes/tome3/page_284.py", label="284", icon="📄")
    else:
        st.write_stream(stream_text(fr_oil))
        st.page_link("tomes/tome3/page_284.py", label="284", icon="📄", disabled=True)
    st.write_stream(stream_text("Enfin, si vous souhaitez attaquer ces créatures, rendez-vous au :"))
    if not has_flag("huile de Bakanal"):
        st.page_link("tomes/tome3/page_138.py", label="138", icon="📄")
    else:
        st.write_stream(stream_text(fr_oil))
        st.page_link("tomes/tome3/page_138.py", label="138", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
