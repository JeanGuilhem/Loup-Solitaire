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

check_inventory(current_page_number=374, book=5)

fr_text = """
Tandis que vous tombez, les images de la Nef du ciel, des Kraans
et de l'horizon défilent sous vos yeux en un mélange de formes et
de couleurs, comme si vous regardiez à travers un kaléidoscope,
et vous pensez que ces images sont les dernières qu'il vous sera
permis de voir. Vous êtes désormais préparé à mourir et vous
vous sentez calme et paisible. Mais, tout à coup, vous sentez que
votre corps est retenu par des fibres invisibles et solides. Une
terrible secousse vous coupe le souffle et vous laisse tout étourdi.
Un miracle est en train de se produire : vous ne tombez plus,
mais vous remontez ! Vous êtes pris dans une espèce de filet aux
mailles serrées, comme une mouche dans une toile d'araignée.
Vous êtes hissé vers la Nef du ciel aussi rapidement que vous
tombiez et trois Nains barbus, vêtus de pourpoints de combat
éclatants, vous aident à monter à bord. Cependant, vous n'avez
même pas le temps de les remercier, car le petit vaisseau du ciel
subit l'assaut redoublé des Kraans et de leurs cavaliers. Au bout
du pont, un Nain est aux prises avec un Drakkar hargneux. Le
petit homme semble en très mauvaise posture mais alors que
vous vous précipitez pour lui venir en aide, un autre des cruels
guerriers Drakkars vient atterrir au centre du vaisseau, sur la
plateforme fortifiée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez aider le Nain, rendez-vous au :"))
    st.page_link("tomes/tome5/page_280.py", label="280", icon="📄")
    st.write_stream(stream_text("Si vous préférez enjamber le bastingage et vous élancer vers la plate-forme, rendez-vous au :"))
    st.page_link("tomes/tome5/page_361.py", label="361", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
