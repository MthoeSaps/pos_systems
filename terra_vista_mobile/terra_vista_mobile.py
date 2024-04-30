import streamlit as st
import pandas as pd
import openpyxl
import os
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import time
import geopandas as gpd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from streamlit_extras.colored_header import colored_header
from streamlit_option_menu import option_menu
from streamlit.logger import get_logger
from streamlit.elements.lib.column_types import Column
from streamlit.elements.map import Data
from PIL import Image

st.set_page_config(page_title="Terra Vista Bulawayo Mapping Engine", page_icon=":🌏:", layout="wide", initial_sidebar_state="expanded")

st.title("Terra Vista Mobile")
st.text("Mobile Edition")
st.divider()
#with st.container(border=True):
 #   img = Image.open("C:/Users/Mthoko/source/repos/terra_vista_mobile/img/Blue and White Minimalist Travel App Logo_20240427_135856_0000.png")
  #  st.image(img,caption="Explore our world the tech savy way", width=320)
    
with st.sidebar:
    with st.container(border=True, height=300):
        img = Image.open("terra_vista_mobile/img/Blue and White Minimalist Travel App Logo_20240427_135856_0000.png")
        st.image(img,caption="Explore Bulawayo the tech savy way", width=250)
        st.divider()
    
    selected = option_menu(
    menu_title = "Terra Vista Mobile Menu",
    options = ["🏡 Home","🗺 Maps and Visuals","☎Contact me here"],
    menu_icon = "Map",
    default_index = 0,
    )
    with st.form("my_form", clear_on_submit=True):
        st.write("**Rate my software**")
        slider_val = st.slider("How do you rate this tool", help="Slide to the desired precentage(%)")
        checkbox_val = st.checkbox("Did you find this engine useful?", help="Check the box if True")
        submitted = st.form_submit_button("Submit")
        if submitted: st.write("Rating", slider_val, "Helpful", checkbox_val)
    
if selected == "🏡 Home":
    with st.container(border=True):
        st.info("""Welcome, to the official Terra Vista Bulawayo Mapping Engine Platform: Mobile Version. Terra Vista is a powerful mapping and analytics software 
                that unlocks the potential of location data. With Terra Vista, you can visualize, analyze, and collaborate using contextual tools. Whether
                you’re a business, researcher, or government agency, Terra Vista provides flexible licensing options and a cloud-based infrastructure for 
                smarter decision-making.""")
        
            
            

