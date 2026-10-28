import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=33, book=3)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Vous jetez le jeune garçon sur le traîneau, vous agrippez votre
fouet et vous cinglez l'échine des chiens Kanu qui se mettent à
courir de toutes leurs forces. Les Barbares des Glaces vous
donnent immédiatement la chasse, criant quelque chose à
l'enfant dans leur étrange langage. Vous avez parcouru moins
d'une centaine de mètres lorsque le garçon saute soudain du
traîneau pour atterrir sur un grand tas de neige. Au même
instant, une volée de flèches aux pointes d'os vous sifflent aux
oreilles et l'une d'elles vous écorche l'épaule, vous faisant perdre
1 point d'ENDURANCE. Bien que l'enfant soit libre, à présent,
deux des Barbares continuent de vous poursuivre ; mais vos
chiens sont rapides et vous avez tôt fait de les distancer, eux et
leurs flèches. A la nuit tombée, vous arrivez en bordure des
monts de Viad. Ces impressionnantes montagnes de granite
dressent leurs parois verticales au-dessus de la neige et de la
glace et il vous sera impossible de les franchir par cette nuit
froide et sans lune. En outre, un vent venant de l'ouest annonce
du blizzard pour les heures qui viennent. Il vous faut trouver un
abri, ou vous mourrez de froid.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-1)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-1)

    st.write_stream(
        stream_text(
            'Si vous souhaitez vous diriger vers le nord pour chercher cet abri, rendez-vous au :'
        )
    )
    st.page_link("tomes/tome3/page_27.py", label="27", icon="📄")

    st.write_stream(stream_text('Si vous préférez aller au sud, rendez-vous au :'))
    st.page_link("tomes/tome3/page_314.py", label="314", icon="📄")

    st.write_stream(
        stream_text(
            "Enfin si vous maîtrisez les Disciplines Kaï de l'Orientation ou du Sixième Sens, "
            'rendez-vous au :'
        )
    )
    if has_kai("L'Orientation") or has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome3/page_348.py", label="348", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_348.py", label="348", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
