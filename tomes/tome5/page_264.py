import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=264, book=5)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Tout à coup, un son suraigu éclate au-dessus du mugissement du
vent, vous faisant terriblement souffrir de la tête. Vous êtes
attaqué par une puissante force psychique. A moins que vous ne
maîtrisiez la Discipline Kaï du Bouclier Psychique, diminuez de 2
points votre total actuel d'ENDURANCE. L'Itikar frissonne, puis
secoue frénétiquement la tête de gauche à droite lorsque le bruit
strident retentit à nouveau : le grand oiseau agonise, détruit par
l'explosion psychique. Tandis que vous regardez par-dessus votre
épaule, vous apercevez, l'estomac noué par la peur, un Kraan qui
fond sur vous pour vous attaquer. Il porte sur son dos un
adversaire de taille : un Vordak, un des redoutables morts
vivants dont les Seigneurs des Ténèbres ont fait leurs lieutenants.
Au moment où le Kraan se précipite sur vous, le Vordak étend
ses bras revêtus de rouge puis saute de la selle. Il atterrit juste
derrière vous, sur le dos de l'Itikar, ses doigts de squelette
profondément enfoncés dans la chair hérissée de plumes de votre
monture. Le choc vous projette en avant et vous contraint à
lâcher ses rênes. L'oiseau géant, horrifié, hurle de douleur et de
peur lorsque la prise du Vordak lui paralyse la colonne
vertébrale. Vous devez réagir rapidement, car l'Itikar tombe
comme une pierre vers la plaine salée du lac Inrahim.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if has_kai("Bouclier psychique"):
        st.success("*Votre Bouclier Psychique vous protège de cette attaque.*")
    else:
        if is_new_page():
            change_endurance(-2)
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(stream_text("Si vous possédez le Glaive de Sommer, rendez-vous au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome5/page_315.py", label="315", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome5/page_315.py", label="315", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous ne possédez pas cet Objet Spécial, rendez-vous au :"))
    if has_item("GLAIVE DE SOMMER"):
        st.page_link("tomes/tome5/page_299.py", label="299", icon="📄", disabled=True)
    else:
        st.page_link("tomes/tome5/page_299.py", label="299", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
