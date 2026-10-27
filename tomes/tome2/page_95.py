import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_kai,
    show_illustrations,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=95, book=2)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."
fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
Vous lancez votre cheval à grands coups d'éperons parmi les arbres
enchevêtrés et vous arrivez bientôt dans une petite clairière. Là, six
Squalls surexcités sont en train de sautiller autour du corps convulsé
d'un homme étendu sur le sol. Une lance à la hampe sculptée de motifs
étranges est enfoncée dans sa poitrine et le cadavre d'un Chevalier de la
Montagne Blanche repose à côté de lui. Les Squalls échangent des cris
perçants et semblent tout à fait indifférents au sort de l'homme blessé
qui visiblement agonise sous leurs yeux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous souhaitez attaquer les Squalls, rendez-vous au :"))
    st.page_link("tomes/tome2/page_28.py", label="28", icon="📄")

    st.write_stream(
        stream_text(
            "Si vous maîtrisez la Discipline Kaï de la Guérison ou si vous disposez d'une potion de "
            "guérison ou d'herbe de Laumspur, vous pouvez essayer de sauver la vie de l'homme blessé en"
            " vous rendant au :"
        )
    )
    can_heal = has_kai("La Guérison") or any(
        has_item(name)
        for name in (
            "POTION DE GUÉRISON",
            "PETITE POTION DE GUÉRISON",
            "FIOLE DE LAUMSPUR",
            "MOISSON DE LAUMSPUR",
            "LAUMSPUR",
        )
    )
    if can_heal:
        st.page_link("tomes/tome2/page_239.py", label="239", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome2/page_239.py", label="239", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_2.jpg")

end_page()
