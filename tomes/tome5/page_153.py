import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=153, book=5)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Maouk ordonne à ses troupes de fouiller les lieux tout en les
menaçant de mort si vous réussissez à vous échapper. Vous
serrez les dents et vous attendez qu'un heureux hasard se
produise. Vous passez d'un bateau à l'autre en rampant et vous
arrivez bientôt devant un escalier en pierre. Vous grimpez les
marches et vous apercevez une petite place pavée au bout de
laquelle s'étend un véritable dédale de ruelles tortueuses qui
disparaissent dans l'obscurité du Quartier des Voleurs. Vous avez
presque traversé la place lorsqu'un cri retentit du quai : « Le
voilà ! » Vous vous engagez en courant dans une rue déserte,
puis vous grimpez les marches d'un escalier qui donne sur une
petite cour. Le bruit des sabots claquant sur les pavés en
contrebas vous fait accélérer l'allure. Vous avez trois issues
possibles : une porte cloutée à votre gauche, une allée à votre
droite et, devant vous, une ruelle pavée qui mène droit à un
porche. Les hommes de Maouk sont sur vos talons et vous devez
prendre une décision rapide.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous désirez ouvrir la porte, rendez-vous au :'))
    st.page_link("tomes/tome5/page_75.py", label="75", icon="📄")

    st.write_stream(stream_text("Si vous voulez suivre l'allée, rendez-vous au :"))
    st.page_link("tomes/tome5/page_117.py", label="117", icon="📄")

    st.write_stream(stream_text('Si vous décidez de prendre la ruelle pavée vers le porche, rendez-vous au :'))
    st.page_link("tomes/tome5/page_169.py", label="169", icon="📄")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au :"))
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome5/page_42.py", label="42", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome5/page_42.py", label="42", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
