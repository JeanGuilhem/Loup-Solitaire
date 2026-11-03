import streamlit as st
from inventory import (
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    show_illustrations,
    show_map,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=57, book=4)

fr_unknown_item = "Vous ne possédez pas cet objet."

fr_text = """
« Il faut que vous la sauviez, Loup Solitaire, s'écrie le baron d'une
voix brisée par l'émotion. Il faut à tout prix empêcher ce sacrifice. »
« Sauvez qui ? Qui donc doit-il sauver ? » interroge le capitaine
Gayal en essayant de calmer le baron. « Ma fille Madelon, bien
entendu », répond ce dernier. Ses yeux rougis sont baignés de
larmes et il se tord les mains en un geste nerveux. Il récite alors
cette sinistre prophétie :
Au soir de pleine lune, en un temple profond,
Sacrifice viendra à jamais réveiller
Les légions d'un Seigneur trop longtemps oublié.
Quand mourra sur l'autel la vierge aux cheveux blonds,
Des gorges de Maaken, les morts se lèveront
Pour exiger enfin la rançon des guerriers.

« Vous ne comprenez donc pas ? poursuit le baron. Barraka a
trouvé le poignard de Vashna et il s'apprête à sacrifier ma fille
sur l'autel du Temple pour libérer les morts des gorges de
Maaken, le gouffre maudit. Au temps de la lune noire, explique-t-il,
le roi Ulnar du Sommerlund tua Vashna, le plus puissant des
Maîtres des Ténèbres, à l'aide du Glaive de Sommer, l'épée du
soleil. Le corps de Vashna et les cadavres de tous ses soldats
furent ensuite jetés dans l'abîme sans fond des gorges de
Maaken. Barraka veut à présent mener les morts à la victoire en
conquérant d'abord le Sommerlund, puis l'ensemble des Fins de
Terre. » Dans un silence terrifié vous observez le baron dont le
regard exprime toute la détresse. Si Barraka accomplit le
sacrifice, tout est perdu. Que pourrait faire une armée de mortels
face aux légions des morts ? Le capitaine Gayal vous emmène
hors de la pièce et referme la porte derrière lui. « Je craignais
qu'il ne soit fou, dit-il, et j'ai refusé de l'écouter, mais les
événements de ces derniers jours confirment mon pire
cauchemar. Il dit la vérité. » Un frisson vous parcourt l'échine
tandis que vous repensez à l'épouvantable prophétie, mais
bientôt vous êtes arraché à votre sombre méditation par le son
aigu d'une corne de guerre. Le capitaine Gayal s'approche
aussitôt d'une meurtrière à travers laquelle il scrute la plaine
désolée. Il se tourne ensuite vers vous, le visage d'un gris de
cendre. « Les brigands, dit-il, ils nous attaquent. »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Si vous possédez l'Épée du capitaine Gayal, rendez-vous au :"))
    if has_item("ÉPÉE DE GAYAL"):
        st.page_link("tomes/tome4/page_327.py", label="327", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_item))
        st.page_link("tomes/tome4/page_327.py", label="327", icon="📄", disabled=True)

    st.write_stream(stream_text("Sinon, rendez-vous au :"))
    st.page_link("tomes/tome4/page_289.py", label="289", icon="📄", disabled=has_item("ÉPÉE DE GAYAL"))

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
