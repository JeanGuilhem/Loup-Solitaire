import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    kai_rank,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=282, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous quittez le beffroi et vous descendez vers la sentinelle. Il
vous est tout d'abord facile de progresser, tout en restant caché,
en passant de tourelle en tourelle, mais pour les trente derniers
mètres vous serez à découvert, car la plate-forme d'atterrissage et
le toit du Palais sont reliés par une passerelle exposée à la vue de
tout le monde. Si vous décidez de neutraliser la sentinelle, vous
devrez traverser la passerelle sans vous faire remarquer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez la Discipline Kaï de la Maîtrise Psychique de la Matière, rendez-vous au :"))
    if has_kai("Maîtrise Psychique de la Matière"):
        st.page_link("tomes/tome5/page_295.py", label="295", icon="📄")
        st.page_link("tomes/tome5/page_357.py", label="357", icon="📄", disabled=True)
        st.page_link("tomes/tome5/page_389.py", label="389", icon="📄", disabled=True)
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_295.py", label="295", icon="📄", disabled=True)

        st.write_stream(stream_text("Si vous ne possédez pas cette Discipline, utilisez la Table de Hasard pour obtenir un chiffre. Si vous maîtrisez la Discipline Kaï du Camouflage, ou bien la Discipline Kaï de la Chasse, ajoutez 2 points au chiffre que vous avez tiré. Si vous avez le titre de Guerrier Kaï (ou un rang plus élevé), ajoutez 3 points au chiffre que vous avez tiré."))
        roll = hazard_roll()
        if roll is not None:
            bonus = 0
            if has_kai("Le Camouflage") or has_kai("La Chasse"):
                bonus += 2
            if kai_rank() >= 8:
                bonus += 3
            total = roll + bonus
            if bonus:
                st.write(f"*Bonus : +{bonus}, soit un total de {total}.*")
            if total <= 4:
                st.write_stream(stream_text("Si le résultat obtenu est compris entre 0 et 4, rendez-vous au :"))
                st.page_link("tomes/tome5/page_357.py", label="357", icon="📄")
            else:
                st.write_stream(stream_text("Si ce même résultat est supérieur ou égal à 5, rendez-vous au :"))
                st.page_link("tomes/tome5/page_389.py", label="389", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
