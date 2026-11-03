import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, hazard_roll, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=343, book=4)

fr_text = """
Vous vous trouvez au milieu de la rivière souterraine lorsque
l'eau noire se met soudain à frémir et à bouillonner. Vous vous
cramponnez au bord du bateau en ordonnant à vos hommes de
ramer de toutes leurs forces ; les remous menacent en effet de
vous faire chavirer. Soudain, un tentacule verdâtre et répugnant
jaillit à la surface. Il s'abat sur l'embarcation comme la lanière
d'un fouet, fracassant le bois de la coque, et s'enroule autour de
deux de vos hommes. Avant même que vous n'ayez pu dégainer
votre arme, les deux malheureux sont emportés dans les
profondeurs bouillonnantes. Un autre tentacule surgit aussitôt.
Cette fois il ondule dans votre direction et essaie de vous frapper
pour vous jeter par-dessus bord.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre. Si votre total actuel d'ENDURANCE est supérieur à 20, vous ajouterez 3 au chiffre que vous aurez tiré. Si votre total d'ENDURANCE est actuellement égal ou inférieur à 12, vous devrez ôter 2 points au chiffre donné par la Table."))
    roll = hazard_roll()
    if roll is not None:
        bonus = 3 if st.session_state.endurance > 20 else (-2 if st.session_state.endurance <= 12 else 0)
        total = roll + bonus
        if bonus:
            st.write(f"*ENDURANCE {st.session_state.endurance} : {bonus:+d}, soit un total de {total}.*")
        if total <= 6:
            st.write_stream(stream_text("Si vous obtenez un total de 2 à 6, rendez-vous au :"))
            st.page_link("tomes/tome4/page_194.py", label="194", icon="📄")
        else:
            st.write_stream(stream_text("De 7 à 12, rendez-vous au :"))
            st.page_link("tomes/tome4/page_61.py", label="61", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
