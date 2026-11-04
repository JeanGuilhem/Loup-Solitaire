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

check_inventory(current_page_number=315, book=5)

fr_text = """
Alors que vous tirez le Glaive de Sommer de son fourreau, un
reflet d'or aveuglant court le long de sa lame. Le Vordak hurle
d'effroi, ses doigts osseux maculés de sang s'agrippant à une
lourde masse d'armes en métal noir qui pend à sa ceinture. Le
Vordak lève son arme pour parer votre coup, mais l'épée du soleil
fend le fer de votre adversaire en lançant une gerbe d'étincelles
bleues. Vous frappez à nouveau en décrivant un grand cercle et la
lame d'or transperce le corps monstrueux du Vordak, le coupant
en deux de la tête à la taille. Une épouvantable odeur aigre vous
prend à la gorge tandis qu'un flot de liquide verdâtre s'écoule à
travers les vêtements rouges de la créature. Le Vordak vacille et
se recroqueville sous vos yeux puis le cadavre en dissolution
tombe en vrille vers le lac Inrahim en produisant un sifflement
aigu. Après avoir rengainé votre arme, vous saisissez les rênes et
vous vous efforcez de maîtriser les tressaillements de votre
monture blessée. Bien que vous vous soyez débarrassé du
Vordak, la victoire n'en est pas assurée pour autant, car l'Itikar
perd toujours son sang en abondance et il risque à tout moment
de sombrer dans l'inconscience et de vous laisser tomber comme
une pierre. Soudain, vous apercevez quelque chose dans le
lointain... Et cette vision vous redonne envie de croire aux
miracles !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome5/page_221.py", label="221", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
