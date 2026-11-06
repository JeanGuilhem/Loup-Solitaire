import streamlit as st
from inventory import (
    check_inventory,
    clear_flag,
    display_inventory,
    end_page,
    set_flag,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=245, book=6)

fr_text = """
Tout d'abord, notez le nombre de Pièces d'Or que vous souhaitez
parier, dans la marge de votre Feuille d'Aventure. Vous
réfléchissez au problème et vous arrivez à la conclusion qu'il n'y a
que quatre combinaisons possibles et vous répétez tout bas avant
de prendre votre décision. «Je suis un garçon», dit l'enfant aux
cheveux noirs. «Je suis une fille », dit celui aux cheveux blonds.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # Fait posé : « pari : N » (N = mise), réglé aux paragraphes 50, 62, 113 et 223
    bet = st.session_state.get("visibility_pari_245")
    if not bet:
        amount = st.number_input(
            "Pièces d'Or que vous pariez", min_value=1, max_value=max(1, st.session_state.purse),
            value=1, step=1, key="pari_245",
        )
        if st.button("Parier", disabled=st.session_state.purse < 1):
            for flag in [f for f in st.session_state.get("story_flags", []) if f.startswith("pari : ")]:
                clear_flag(flag)
            set_flag(f"pari : {int(amount)}")
            st.session_state["visibility_pari_245"] = int(amount)
            st.rerun()
    else:
        st.write(f"*Vous avez parié {bet} Pièce(s) d'Or.*")

    st.write_stream(stream_text("Si vous concluez que les deux enfants ont dit la vérité, rendez-vous au :"))
    st.page_link("tomes/tome6/page_50.py", label="50", icon="📄", disabled=not bet)

    st.write_stream(stream_text("Si vous concluez que le premier enfant a dit la vérité et que le second a menti, rendez-vous au :"))
    st.page_link("tomes/tome6/page_113.py", label="113", icon="📄", disabled=not bet)

    st.write_stream(stream_text("Si vous concluez que le premier enfant a menti et que le second a dit la vérité, rendez-vous au :"))
    st.page_link("tomes/tome6/page_223.py", label="223", icon="📄", disabled=not bet)

    st.write_stream(stream_text("Enfin, si vous pensez que les deux ont menti, rendez-vous au :"))
    st.page_link("tomes/tome6/page_62.py", label="62", icon="📄", disabled=not bet)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
