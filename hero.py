"""
Point d'entrée de l'app : déclare toutes les pages (accueil + paragraphes des tomes)
et affiche celle demandée. Les pages ne sont pas listées dans la barre latérale :
on navigue uniquement par les liens des paragraphes.
"""
import glob
import os

import streamlit as st

BOOKS = ["tome1", "tome2", "tome3"]


def book_pages(book: str) -> list:
    """Toutes les pages d'un tome. L'URL est préfixée par le tome : les numéros se répètent d'un tome à l'autre."""
    return [
        st.Page(path, url_path=f"{book}_{os.path.basename(path)[:-3]}")
        for path in sorted(glob.glob(f"tomes/{book}/*.py"))
    ]


home = st.Page("accueil.py", title="Accueil", icon="🏠", default=True)
stats = st.Page("statistiques.py", title="Statistiques", icon="📊", url_path="statistiques")
pages = [home, stats] + [page for book in BOOKS for page in book_pages(book)]
st.navigation(pages, position="hidden").run()