if selected == "🗺 Maps and Visuals":
    #st.subheader("Bulawayo Maps")
    st.write("Upload your data on the Excel File Uploader below and access the data on the diffent menu options")
    uploaded_file = st.file_uploader("Choose a XLSX file", type="xlsx")
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
    else:
        pass
    st.divider()
    with st.container(border=True):
        st.subheader("Bulawayo Maps 🗺")
    st.text("Use the select box below to switch between maps.")
    menu = ["Bulawayo Open Street Map", "Bulawayo Carto Positron Map", "Bulawayo Carto Darkmatter Map"]
    choice = st.selectbox("Analyse Bulawayo Interactive Maps",menu)
    st.divider()
    if choice == "Bulawayo Open Street Map":
        #df = pd.read_excel('C:/Users/Mthoko/source/repos/terra_vista_pc/dbs/bulawayo_map 20240331_101353_update1.xlsx')
        if uploaded_file is not None:
            st.subheader("Bulawayo Open Street Map")
            df = pd.read_excel(uploaded_file)
            fig = px.scatter_mapbox(df,
                                lat="latitude ", lon="longitude",
                                hover_name="Suburb",
                                text=None,
                                hover_data=None,
                                custom_data=None,
                                size=None,
                                animation_frame=None,
                                animation_group=None,
                                category_orders=None,
                                labels=None,
                                color_discrete_sequence=None,
                                color_discrete_map=None,
                                color_continuous_scale=None,
                                range_color=None,
                                color_continuous_midpoint=None,
                                opacity=None,
                                size_max=None,
                                center=None,
                                title=None,
                                template=None,
                                width=None,
                                #color="Suburb",
                                zoom=10,
                                height=400)
            fig.update_layout(mapbox_style="open-street-map")
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            st.plotly_chart(fig)
    else:
        pass
    if choice == "Bulawayo Carto Positron Map":
        if uploaded_file is not None:
            st.subheader("Bulawayo Carto Positron Map")
            df = pd.read_excel(uploaded_file)
            fig = px.scatter_mapbox(df, lat="latitude ", lon="longitude",
                            hover_name="Suburb",
                            text=None,
                            hover_data=None,
                            custom_data=None,
                            size=None,
                            animation_frame=None,
                            animation_group=None,
                            category_orders=None,
                            labels=None,
                            color_discrete_sequence=None,
                            color_discrete_map=None,
                            color_continuous_scale=None,
                            range_color=None,
                            color_continuous_midpoint=None,
                            opacity=None,
                            size_max=None,
                            center=None,
                            mapbox_style=None,
                            title=None,
                            template=None,
                            width=None,
                            color="Suburb",
                            zoom=10,
                            height=400)
            fig.update_layout(mapbox_style="carto-positron")
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            st.plotly_chart(fig)
    else:
        pass
    if choice == "Bulawayo Carto Darkmatter Map":
        if uploaded_file is not None:
            st.subheader("Bulawayo Carto Darkmatter Map")
            df = pd.read_excel(uploaded_file)
            fig = px.scatter_mapbox(df, lat="latitude ", lon="longitude",
                            hover_name="Suburb",
                            text=None,
                            hover_data=None,
                            custom_data=None,
                            size=None,
                            animation_frame=None,
                            animation_group=None,
                            category_orders=None,
                            labels=None,
                            color_discrete_sequence=None,
                            color_discrete_map=None,
                            color_continuous_scale=None,
                            range_color=None,
                            color_continuous_midpoint=None,
                            opacity=None,
                            size_max=None,
                            center=None,
                            mapbox_style=None,
                            title=None,
                            template=None,
                            width=None,
                            color="Suburb",
                            zoom=10,
                            height=400)
            fig.update_layout(mapbox_style="carto-darkmatter")
            fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
            st.plotly_chart(fig)
    else:
        pass
    with st.container(border=True):
        st.title("Excel file Visuals 📈")
    if uploaded_file:
        df = pd.read_excel(uploaded_file,
                           #usecols = "D:I",
                           engine="openpyxl")
        df_participants = pd.read_excel(uploaded_file, engine="openpyxl")
        df_participants.dropna(inplace=True)
        with st.container(border=False):
            st.subheader("Pie Chart Visual of the dataset")
            pie_chart = px.pie(df_participants,
                               #title="Coordinate Piechart",
                               values="longitude",
                               names="Suburb")
            st.plotly_chart(pie_chart)
            st.subheader("Bargraph visuals")
            bar = px.bar(
                df,
                x="Suburb",
                y="latitude ",
                color="longitude",
                color_continuous_scale=["red","yellow","green"],
                template="plotly_white"
                )
            st.plotly_chart(bar)
    with st.container(border=True):
        st.title("Data Tables")
    if uploaded_file:
        df = pd.read_excel(uploaded_file,
                           #usecols = "D:I",
                           engine="openpyxl")
       
        
if selected == "☎Contact me here":
    st.subheader("Use these buttons to get in touch with me")
    st.link_button("Contact me on WhatsApp", "https://wa.me/263777932721") 
    st.link_button("Email me here", "https://mthoesaps06@gmail.com") 
    st.link_button("View my LinkedIn Profile", "https://www.linkedin.com/in/mthokozisi-sapuwa-1ab2151ab?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app") 
    st.link_button("Find me on Instagram", "https://www.instagram.com/mthoe.zw?utm_source=qr&igsh=MTlrZWlvdW1pNGI4bA")
    st.link_button("Check me out Facebook", "https://www.facebook.com/mthokozisi.sapuwa.50?mibextid=kFxxJD")
    
    
    

