import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    set_flag,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=91, book=3)

fr_text = """
Vous retenez votre respiration tandis que vous vous enduisez le
torse de cette graisse gluante. A mesure que l'huile imprègne
votre peau, cependant, vous sentez une bienfaisante chaleur
rayonner dans tout votre corps, comme si vous vous trouviez
près d'un feu. Et plus vous appliquez de graisse, plus vous avez
chaud. Vous remarquez également que l'épouvantable odeur s'est
dissipée. « Lorsque l'huile pénètre dans la peau, on perd
l'odorat », dit Irian. Il recommande aux autres de se frictionner à
leur tour avec l'huile de Bakanal ; cette substance apporte une
protection particulièrement efficace contre les températures
glaciales de Kalte, et elle pourrait bien se révéler
particulièrement utile dans un proche avenir. Lorsque vous
revenez sous votre tente, les chiens Kanu ne semblent pas
apprécier l'odeur que vous dégagez : quand vous passez près
d'eux, ils se mettent à gémir et enfouissent leur museau dans la
neige.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        set_flag("huile de Bakanal")
    st.success("*Vous vous êtes enduit le torse d'huile de Bakanal.*")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_134.py", label="134", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
