# Page 1: Details
import streamlit as st
from app_data_loader import load_data_brsma, load_data_lcl, process_data_lcl, process_data_brsma
import app_styles as app_styles
from _pages import homepage
# import matplotlib.pyplot as plt




#-------------#
# "homepage.py"
#-------------#
def page_home():
    st.subheader("🏠Home")
    st.write("This application helps you track and analyze your expenses.")

