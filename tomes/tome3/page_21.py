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
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=21, book=3)

fr_text = """
Vous tombez dans un sifflement glacé et vous atterrissez
brutalement sur une surface gelée, près de 10 mètres plus bas.
Vous avez le souffle coupé et vous êtes durement secoué, mais
vous gardez conscience. Les cris des guides se transforment
bientôt en hurlements de joie et de surprise lorsqu'ils vous voient
vous relever tant bien que mal. Vous levez les yeux et vous voyez
Irian qui saute sans encombre par-dessus la crevasse. Quelques
secondes plus tard, on vous descend une corde et vous êtes
ramené sain et sauf à la surface. Vous avez perdu vos chiens
Kanu, votre traîneau avec les provisions qu'il contenait et 2
points d'ENDURANCE. Après s'être concertés avec vous, vos
guides sont d'accord pour poursuivre la mission, bien qu'ils
sachent que, désormais, les épreuves qui les attendent seront
deux fois plus pénibles. En scrutant l'horizon, Irian repère alors
un passage étroit au bord de la banquise à l'endroit où elle jouxte
la plaine de Hrod. Vous vous remettez en chemin et, lorsque le
soir tombe, vous avez atteint l'abri de ce passage où vous décidez
d'installer votre campement. En faisant l'inventaire des
provisions qui vous restent, vous vous apercevez qu'il faudra
diminuer les rations de moitié si vous voulez arriver tous à Ikaya.
La frugalité de votre dîner vous fait perdre 1 autre point
d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # 2 points pour la chute, 1 pour le dîner rationné
    if is_new_page():
        change_endurance(-3)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome3/page_325.py", label="325", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
