import streamlit as st
from inventory import (
    add_arrows,
    add_to_inventory,
    check_inventory,
    display_inventory,
    end_page,
    has_item,
    has_magnakai,
    pickup_button,
    show_illustrations,
    show_map,
)
from text import fr_unknown_magnakai
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=56, book=7)

fr_text = """
Vous fouillez rapidement les corps de vos victimes dans l'espoir
de trouver sur elles quelque chose qui éclairerait quelque peu le
mystère de Kazan-Oud. Après avoir vidé leurs poches et inspecté
leur équipement, vous passez en revue les divers objets avant de
faire votre choix :
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.markdown("- 2 Haches (Armes)\n- 1 Arc (Arme)\n- 2 Lances (Armes)\n- 1 Carquois contenant 4 Flèches\n- Provisions équivalentes à 4 Repas (Repas)\n- 1 Sachet d'Herbes (Objet de Sac à Dos)\n- 1 Bouteille de Vin (Objet de Sac à Dos)")
    pickup_button("HACHE", key="hache_1", label="Prendre une Hache")
    pickup_button("HACHE", key="hache_2", label="Prendre la seconde Hache")
    pickup_button("ARC", key="arc", label="Prendre l'Arc")
    pickup_button("LANCE", key="lance_1", label="Prendre une Lance")
    pickup_button("LANCE", key="lance_2", label="Prendre la seconde Lance")
    # le Carquois et ses 4 flèches : si vous avez déjà un Carquois, vous n'en prenez que les flèches
    quiver_label = "Prendre les 4 Flèches (dans votre Carquois)" if has_item("CARQUOIS") else "Prendre le Carquois et ses 4 Flèches"
    if st.button(quiver_label, key="pickup_carquois_56", disabled=bool(st.session_state.get("visibility_carquois_56"))):
        if not st.session_state.get("visibility_carquois_56"):
            if has_item("CARQUOIS") or add_to_inventory("CARQUOIS"):
                add_arrows(4)
                st.session_state["visibility_carquois_56"] = True
                st.rerun()
    for index in range(1, 5):
        pickup_button("REPAS", key=f"repas_{index}", label=f"Prendre un Repas ({index}/4)")
    pickup_button("SACHET D'HERBES", key="herbes", label="Prendre le Sachet d'Herbes")
    pickup_button("BOUTEILLE DE VIN", key="vin", label="Prendre la Bouteille de Vin")

    st.write_stream(stream_text("Si vous maîtrisez la Discipline Magnakaï de la Science Médicale et que vous souhaitez identifier les herbes contenues dans le sachet, rendez-vous au :"))
    if has_magnakai("Science Médicale"):
        st.page_link("tomes/tome7/page_129.py", label="129", icon="📄")
    else:
        st.write_stream(stream_text(fr_unknown_magnakai))
        st.page_link("tomes/tome7/page_129.py", label="129", icon="📄", disabled=True)

    st.write_stream(stream_text("Si vous préférez examiner le sarcophage, rendez-vous au :"))
    st.page_link("tomes/tome7/page_83.py", label="83", icon="📄")

    st.write_stream(stream_text("Si vous jugez plus prudent de quitter le vestibule en empruntant le tunnel qui s'ouvre à votre gauche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_201.py", label="201", icon="📄")

    st.write_stream(stream_text("Si vous voulez plutôt vous engager dans le tunnel par où les Hommes-Bêtes avaient surgi, rendez-vous au :"))
    st.page_link("tomes/tome7/page_323.py", label="323", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
