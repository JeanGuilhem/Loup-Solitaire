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

check_inventory(current_page_number=371, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
La hache siffle dans les ténèbres et vous faites un saut de côté,
guidé uniquement par votre instinct car vous ne pouvez pas voir
le projectile meurtrier qui se dirige vers vous. Le métal noir et
tranchant s'enfonce dans votre flanc et une douleur fulgurante
vous coupe le souffle. Vous portez la main à vos côtes et vous
sentez un flot de sang chaud couler entre vos doigts. Vous perdez
4 points d'ENDURANCE. Soudain, un fracas assourdissant
retentit et le Drakkar est projeté en arrière, la cuirasse déchirée
par une balle tirée par l'un des Nains. Il bascule dans les ténèbres
qui entourent la Nef du ciel en laissant échapper un dernier cri
de douleur et d'effroi. Au loin, un roulement de tonnerre gronde
depuis Barrakeesh et traverse la plaine obscurcie, plein de
lourdes menaces, comme si la ville entière maudissait votre fuite.
Banedon surgit à vos côtés, visiblement très inquiet. Tandis qu'il
vous tend une main tremblante pour vous aider à vous relever,
vous remarquez que le pansement de fortune qui recouvre sa
blessure est plein de sang. Il est si pâle et semble tellement
affaibli que vous avez l'impression qu'il va s'évanouir d'un
moment à l'autre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-4)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-4)
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
