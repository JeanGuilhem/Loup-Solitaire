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

check_inventory(current_page_number=305, book=4)

fr_text = """
Un plan audacieux vous vient à l'esprit. Vous prenez dans votre
poche le Médaillon d'Onyx et vous avancez d'un pas résolu vers
les brigands. Ils sont si occupés à bavarder qu'ils ne vous
remarquent même pas. Lorsque soudain vous apparaissez devant
eux, ils sursautent. Jouant alors votre rôle à la perfection, vous
les rappelez sèchement à l'ordre, vous déclarant scandalisé par la
désinvolture de leur tenue et de leur démarche. Vous les menacez
de faire un rapport à Barraka lui-même pour lui signaler leur
comportement. Dès qu'ils aperçoivent le Médaillon d'Onyx, ils se
redressent comme un seul homme et s'alignent au garde-à-vous,
prêts à obéir à vos ordres. D'un ton de commandement sans
réplique, vous les envoyez alors en direction de la forêt en leur
ordonnant de marcher au pas cadencé. Tandis qu'ils s'éloignent,
vous courez dans l'autre direction pour mettre le plus de distance
possible entre eux et vous, avant qu'ils ne s'aperçoivent de la
supercherie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome4/page_204.py", label="204", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
