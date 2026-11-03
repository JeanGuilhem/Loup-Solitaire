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

check_inventory(current_page_number=159, book=4)

fr_text = """
Vous vous étendez parmi les blés et vous retenez votre souffle, les
nerfs tendus comme des cordes de violon, en attendant que la
patrouille soit passée. Des centaines de créatures minuscules
grouillent le long des tiges jaunes. Votre corps tout entier
commence à vous démanger. De toute évidence, ces insectes se
sont introduits sous vos vêtements. La sueur ruisselle sur vos
joues et les démangeaisons deviennent si insupportables que
vous êtes sur le point de laisser échapper un cri. Vous vous
retenez cependant tandis que les brigands passent à quelques
centimètres de votre cachette sans remarquer le moins du monde
votre présence. Lorsque vous êtes sûr qu'ils se sont suffisamment
éloignés, vous vous relevez d'un bond et vous vous grattez
frénétiquement. Vous découvrez alors avec horreur que vos
jambes sont couvertes d'insectes qui se repaissent de votre sang.
Vous vous débarrassez en hâte de vos vêtements, vous videz vos
bottes de ces créatures et vous les arrachez de votre peau, avant
de vous rhabiller et de poursuivre votre chemin le long du
sentier.
Les insectes vous ont fait perdre 2 points d'ENDURANCE en suçant votre sang.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_204.py", label="204", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
