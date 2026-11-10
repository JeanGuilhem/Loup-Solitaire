import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=85, book=7)

fr_text = """
L'ascension se révèle particulièrement longue et difficile ; c'est
même la plus éprouvante que vous ayez jamais accomplie ! Vous
trouvez à peine la place de caler vos pieds dans de minuscules
anfractuosités de la roche et vous grimpez pratiquement à la
seule force des bras. Vous progressez avec une lenteur
désespérante, et les efforts que vous devez fournir sont, de plus,
freinés par de violentes bourrasques de pluie et de vent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard et ajoutez 2 au chiffre que vous avez tiré. Si vous maîtrisez la Discipline Magnakaï de l'Art de la Chasse et si vous avez atteint le rang de Maître Primat, déduisez 2 du résultat précédent. Le chiffre final représente le nombre de points d'ENDURANCE que vous perdez au cours de cette pénible ascension."))
    roll = hazard_roll(key="ascension")
    if roll is not None:
        lost = max(0, roll + 2 - (2 if has_magnakai("Art de la Chasse") else 0))  # rang de Maître primat : toujours atteint au tome 7
        # perte appliquée une seule fois par visite
        if not st.session_state.get("visibility_t7_85_ascension"):
            st.session_state["visibility_t7_85_ascension"] = True
            change_endurance(-lost)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-lost)
        st.write_stream(stream_text("Finalement, vous arrivez en haut, à moitié mort de fatigue et les membres tout endoloris, puis vous vous approchez de la brèche qui s'ouvre dans le rempart de la forteresse. Rendez-vous au :"))
        st.page_link("tomes/tome7/page_27.py", label="27", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
