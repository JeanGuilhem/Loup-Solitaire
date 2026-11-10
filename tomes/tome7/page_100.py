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

check_inventory(current_page_number=100, book=7)

fr_text = """
Vous pénétrez dans une pièce où se dresse une grande statue en bronze. Vous reconnaissez immédiatement la coiffure caractéristique et les vêtements d'un Zakhan, souverain de l'empire du désert de Vassagonie. La statue est figée dans une attitude de détresse absolue ; son visage reflète la tristesse la plus désespérée, et ses bras sont tendus en avant, dans un geste implorant. Derrière la statue, vous apercevez une porte ovale encastrée dans le mur, mais elle est fermée à clé. Entretemps, la brume s'est éclaircie. Le crâne réapparaît et se met à parler d'une voix aussi douce et chaleureuse que le croassement d'un corbeau :

Écoutez les paroles du Zakhan,  
Et méditez ce qu'il dira ;  
Donnez la bonne réponse,  
Ou bien il vous en pâtira !

Sur ces mots, le crâne disparaît à nouveau dans la brume. A votre grande stupéfaction, vous voyez alors les lèvres de la statue se mettre à remuer. L'écho d'une voix rauque et sépulcrale s'élève des profondeurs du grand corps de métal : « Ma fille a plusieurs sœurs ; elle a autant de sœurs que de frères, mais chacun de ses frères a deux fois plus de sœurs que de frères. Dites-moi donc, brave guerrier, combien ai-je de fils et de filles ? »
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Réfléchissez bien et, lorsque vous aurez trouvé la réponse à cette énigme, notez en premier le nombre de fils, puis le nombre de filles qu'a le Zakhan. Ensuite, rendez-vous au paragraphe portant ce chiffre pour numéro."))
    code = st.number_input("Nombre de fils, suivi du nombre de filles", min_value=1, max_value=350, value=None, step=1, key="code_100")
    if code == 34:
        st.page_link("tomes/tome7/page_34.py", label="34", icon="📄")
    elif code is not None:
        st.write("*La statue reste muette : ce n'est pas la bonne réponse.*")

    st.write_stream(stream_text("Si vous n'arrivez pas à résoudre l'énigme du Zakhan, rendez-vous au :"))
    st.page_link("tomes/tome7/page_270.py", label="270", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
