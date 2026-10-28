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

check_inventory(current_page_number=238, book=3)

fr_text = """
Les deux jours qui suivent sont un véritable enfer. Des blocs de
glace se dressent continuellement sur votre chemin, vous forçant
à descendre des traîneaux et à les manœuvrer à la main pour
parvenir à passer. Vous avancez lentement et les chiens Kanu
sont nerveux, prenant peur à la moindre occasion. Souvent, les
traîneaux se renversent, répandant leur chargement sur le sol.
Un brouillard de neige fine réduit la visibilité, provoquant par
deux fois la chute de Fenor et d'Irian dans des crevasses ;
heureusement, la corde de sécurité permet de les ramener sans
dommage à la surface. C'est ensuite au tour de votre traîneau de
disparaître dans une crevasse. Dyce se porte volontaire pour
descendre dans le gouffre à l'aide d'une corde afin de décharger
le traîneau : ainsi allégé, il sera possible de le hisser et de le
récupérer. Après deux heures d'efforts harassants, vous parvenez
enfin à remonter le traîneau mais vous vous apercevez alors qu'il
a subi des dégâts irréparables et qu'il ne reste plus qu'à
l'abandonner. Une tempête se lève bientôt à l'ouest et souffle si
violemment que vous avez du mal à vous maintenir debout. En
quelques minutes, les conditions météorologiques sont devenues
trop mauvaises pour continuer. Vous dressez donc la tente et
vous attendez que la tempête se calme. Des heures durant, la
toile de la tente claque sans répit sous le souffle impitoyable du
vent. Et, tandis que vous laissez le sommeil vous gagner peu à
peu, vous vous demandez quelles autres épreuves vous attendent
le lendemain. Vous n'avez alors aucune idée de l'étonnant
spectacle qui s'offrira à vos yeux dès votre réveil.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome3/page_117.py", label="117", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
