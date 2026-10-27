import streamlit as st
from combat import combat
from inventory import (
    add_to_inventory,
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    is_new_page,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=106, book=2)

fr_text = """
La lance sculptée est en métal et pourtant elle est aussi légère que si
elle avait été taillée dans du bois. Vous remarquez que la hampe est
gravée de caractères runiques et de symboles magiques. Vous la retirez
avec précaution de la poitrine de l'homme blessé qui pousse un long
soupir de soulagement. Vous vous apprêtez ensuite à examiner sa
blessure lorsqu'une subite douleur vous déchire la tête. Vous avez si
mal que vous vous écroulez sur le sol en perdant 2 points
d'ENDURANCE. Vous êtes alors stupéfait de voir l'homme se relever
d'un bond, mais votre surprise se change en horreur quand soudain il se
métamorphose devant vos yeux. La peau de son visage se convulsé et
change de couleur ; elle prend une teinte de plus en plus sombre et se
ratatine en se décomposant à vue d'œil. Le crâne de l'homme apparaît,
ses yeux s'enflamment d'une lueur rouge et brillante et de longs crocs
jaillissent de sa mâchoire. La terreur vous saisit à la gorge lorsque vous
comprenez enfin que cette créature est en réalité un MONSTRE
D'ENFER, un de ces effroyables serviteurs des Maîtres des Ténèbres.
Le monstre vous attaque en se servant de sa puissante Force Mentale et,
si vous ne maîtrisez pas la Discipline Kaï du Bouclier Psychique, vous
perdrez 2 points d'ENDURANCE supplémentaires à chaque assaut
mené contre lui au cours du combat. La créature est invulnérable aux
armes ordinaires et à la Discipline Kaï de la Puissance Psychique. Vous
ne pouvez la blesser qu'à l'aide de la Lance Magique, celle-là même qui
était fichée dans sa poitrine.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-2)
        # la Lance Magique, retirée de la poitrine du blessé, est la seule arme qui blesse le monstre
        if not has_item("LANCE MAGIQUE"):
            add_to_inventory("LANCE MAGIQUE")
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

    st.write_stream(
        stream_text(
            "Il vous est impossible de prendre la fuite et vous devrez poursuivre ce combat jusqu'à la mort "
            "de l'un des deux adversaires."
        )
    )
    outcome = combat([("MONSTRE D'ENFER", 22, 30)], psychic_immune=True, psychic_damage=2)
    if outcome == "win":
        st.write_stream(
            stream_text(
                "Vous avez le droit de conserver la Lance Magique : elle est rangée dans vos Objets Spéciaux. "
                "Rendez-vous ensuite au :"
            )
        )
        st.page_link("tomes/tome2/page_320.py", label="320", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
