import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_kai,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=85, book=3)

fr_text = """
Pendant trois jours et trois nuits, vous avancez à grand-peine sur
le glacier au tracé sinueux. Les chutes, les bleus, les tibias
écorchés, les crevasses, les blocs de glace coupants comme des
rasoirs et le vent mordant qui souffle sans cesse se conjuguent
pour épuiser vos forces. Vous avez cependant la chance
d'échapper à un blizzard et vous parvenez enfin, après une
marche harassante, à atteindre l'abri du mont des Brumes au
pied duquel vous décidez d'établir votre campement. Cette
immense montagne de près de 4 000 mètres d'altitude a la forme
d'un gigantesque aileron de requin. Lorsque les vents d'ouest
soufflent à son sommet, ils entraînent de longs panaches de
brume à travers le glacier de Viad ; c'est cet étrange phénomène
qui a donné son nom à la montagne. Vous trouvez bientôt
l'endroit idéal pour dresser votre tente, sur un sol couvert de
rocaille. En quelques instants, tout est installé et vous voilà à
nouveau dans votre abri de toile. Avant de vous endormir, vous
sortez quelques minutes pour satisfaire une exigence de la nature ;
c'est alors que, par un pur hasard, vous apercevez une faible
lueur qui filtre à travers une fissure de la paroi rocheuse, au-
dessus de vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez aller voir de plus près cette lueur insolite, rendez-vous au :'))
    st.page_link("tomes/tome3/page_49.py", label="49", icon="📄")

    st.write_stream(stream_text('Si vous préférez ne pas y prêter attention et retourner sous votre tente, rendez-vous au :'))
    st.page_link("tomes/tome3/page_212.py", label="212", icon="📄")

    st.write_stream(stream_text('Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au :'))
    if has_kai("Le Sixième Sens"):
        st.page_link("tomes/tome3/page_98.py", label="98", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome3/page_98.py", label="98", icon="📄", disabled=True)

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
