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

check_inventory(current_page_number=305, book=3)

fr_text = """
L'énorme bête roule à bas du traîneau et s'immobilise dans la
neige. Fenor a réussi à allumer une torche et l'agite devant les
deux autres Bakanals qui s'enfuient terrifiés. Vous saluez par des
cris de joie la défaite des créatures et vous vous tournez vers vos
courageux guides pour les féliciter. Vous êtes alors stupéfait de
voir qu'ils ont commencé à dépecer le cadavre du Bakanal que
vous avez tué. Avec dégoût, vous voyez Dyce ouvrir le ventre de la
bête sur toute sa longueur avec son couteau de chasse. Il écarte
ensuite la peau et plonge les mains dans la graisse de l'animal.
L'odeur qui se dégage de cette graisse est infecte, à tel point que
les chiens Kanu eux-mêmes s'enfouissent le museau dans la
neige pour essayer de ne pas la sentir. Lorsque enfin les deux
guides commencent à s'enduire le visage et le corps de cette
substance répugnante, vous avez du mal à en croire vos yeux.
« C'est de l'huile de Bakanal, lance Fenor d'un ton réjoui, c'est ce
qu'il y a de mieux pour se protéger contre le froid et l'humidité. »
Il plonge à nouveau la main dans le cadavre de la bête et vous
tend une poignée de cette gelée putride.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez suivre son exemple et vous enduire à votre tour de cette graisse pestilentielle, rendez-vous au :"))
    st.page_link("tomes/tome3/page_8.py", label="8", icon="📄")
    st.write_stream(stream_text("Si en revanche la perspective de sentir aussi bon qu'une bassine de roquefort rance ne vous séduit guère, rendez-vous au :"))
    st.page_link("tomes/tome3/page_281.py", label="281", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
