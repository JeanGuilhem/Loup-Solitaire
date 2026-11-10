import streamlit as st
from combat import combat
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=301, book=7)

fr_text = """
Le serpent ouvre les mâchoires, et vous apercevez avec effroi ses
crochets étincelants de venin qui brillent dans la lumière froide
comme la lame recourbée de grands sabres. Vous saisissez votre
arme et, le dos appuyé contre le mur de pierres humides, vous
attendez le bon moment pour frapper. La tête monstrueuse se
balance maladroitement d'un côté à l'autre, et vous apercevez
alors un petit tunnel creusé dans le mur d'en face, qui était
auparavant caché par le serpent et son nid. Vous reprenez
courage en pensant que vous allez enfin pouvoir échapper à ce
cauchemar mais, tout d'abord, vous devez combattre l'hideuse
créature. Si vous ne maîtrisez pas la Discipline Magnakaï de la
Science Médicale, doublez tous les points d'ENDURANCE que
vous perdrez au cours du combat, à cause des morsures
venimeuses du monstre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # venin : sans Science Médicale, vos pertes d'ENDURANCE sont doublées
    outcome = combat([("HACTARON GÉANT", 22, 60)], flee_after=4,
                     ls_loss_multiplier=1 if has_magnakai("Science Médicale") else 2)
    if outcome == "fled":
        st.write_stream(stream_text("Après 4 Assauts, vous pouvez essayer de fuir la créature en courant vers le tunnel ; rendez-vous, dans ce cas, au :"))
        st.page_link("tomes/tome7/page_91.py", label="91", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Si vous remportez le combat, rendez-vous au :"))
        st.page_link("tomes/tome7/page_21.py", label="21", icon="📄")
    elif outcome is None:
        st.caption("Après 4 Assauts, vous pourrez fuir vers le tunnel (rendez-vous alors au 91).")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
