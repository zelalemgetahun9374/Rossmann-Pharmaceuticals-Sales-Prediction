import os
import sys

sys.path.append(os.path.abspath(os.path.join('./pages')))

import page1
import page2
import streamlit as st

PAGES = {
  "Home": page1,
  "Dashboard": page2,
}

selection = st.sidebar.radio("Go to page", list(PAGES.keys()))
page = PAGES[selection]
page.app()
