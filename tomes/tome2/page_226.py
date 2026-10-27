import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    spend_gold,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=226, book=2)

fr_text = """
L'aubergiste s'exprime avec l'accent rocailleux des natifs de Ragadorn.
Il vous raconte que la ville est gouvernée par Lachelan, le fils de
Killean le Suzerain qui a été emporté trois ans plus tôt par la peste
rouge. Votre interlocuteur ne semble pas tenir Lachelan en grande
estime, il le surnomme en effet le « Prince des Voleurs ». « Lui et ses
hommes saignent le peuple à blanc en levant de lourds impôts, vous
explique-t-il, et si vous avez le malheur de vous en plaindre, vous êtes
sûr de finir dans les eaux du port avec un poignard planté entre les deux
épaules. » L'homme hoche la tête d'un air sombre et sert une autre
tournée de bière aux marins ivres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez louer une chambre pour la nuit, donnez 2 Pièces d'Or à l'aubergiste et rendez-vous au :"))
    if st.button("Payer 2 Couronnes (56)", key="pay_56", disabled=st.session_state.purse < 2):
        if spend_gold(2):
            st.switch_page("tomes/tome2/page_56.py")
    if st.session_state.purse < 2:
        st.caption("Vous ne possédez pas la somme requise.")

    st.write_stream(stream_text("Si vous préférez essayer de gagner un peu d'or en engageant une partie de bras de fer, rendez-vous au :"))
    st.page_link("tomes/tome2/page_276.py", label="276", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
