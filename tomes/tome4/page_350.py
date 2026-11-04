import streamlit as st
from inventory import (
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=350, book=4)

fr_text = """
Tandis que meurt Barraka, le vent se met à souffler plus fort et
son mugissement s'intensifie, emplissant le temple d'une longue
plainte désespérée. Vous sentez l'esprit maléfique et glacé de
Vashna, Maître des Ténèbres, vous envelopper dans une ultime
étreinte, mais il ne peut rien contre vous, le sacrifice a été
empêché, et il est désormais condamné à se lamenter, en rêvant
d'une victoire qui ne viendra jamais. Le Poignard de Vashna
repose sur le sol noir du temple. Vous le ramassez et vous le
glissez dans votre ceinture (inscrivez-le sur votre Feuille
d'Aventure dans la case Objets Spéciaux.) La diabolique flamme
bleue s'est éteinte et, aussi longtemps que vous resterez en
possession de cette arme maudite, Vashna, Maître des Ténèbres,
et ses légions de guerriers morts, demeureront prisonniers du
gouffre maudit. Vous libérez la blonde Madelon, attachée sur
l'autel, et vous la portez à l'air libre à travers les couloirs du
temple. Lorsque vous émergez parmi les ruines que baigne la
clarté de la pleine lune, un spectacle extraordinaire s'offre à vos
yeux. Les Guerriers de Barraka fuient en tous sens la cité
fantôme, poursuivis par une armée de cavaliers. Les flammes de
leurs Torches et le clair de lune illuminent le soleil qui orne leurs
tuniques. C'est l'armée du Sommerlund commandée par le roi
Ulnar en personne qui leur donne ainsi la chasse. Vos
compatriotes lancent des cris enthousiastes pour saluer votre
courage, et leurs acclamations étouffent les longs gémissements
qui s'élèvent des profondeurs du gouffre maudit. Une fois de
plus, vous vous êtes révélé comme un authentique héros de votre
patrie. Lorsque vous déposez Madelon dans les bras de son père,
l'intensité de son bonheur vous donne le sentiment d'avoir
pleinement accompli votre mission. En vérité, vous êtes plus que
tout autre digne du titre de Seigneur Kaï. Vous avez triomphé à
l'issue d'une quête périlleuse, mais vos exploits ne s'arrêteront
pas ici. L'épopée du Loup Solitaire, dernier des Seigneurs Kaï, est
loin en effet d'être terminée car un nouveau défi, tout aussi
implacable que les précédents, vous attend à présent dans le
cinquième volume de la série.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        add_to_inventory("POIGNARD DE VASHNA")
        st.balloons()
    st.write("*Le Poignard de Vashna a été ajouté à vos Objets Spéciaux.*")
    st.success(
        "**Mission accomplie !** Barraka est mort et le sacrifice de Madelon a été empêché : Vashna et ses "
        "légions de guerriers morts demeurent prisonniers du Gouffre Maudit. "
        "Le Loup Solitaire peut reprendre la route dans le tome 5, *Le Tyran du Désert*."
    )
    st.page_link("tomes/tome5/debut.py", label="Continuer avec le tome 5", icon="📜")
    st.page_link("accueil.py", label="Retour à l'accueil", icon="🏠")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
