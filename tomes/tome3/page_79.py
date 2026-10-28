import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    remove_from_inventory,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=79, book=3)

fr_text = """
Vous entrouvrez la porte, juste assez pour pouvoir verser la fiole
de Ronces des Cimetières dans le gruau bouillonnant. Vous
n'avez pas à attendre très longtemps : bientôt, les Barbares des
Glaces ont absorbé leur dernier dîner, et dès que leurs cadavres
sont étendus sur le sol, vous commencez à inspecter la cuisine en
toute tranquillité. C'est une petite cuisine qui comporte des
réserves d'herbes étonnamment abondantes. « Elles viennent
sans doute des comptoirs de Liouk », dit Loi-Kymar en regardant
le contenu des bocaux et des pots rangés sur des étagères. Il
prend plusieurs bocaux d'herbes et les entasse dans les vastes
poches de sa toge. Vous avez hâte, pour votre part, de quitter les
lieux, de peur que d'autres gardes n'arrivent, mais le vieux
magicien semble complètement absorbé par ses découvertes. Il
ouvre deux petits bocaux et en mélange le contenu en insistant
pour que vous partagiez avec lui cette mixture. « Elle vous
donnera des forces, Loup Solitaire », assure-t-il. Tandis que vous
mangez les feuilles séchées qu'il vous offre, vous sentez tout votre
corps rayonner de chaleur. Vous gagnez 6 points d'ENDURANCE
à ajouter à votre total actuel.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        remove_from_inventory("POTION DE RONCES DES CIMETIÈRES")  # la fiole est versée dans le gruau
        before = st.session_state.endurance
        change_endurance(6)
        st.session_state["visibility_herbs"] = st.session_state.endurance - before
    st.metric(label="Endurance", value=st.session_state.endurance, delta=st.session_state.get("visibility_herbs") or 0)

    st.write_stream(stream_text('Rendez-vous à présent au :'))
    st.page_link("tomes/tome3/page_301.py", label="301", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
