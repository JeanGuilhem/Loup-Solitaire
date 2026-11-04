import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=127, book=5)

fr_text = """
Vous retournez sur vos pas jusqu'au croisement afin d'avoir
suffisamment d'élan. Si vous heurtez la porte au bon endroit et à
une vitesse suffisante, vous parviendrez peut-être à faire sauter le
verrou.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour savoir si l'opération réussit ou non. Ajoutez 10 au chiffre que vous avez obtenu."))
    roll = hazard_roll()
    if roll is not None:
        total = roll + 10
        st.write(f"*Total : {total} (votre HABILETÉ : {st.session_state.hability}).*")
        if total <= st.session_state.hability:
            st.write_stream(stream_text("Votre total est égal ou inférieur à vos points d'HABILETÉ : le mur se fendille et la serrure cède. Rendez-vous au :"))
            st.page_link("tomes/tome5/page_159.py", label="159", icon="📄")
        else:
            # blessure à l'épaule, une seule fois par visite
            if not st.session_state.get("visibility_t5_127_epaule"):
                st.session_state["visibility_t5_127_epaule"] = True
                change_endurance(-1)
            st.write_stream(stream_text("Votre total est supérieur à votre total d'HABILETÉ : la serrure ne cède pas et vous subissez à l'épaule une blessure qui vous coûte 1 point d'ENDURANCE."))
            st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)
            st.write_stream(stream_text("Vous devez alors prendre l'autre passage conduisant à l'escalier et vous rendre au :"))
            st.page_link("tomes/tome5/page_93.py", label="93", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
