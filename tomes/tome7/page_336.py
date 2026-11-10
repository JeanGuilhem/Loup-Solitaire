import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=336, book=7)

fr_text = """
Un nouveau bruit s'ajoute brusquement aux cris perçants des
rats : un craquement de bois qui éclate. En moins d'une minute,
votre petite embarcation est complètement engloutie sans laisser
aucune trace. Les rochers déchiquetés vous écorchent les mains
et les genoux mais, surmontant la douleur, vous continuez votre
escalade. Une fois sur la plage, vous commencez à courir, mais
vous vous enfoncez dans le sable noir jusqu'aux chevilles et vous
êtes obligé à chaque pas de tirer violemment sur vos jambes
endolories. Vous regardez par-dessus votre épaule et apercevez la
horde des rats qui gagne rapidement du terrain. Ils vous auront
rejoint avant que vous n'arriviez au pied de la paroi rocheuse de
Kazan-Oud ! Mais les cris cessent brusquement. Le flot noir des
rongeurs s'est arrêté brusquement au bord de la plage. Leurs
dents blanches luisent dans l'obscurité et leurs yeux affamés
continuent à surveiller vos moindres mouvements, mais ils
restent immobiles, comme cloués sur les rochers. Vous continuez
à courir en vous demandant pourquoi les rats ont arrêté leur
poursuite. A quelques mètres devant vous apparaît l'horrible
réponse à votre question.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome7/page_221.py", label="221", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
