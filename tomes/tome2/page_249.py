import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=249, book=2)

fr_text = """
Au cours de l'après-midi, vous bavardez avec vos compagnons de
voyage tandis que la diligence file bon train. Au bout de quelques
heures, vous avez appris beaucoup de choses à leur sujet. Les deux
hommes assis face à vous sont frères. Ils se nomment Ganon et Dorier
et ce sont des Chevaliers de l'Ordre de la Montagne Blanche, des
guerriers du Royaume de Durenor, qui ont fait serment de protéger leur
patrie contre les brigands du Pays Sauvage. Ils possèdent un château et
des terres près de Port Bax. A côté d'eux est assis un certain Halvorc,
marchand de son état. Il a le nez enflé et le visage couvert de bleus. Ce
sont les gardes de Lachelan, le Suzerain de Ragadorn, qui l'ont mis
dans cet état. A la suite d'un léger malentendu avec les autorités de la
ville à propos de taxes portuaires, toute sa marchandise et la plus
grande partie de son or lui ont été confisqués. Près de la portière
opposée est assis un moine du nom de Parsion, un compatriote du
Sommerlund qui a traversé le Pays Sauvage en diligence pour se rendre
à Port Bax. La jeune femme assise à côté de vous a pour nom Viveka.
C'est une aventurière mercenaire qui gagne son or les armes à la main
en vendant ses services au plus offrant. Elle retourne à Port Bax avec
en poche le prix de ses derniers exploits, accomplis victorieusement
dans la ville de Ragadorn. Quant à vous, vous n'avez nullement
l'intention de révéler votre véritable identité et vous vous êtes fait
passer pour un simple paysan. Les passagers de la diligence semblent
tout ignorer de la guerre qui ravage le Royaume du Sommerlund.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome2/page_39.py", label="39", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
