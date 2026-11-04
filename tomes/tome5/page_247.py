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

check_inventory(current_page_number=247, book=5)

fr_text = """
Le voyage que vous effectuez à travers les Foos est absolument
extraordinaire. La Nef du ciel se faufile en planant entre de
hautes colonnes de pierre qui s'élèvent de la vallée. Ces pitons
rocheux forment un paysage fantastique d'une grandeur
surnaturelle. Très loin en dessous, au fond de la vallée, des bulles
d'eau sulfureuse montent lentement des fissures du sol orangé et
des flots de lave incandescente creusent en grondant des canaux
circulaires qui rougeoient tel des douves remplies de feu liquide.
Vous observez le ciel, mais il n'y a aucun signe d'une présence
ennemie. « Ikaresh, le "Repaire de l'Aigle", dit pensivement
Banedon, c'est là que nous trouverons Tipasa le Vagabond, car
Ikaresh est sa ville natale et toute sa famille y demeure. Bien qu'il
passe la majeure partie de son temps à errer dans la Mer de la
Sécheresse, il finit toujours par retourner chez les siens. » Après
avoir traversé les Foos, vous atteignez, en fin d'après-midi, les
collines qui dominent la ville d'Ikaresh. Banedon pose la Nef du
ciel au sommet d'un rocher, puis il lance une échelle de corde au
sol. Il a été convenu que Banedon et vous irez à pied jusqu'à
Ikaresh, afin de rechercher Tipasa, tandis que Nolrim et
l'équipage attendront votre retour en cachant la Nef dans les
environs. En effet, la vue de la Nef du ciel survolant la ville
risquerait de donner à votre arrivée une publicité quelque peu
gênante. Avec Banedon, vous préparez votre expédition en vous
enduisant le visage avec une pâte brune tirée des baies de copalla
et en revêtant les habits gris et blancs communément portés par
les montagnards de cette région. Ainsi déguisés, vous dites adieu
à Nolrim et vous partez à travers les collines nues et désolées.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Utilisez la Table de Hasard pour obtenir un chiffre."))
    number = hazard_roll()
    if number is not None and number <= 2:
        st.write_stream(stream_text("Si le chiffre que vous avez tiré est compris entre 0 et 2, rendez-vous au :"))
        st.page_link("tomes/tome5/page_337.py", label="337", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("Si ce chiffre est compris entre 3 et 9, rendez-vous au :"))
        st.page_link("tomes/tome5/page_383.py", label="383", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
