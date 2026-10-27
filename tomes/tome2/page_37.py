import streamlit as st
from inventory import check_inventory, display_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, handle_repas

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=37, book=2)

fr_text = """
A l'intérieur de la diligence, il fait chaud et sec. Vous secouez votre
cape de Seigneur Kaï pour la débarrasser des gouttes de pluie qui la
recouvrent et vous remarquez alors la présence de trois autres passagers :
deux femmes et un homme qui ronfle avec bruit. L'une des femmes
lève les yeux vers vous et vous adresse un sourire. «Nous arriverons à
Ragadorn dans six heures», dit-elle, puis elle dépose son panier sur le
plancher pour que vous puissiez vous asseoir à côté d'elle. Elle vous
apprend ensuite qu'elle habite Ragadorn et vous donne quelques
renseignements sur sa ville. Depuis que Killean le Suzerain est mort il y
a trois ans, raconte-t-elle, son fils Lachelan règne sur Ragadorn ; c'est
un être malfaisant entouré de mercenaires qui sont en fait de purs et
simples brigands. Ils saignent à blanc toute la population en levant de
lourds impôts et si quelqu'un a le malheur de se plaindre, il a tôt fait de
disparaître on ne sait où. La vie est bien dure là-bas et, si vous voulez
mon avis, vous feriez bien de quitter Ragadorn le plus vite possible. Au
cours de ce voyage, vous allez devoir prendre un Repas ; à défaut, vous
perdrez 3 points d'ENDURANCE. Quelques heures plus tard, vous
entendez au loin sonner une cloche. En jetant un coup d'œil par la
fenêtre de la diligence, vous apercevez le mur d'enceinte de Ragadorn.
L'attelage franchit bientôt la porte Ouest, puis s'arrête. Vous sautez à
terre et la terrible puanteur qui baigne ce port sordide vous monte
aussitôt aux narines. Une enseigne rouillée, clouée à un mur porte ces
mots : Bienvenue à Ragadorn. La femme vous indique alors que vous
pouvez prendre une autre diligence pour Port Bax au relais situé près de
la porte Est de la ville.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()
    st.write_stream(stream_text("Si vous voulez marcher en direction du nord, le long de la rue de la porte Ouest, rendez-vous au :"))
    st.page_link("tomes/tome2/page_122.py", label="122", icon="📄")
    st.write_stream(stream_text("Si vous préférez aller vers le sud en empruntant la promenade du quai de l'Est, rendez-vous au :"))
    st.page_link("tomes/tome2/page_323.py", label="323", icon="📄")
    st.write_stream(stream_text("Enfin, si vous décidez plutôt de vous orienter vers l'est en prenant la rue de la Hache, rendez-vous au :"))
    st.page_link("tomes/tome2/page_257.py", label="257", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
