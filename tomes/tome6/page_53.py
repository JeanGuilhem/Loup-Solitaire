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

check_inventory(current_page_number=53, book=6)

fr_text = """
L'homme écoute votre question en vous dévisageant attentivement,
comme pour essayer de deviner vos intentions. « Mais qu'est-ce
qu'un guerrier tel que vous peut bien aller chercher dans la rue
des Sages ? » vous demande-t-il pensivement, tout en tripotant
sa longue barbe grise de ses doigts fins et soignés. Vous êtes
en train de réfléchir à un prétexte quelconque, qui ne dévoilera
rien de la véritable nature de votre quête, lorsque, soudain,
votre interlocuteur semble se troubler. « Désolé, je ne puis
vous aider », répond-il d'une voix sèche en s'éloignant du bar.
Puis il disparaît en un clin d'œil, fendant la foule des
mercenaires enivrés. Vous restez, quant à vous, quelque peu
abasourdi par cette imprévisible réaction... Qu'avez-vous donc
dit qui ait pu provoquer ce brusque départ ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("A moins que vous ne l'ayez déjà fait, vous pouvez maintenant vous approcher de la table où est assis le négociant, rendez-vous au :"))
    st.page_link("tomes/tome6/page_240.py", label="240", icon="📄")

    st.write_stream(stream_text("Si vous préférez en revanche aller trouver le tavernier, rendez-vous au :"))
    st.page_link("tomes/tome6/page_312.py", label="312", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
