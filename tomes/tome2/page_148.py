import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, handle_repas

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=148, book=2)

fr_text = """
Vous vous enveloppez dans votre cape de Seigneur Kaï et vous en
relevez le capuchon. Le cocher lance un cri puis fouette ses chevaux et
bientôt la diligence file sur la route bordée d'arbres qui longe la côte en
direction de Ragadorn. Au cours du trajet, vous bavardez avec le cocher
qui vous donne des renseignements fort utiles concernant le port de
Ragadorn. Depuis la mort de Killean le Suzerain, trois ans auparavant,
la ville est dirigée (et fort mal, d'après votre interlocuteur) par son fils
Lachelan. Ses hommes et lui ne sont en fait que des brigands qui
accablent le peuple d'impôts et assassinent quiconque s'oppose à leur
pouvoir. Tandis que le cocher vous parle, vous vous sentez tenaillé par
la faim et il vous faut à tout prix prendre un repas, sinon vous perdrez 3
points d'ENDURANCE. Quelques heures plus tard, la ville de
Ragadorn se dessine dans le lointain. Une cloche sonne les douze coups
de midi et bientôt la diligence franchit la porte Ouest de la cité puis
s'arrête au relais. « Si vous voulez vous rendre à Durenor, vous devrez
prendre une autre diligence au relais de la porte Est, mais dépêchez-
vous, car le départ est prévu à une heure. » Vous remerciez le cocher
pour ces renseignements et vous sautez sur la chaussée recouverte de
pavés. Vous êtes alors frappé par l'effroyable puanteur qui baigne ce
port sinistre. Une enseigne rouillée accrochée à la façade en ruines
d'une maison porte ces mots : « Bienvenue à Ragadorn ».
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()
    st.write_stream(stream_text("Si vous souhaitez aller vers le sud le long de l'avenue de la porte Ouest, rendez-vous au :"))
    st.page_link("tomes/tome2/page_323.py", label="323", icon="📄")
    st.write_stream(stream_text("Si vous préférez vous diriger au nord en suivant le quai de l'Est, rendez-vous au :"))
    st.page_link("tomes/tome2/page_122.py", label="122", icon="📄")
    st.write_stream(stream_text("Enfin, si vous choisissez plutôt d'aller vers l'est en empruntant la rue de la Hache, rendez-vous au :"))
    st.page_link("tomes/tome2/page_257.py", label="257", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
