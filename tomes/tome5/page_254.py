import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=254, book=5)

fr_text = """
L'air frais vous fouette le visage tandis que vous tombez vers le
lac Inrahim. Les Kraans et leurs cavaliers, le vaisseau du ciel et
l'horizon lointain se mêlent pour former un véritable
kaléidoscope de couleurs et vous redoutez que ce soient là les
dernières images qu'il vous sera donné de voir. Vous vous êtes
déjà préparé à mourir et vous vous sentez calme et paisible. Mais
soudain, vous sentez que votre corps est retenu par une masse de
fibres collantes, puis une secousse terrible vous coupe le souffle
et vous engourdit. L'impossible se réalise : vous perdez 2 points
d'ENDURANCE mais vous n'êtes plus en train de tomber, vous
remontez dans les airs ! Vous avez été pris dans un filet aux
cordes poisseuses, comme une mouche dans une toile d'araignée.
Vous voilà soulevé dans le ciel vers le vaisseau volant aussi
rapidement que vous tombiez auparavant. Soudain trois Nains
barbus, vêtus de pourpoints de guerre chatoyants vous hissent
sur la passerelle qui fait le tour de la coque. Mais vous n'avez
guère le temps de leur témoigner votre reconnaissance car le
petit vaisseau est sous le feu de l'attaque des Drakkars
chevauchant les Kraans. Au bout de la passerelle, un Nain se bat
à mains nues contre un Drakkar qui pousse de terribles cris. Le
Nain est en train de perdre la bataille et, tandis que vous
approchez pour lui prêter main-forte, un autre de ces cruels
guerriers atterrit au milieu du vaisseau, en haut de la plate-forme
fortifiée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous souhaitez aider le Nain, rendez-vous au :"))
    st.page_link("tomes/tome5/page_280.py", label="280", icon="📄")

    st.write_stream(stream_text("Si vous préférez sauter de la passerelle sur la plate-forme fortifiée, rendez-vous au :"))
    st.page_link("tomes/tome5/page_361.py", label="361", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
