import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    pickup_button,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=222, book=4)

fr_text = """
Dans l'intérieur douillet de la roulotte éclairée par des
chandelles, vous trouvez l'acteur réfugié sous une couverture.
Vous écartez la couverture et vous demandez à l'homme paralysé
par la peur de vous expliquer où il a trouvé cette arme. «Je... je
l'ai achetée à Eshnar, balbutie-t-il, le regard terrorisé. C'est le
tenancier de la taverne du Pic et de la Pioche qui me l'a vendue. »
Il saisit l'épée par la lame et vous la tend. « Si c'est votre épée que
j'ai achetée sans le savoir, j'en suis sincèrement désolé. Tenez,
prenez-la. » Vous empoignez le pommeau de cuivre et vous
examinez l'arme avec attention. Aucun doute: il s'agit bien d'une
épée de la cavalerie du Sommerlund. Elle porte même sur sa
lame une inscription qui vous fait sursauter : « Capitaine Rinir
Gayal, régiment de la Garde du Roi. » Si vous souhaitez
conserver cette Épée, inscrivez-la sur votre Feuille d'Aventure
dans la case Armes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("ÉPÉE DE GAYAL", key="epee_gayal", label="Prendre l'Épée du capitaine Gayal")

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_165.py", label="165", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
