import streamlit as st
from inventory import (
    can_shoot,
    check_inventory,
    display_inventory,
    end_page,
    is_new_page,
    show_illustrations,
    show_map,
    use_arrow,
)
from utils import called_cookies, stream_text

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=276, book=7)

fr_text = """
Vous visez en silence et vous tirez. Votre flèche s'enfonce jusqu'à
l'empenne dans le crâne de la créature assise à votre gauche. Les
autres créatures se mettent à pousser des cris d'horreur et de
surprise et bondissent de leur siège pour s'abriter derrière la
table. Soudain, le tintement d'une cloche retentit dans la pièce, et
vous entendez des bruits de pas précipités dans le couloir. Quatre
guerriers, revêtus de rutilantes armures noires, font irruption
dans la pièce, l'arme à la main. Ils regardent le cadavre de la
créature un court instant, puis se jettent sur vous frénétiquement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        use_arrow()  # la flèche décochée
    st.caption(f"Vous avez décoché une flèche : il vous en reste {st.session_state.get('arrows', 0)}.")

    st.write_stream(stream_text("Si vous souhaitez tirer une autre flèche, rendez-vous au :"))
    st.page_link("tomes/tome7/page_50.py", label="50", icon="📄", disabled=not (can_shoot()))

    st.write_stream(stream_text("Si vous préférez passer votre arc en bandoulière et tirer une autre arme, rendez-vous au :"))
    st.page_link("tomes/tome7/page_316.py", label="316", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    show_map()

end_page()
