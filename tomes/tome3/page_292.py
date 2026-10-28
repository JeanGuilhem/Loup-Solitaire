import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=292, book=3)

fr_text = """
La lourde porte s'ouvre en coulissant latéralement et laisse
apparaître un long pont de pierre qui traverse une vaste caverne
baignant dans le rougeoiement d'un feu d'enfer. Une bouffée
d'air chaud à l'odeur putride vous frappe aussitôt au visage et un
bruit assourdissant met vos oreilles à rude épreuve. A 15 mètres
en contrebas du pont, de grandes cuves de pierre sont
suspendues au-dessus de flammes ronflantes. Chacune de ces
cuves est remplie d'une substance visqueuse et bouillonnante qui
semble s'agiter en tous sens comme si elle était douée de vie. Peu
à peu, vous commencez à comprendre ce qui se passe en ce lieu
sinistre et un sentiment de peur mêlée de répulsion vous soulève
le cœur. Des rangées de socles de pierre portent en effet les
cadavres mutilés de Barbares des Glaces que l'on a écorchés et
dont la peau est épinglée de part et d'autre du corps, comme sur
une table de dissection. Des créatures hideuses s'activent autour
de chacun des cadavres: c'est une véritable légion de mutants
vampiriques qui grouillent ainsi sur un sol ruisselant de sang.
Cette caverne est un endroit hautement maléfique, un
laboratoire de cauchemar, un temple consacré par Vonotar le
Traître à l'art ténébreux de la nécromancie. De l'autre côté du
pont, une autre porte s'ouvre soudain et quatre Barbares des
Glaces mutants s'avancent vers vous d'un pas traînant. La vue de
ces malheureuses créatures vous remplit tout à la fois d'horreur
et de pitié.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text('Si vous souhaitez combattre les Barbares mutants, rendez-vous au :'))
    st.page_link("tomes/tome3/page_83.py", label="83", icon="📄")

    st.write_stream(stream_text('Si vous préférez vous enfuir de cette caverne de malheur, rendez-vous au :'))
    st.page_link("tomes/tome3/page_130.py", label="130", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
