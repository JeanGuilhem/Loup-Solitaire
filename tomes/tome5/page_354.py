import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=354, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous vous élancez sur le pont, mais la hache vous entaille la
cuisse, dessinant sur votre peau une longue estafilade violacée.
Vous perdez 2 points d'ENDURANCE. Brusquement, une
explosion assourdissante retentit et le guerrier Drakkar est
projeté en arrière, la cuirasse déchirée par le tir d'un Nain. Puis il
bascule dans les ténèbres environnantes en poussant un long cri
d'agonie. Depuis Barrakeesh, un grondement de tonnerre roule,
menaçant, à travers la plaine obscurcie. La ville elle-même
semble maudire votre fuite ! Banedon surgit à vos côtés, très
inquiet de votre sort. Il vous tend une main tremblante pour vous
aider à vous mettre sur pieds et vous remarquez alors que le
pansement de fortune qui entoure sa blessure est trempé de
sang. Le jeune magicien est livide et semble au bord de
l'évanouissement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de la Guérison, rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome5/page_377.py", label="377", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_377.py", label="377", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, rendez-vous au :"))
    if has_kai("La Guérison"):
        st.page_link("tomes/tome5/page_339.py", label="339", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_339.py", label="339", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
