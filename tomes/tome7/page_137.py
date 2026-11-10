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

check_inventory(current_page_number=137, book=7)

fr_text = """
Par un immense effort de volonté, vous ordonnez au serpent de
ne plus s'approcher. Son œil unique vous fixe d'un regard glacé,
la fente de ses pupilles se dilatant et se rétrécissant au rythme de
ses pulsations cardiaques. L'odieux reptile oscille au-dessus de
vous, hésitant à attaquer; votre pouvoir Kaï a semé le trouble
dans cet esprit primitif, refrénant ses instincts meurtriers à
l'égard d'un humain au sang chaud tel que vous. Tandis que la
monstrueuse tête se balance de droite à gauche comme un
métronome, vous apercevez dans le fond l'entrée d'un tunnel,
que le corps du serpent et son nid avaient jusque là dissimulée à
vos regards. A la vue de cette issue, vous reprenez courage, mais,
dans le même temps, vous relâchez votre concentration. Le serpent en profite aussitôt pour passer à l'attaque !
Heureusement, l'extraordinaire rapidité de vos réflexes vous
sauve la vie : les crochets à venin se referment dans le vide, et
vous reprenez immédiatement le contrôle psychique de l'animal.
Celui-ci bat en retraite, puis se love au centre de la pièce, la tête
posée au milieu de ses anneaux, prêt à dormir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous voulez attaquer le serpent, rendez-vous au :"))
    st.page_link("tomes/tome7/page_219.py", label="219", icon="📄")

    st.write_stream(stream_text("Si vous préférez vous contenter de le contourner, afin de gagner l'entrée du tunnel, rendez-vous au :"))
    st.page_link("tomes/tome7/page_260.py", label="260", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
