import streamlit as st
from inventory import (
    can_shoot,
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

check_inventory(current_page_number=13, book=6)

fr_text = """
Vous vous frayez un chemin à travers le sous-bois, sans faire le
moindre bruit et avec toute l'habileté dont sait faire preuve un
Maître Kaï tel que vous. Vous arrivez bientôt à la lisière d'une
clairière rocailleuse. Là, une dizaine d'hommes se tiennent en
cercle autour d'un autel en pierre. Leur chef, un homme grand et
mince, portant un masque vert hideux sur le visage, promène une
longue baguette en or au-dessus de la tête d'une créature
batracienne, écartelée sur l'autel. Des étincelles aveuglantes
jaillissent du corps du monstrueux animal et, au fur et à mesure
que les incantations de la sinistre assemblée augmentent
d'intensité, le corps de la bête s'élève graduellement, planant à
quelques dizaines de centimètres au-dessus de l'autel. Mais
soudain, le chef pousse un cri de colère et il se tourne dans
votre direction: il vient de détecter votre présence ! Ses yeux
lancent des éclairs et vous pouvez sentir la fureur qui l'anime.
Tout à coup, l'homme pointe sa baguette en or vers vous et une
décharge d'énergie fend l'air en grésillant.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez un arc et si vous voulez vous en servir, rendez-vous au :"))
    st.page_link("tomes/tome6/page_56.py", label="56", icon="📄", disabled=not can_shoot())

    st.write_stream(stream_text("Si vous ne possédez pas d'arc, vous pouvez prendre la fuite. Rendez-vous dans ce cas au :"))
    st.page_link("tomes/tome6/page_182.py", label="182", icon="📄", disabled=can_shoot())

    st.write_stream(stream_text("Si vous préférez dégainer votre arme et vous préparer au combat, rendez-vous au :"))
    st.page_link("tomes/tome6/page_295.py", label="295", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
