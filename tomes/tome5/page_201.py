import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=201, book=5)

fr_text = """
Tout à coup, vous apercevez deux guerriers qui s'avancent
lentement vers vous le long d'un passage à votre droite. Ils
portent des armures noires, des habits écarlates et vous
reconnaissez leur hideux masque à tête de mort: ce sont des
guerriers Drakkars. Les Drakkars sont des hommes, certes, mais
des hommes extrêmement cruels, aussi méchants et féroces que
les Seigneurs des Ténèbres qu'ils servent. L'un d'eux tient en
laisse un Akataz aux crocs acérés. Le Drakkar siffle, et aussitôt, le
redoutable chien de guerre vous saute à la gorge.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous désirez vous battre avec cette créature, rendez-vous au :"))
    st.page_link("tomes/tome5/page_273.py", label="273", icon="📄")

    st.write_stream(stream_text("Si vous préférez tenter d'échapper à cette attaque et vous enfuir, rendez-vous au :"))
    st.page_link("tomes/tome5/page_285.py", label="285", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
