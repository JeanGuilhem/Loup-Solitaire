import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=19, book=3)

fr_text = """
Vous courez le long du pont de glace et vous plongez pour
attraper la main de Dyce, mais il est trop tard. Une seconde à
peine avant que vous ne l'ayez atteint, il lâche prise et tombe en
arrière dans le vide béant. Un frisson vous parcourt l'échine
tandis que vous entendez son hurlement disparaître dans les
profondeurs obscures. Vous scrutez le fond du précipice sans
pouvoir rien faire, lorsqu'Irian pousse soudain un cri : « Là,
là-bas ! s'exclame-t-il, je suis sûr que j'ai vu quelque chose ! » Vous
regardez avec attention dans l'espoir de voir quelque chose à
votre tour, mais la gorge est aussi noire qu'une nuit sans lune.
Vous vous tournez alors vers Irian qui vous désigne non pas le
précipice, mais l'horizon en direction de l'ouest. « Regardez
là-bas ! » dit-il en montrant une hauteur qui se dessine au loin.
Deux guerriers vêtus de fourrure se tiennent debout au sommet
d'une vaste étendue de glace. Ils regardent vers vous, alertés sans
aucun doute par le cri désespéré de Dyce. « Des Barbares des
Glaces, avertit Fenor, la voix tremblante de peur, s'ils atteignent
Ikaya avant nous, c'est comme si nous étions déjà morts ! » Vous
êtes à présent à 25 kilomètres de la forteresse et il reste moins de
trois heures de jour.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            'Si vous souhaitez poursuivre votre chemin en espérant que vous arriverez avant les '
            'Barbares, rendez-vous au :'
        )
    )
    st.page_link("tomes/tome3/page_327.py", label="327", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous préférez les attaquer pour les empêcher de donner l'alerte, rendez-vous au :"
        )
    )
    st.page_link("tomes/tome3/page_307.py", label="307", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
