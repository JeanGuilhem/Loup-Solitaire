import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=372, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Une flèche vous atteint à l'épaule au moment où vous atteignez le
chemin de ronde, ce qui vous oblige à plonger derrière le mur du
parapet, pour vous mettre à l'abri. Vous perdez 1 point
d'ENDURANCE. Deux autres flèches rebondissent sur le parapet,
à quelques centimètres de votre tête. La porte en pierre est
fermée par un verrou en fer, mais pour le faire glisser vous
devrez vous exposer au tir des arbalètes car la serrure se trouve
bien au-dessus du petit muret de protection.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)
    st.write_stream(stream_text("Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous au :"))
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome5/page_269.py", label="269", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_269.py", label="269", icon="📄", disabled=True)
    st.write_stream(stream_text("Si vous ne maîtrisez pas cette Discipline, utilisez la Table de Hasard pour obtenir un chiffre. Si vous avez le titre d'Aspirant Kaï ou un titre plus élevé, ajoutez 2 points au chiffre que vous avez tiré."))
    if not has_kai("Maîtrise Psychique de la Matière"):
        roll = hazard_roll()
        if roll is not None:
            bonus = 2 if kai_rank() >= 6 else 0
            total = roll + bonus
            if bonus:
                st.write(f"*Bonus de votre rang Kaï : +2, soit un total de {total}.*")
            if total <= 3:
                st.write_stream(stream_text("Si le résultat obtenu est compris entre 0 et 3, rendez-vous au :"))
                st.page_link("tomes/tome5/page_366.py", label="366", icon="📄")
            else:
                st.write_stream(stream_text("Si ce résultat est supérieur, rendez-vous au :"))
                st.page_link("tomes/tome5/page_277.py", label="277", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
