import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_magnakai,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=145, book=7)

fr_text = """
Vous ouvrez votre Sphère de Feu en deux et vous approchez la
flamme magique qu'elle recèle de la pellicule transparente qui
vous emprisonne. Celle-ci fond instantanément, et une vague
d'air frais s'engouffre dans la bulle qui explose comme un ballon
trop gonflé. Gardant la Sphère de Feu à la main, vous vous frayez
aisément un chemin parmi les autres bulles. Au fur et à mesure
que la flamme perce les globes gélatineux, vous les entendez
exploser et tomber mollement sur le sol. Vous continuez ensuite
à avancer, les yeux écarquillés afin de repérer le moindre signe
de danger. Au loin, vous apercevez justement une grande ombre
projetée sur le sol et vous redoublez de vigilance. Mais vos
craintes se muent en désarroi quand vous découvrez que l'ombre
est en fait un gouffre noir et profond, déchirant le passage sur
une dizaine de mètres. Au-dessus de vous, l'éclaircissement
soudain de la brume annonce le retour inopiné du crâne :
Le moyen de traverser défie votre regard :
Trouvez-le, sinon gare à la bagarre !
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de l'Écran Psychique ou de l'Intuition, rendez-vous au :"))
    if has_magnakai("Écran Psychique") or has_magnakai("Intuition"):
        st.page_link("tomes/tome7/page_39.py", label="39", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_39.py", label="39", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez ni l'une ni l'autre de ces disciplines, rendez-vous au :"))
    st.page_link("tomes/tome7/page_261.py", label="261", icon="📄", disabled=has_magnakai("Écran Psychique") or has_magnakai("Intuition"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
