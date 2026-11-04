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

check_inventory(current_page_number=95, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous faites surface à côté d'une petite embarcation bâchée. Affolé
à l'idée qu'il puisse y avoir des Sangsues géantes dans les eaux du
port de Barrakeesh, vous vous hissez à bord de la barque et vous
vous dissimulez sous la toile grossièrement tissée qui la recouvre.
La distance que vous avez parcourue à la nage vous a fait perdre
haleine, mais vous n'osez pas émettre le moindre souffle car les
hommes de Maouk sont partout, patrouillant le long des quais et
scrutant la surface de l'eau pour repérer le moindre signe de vie
de votre part. Si vous voulez tenter de vous enfuir, il vous faudra
auparavant détourner l'attention des soldats.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous au :"))
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome5/page_184.py", label="184", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_184.py", label="184", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, rendez-vous au :"))
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome5/page_56.py", label="56", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_56.py", label="56", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
