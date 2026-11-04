import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=210, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous vous jetez au sol et votre connaissance Kaï vous fait
échapper à la hache qui arrive en tournoyant sur la plate-forme.
Soudain, une explosion assourdissante retentit et le Drakkar est
violemment projeté en arrière, la cuirasse déchirée par le tir du
Nain, puis il disparaît dans les ténèbres qui entourent la Nef du
ciel en lâchant un dernier cri. Comme en réponse au tir, un coup
de tonnerre menaçant roule dans le ciel au-dessus de la plaine
assombrie de Barrakeesh et vous avez l'impression que la ville
entière maudit votre fuite. Très inquiet, Banedon surgit à vos
côtés. Il vous tend une main tremblante pour vous aider à vous
relever et vous remarquez que le pansement de fortune qui
protège sa blessure est tout trempé de sang. Son visage est blême
et vous avez l'impression qu'il va s'évanouir d'une seconde à
l'autre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

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
