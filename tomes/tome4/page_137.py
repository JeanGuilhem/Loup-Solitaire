import streamlit as st
from inventory import (
    change_endurance,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=137, book=4)

fr_text = """
Tout autour de la barricade, les ennemis refluent en désordre.
Les cornes de guerre des brigands sonnent la retraite, exhortant
les Guerriers vaincus à fuir le champ de bataille. Jubilant, le
capitaine Gayal émerge de la fumée les yeux brillants comme des
joyaux sous les bords de son casque cabossé. «Nous avons
triomphé, Loup solitaire, s'exclame-t-il, l'ennemi est vaincu ! »
Les hommes du capitaine ont entrepris de rebâtir la barricade et
de soigner leurs camarades blessés. La vue des soldats
sommerlundais morts dans la bataille vous attriste, mais vous
vous consolez en songeant que les pertes de vos agresseurs sont
infiniment plus lourdes. Le capitaine vous emmène à la tour de
guet où l'on soigne vos blessures à l'aide d'herbes de Laumspur.
Vous regagnez aussitôt 6 points d'ENDURANCE. « Nous avons
vaincu ces brigands, mais je crains bien qu'il ne s'agisse là que
d'un bref répit, dit le capitaine dont le visage à présent a pris une
expression grave et sombre. Le sacrifice de la fille du baron
Vanalund doit être empêché à tout prix si nous voulons éviter la
catastrophe. Nous n'aurions pas la force en effet de nous opposer
aux légions des morts ressuscités de leur tombe. » Les vers de la
prophétie vous reviennent aussitôt en mémoire et un frisson
vous parcourt l'échine quand vous repensez à la menace qu'ils
font peser. Dans trois jours, lorsque la lune sera pleine, Barraka
sacrifiera la fille du baron dans le temple souterrain et ce
sacrifice libérera les morts des gorges de Maaken, le gouffre
maudit. Il vous faut à tout prix empêcher ce sacrifice.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(6)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=6)

    st.write_stream(stream_text('Rendez-vous au :'))
    st.page_link("tomes/tome4/page_12.py", label="12", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
