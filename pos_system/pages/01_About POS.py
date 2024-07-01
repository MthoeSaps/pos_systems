import streamlit as st
from streamlit_extras import colored_header
from streamlit_extras.streaming_write import write
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_option_menu import option_menu
import pandas as pd 
import plotly.graph_objects as go
import plotly.express as px

st.toast("Data Tree", icon="🪐")
st.title("Data Tree Saint Inc. Data Science and analysis engine")

tab1,tab2,tab3,tab4,tab5 = st.tabs([":blue[**Home**]", ":blue[**Data Representation**]", ":blue[**GIS**]", ":blue[**About**]", ":blue[**FAQ**]"])
with tab1:
        st.empty()
with tab2:
        st.empty()
with tab3:
        st.empty()
with tab4:
        option = ["About Data Tree","User Manual", "Contact Us", "Developer"]
        choice = st.selectbox("About Us",option)
        st.write(f":orange[**You're viewing the {choice} section**]")

        if choice == "About Data Tree":
            st.title(":blue[**Northveil Incorporated**]")
            st.write(":blue[**Private Limited Company**]")

            selected = option_menu(
                menu_title="Data Tree",
                options= ["Home", "Services", "Metric Data", "Affiliated Partners"],
                menu_icon="tree",
                icons=["house", "tools", "controller", "person-circle"],
                orientation="horizontal",
                styles={
                    "container": {"padding": "initial","background-color": '#0E1117', "boarder-color": 'orange'},
                    "icon": {"color":"grey","font-size": "15px"},
                    "nav-link": {"color":"grey","font-size": "12px", "text-align": "initial", "margin":"10px"},
                    "nav-link-selected": {"background-color": "white"},
                    }
                    )
            
            if selected == "Home":
                st.write("- :blue[Welcome to the official Northveil Inc. (PVT) LTD Online Informatics Platform]")
                st.write("- :gray[Use this website in order to get upto date info with our upcoming projects and most importantly we will be updating our key perfomence indicators for stock]")
                st.write("- :orange[Navigate to our DT Metrics Data option on the menu and view some shares we have listed for sale and our stock value, Do not miss out on the opportunity to invest in tech companies today]")

            if selected == "Metric Data":
                st.write(":blue[Data Tree stock market dashboard]")
                st.write(":orange[Metric Dashboard]")

                col1, col2, col3, = st.columns(3)
                col1.metric(label="MS ConTech share(%)", value="$405.00", delta=1.00, help=" %")
                col2.metric(label="Terra Vista Licencing share(%)", value="$720.00", delta=3.57, help=" %")
                col3.metric(label="Northveil Inc.(%)", value="N/A", delta= -1, help=" %")
                style_metric_cards()

                df = pd.read_excel("Data\pc.xlsx")
                def preview():
                    yield pd.DataFrame(df)
                if st.button("Preview"):
                    write(preview)

                st.write(":orange[**Bar Graph Stock Display**]")
                fig = px.bar(
                    df,
                    x="Project Name ",
                    y="Project Value (USD)",
                    color="Cost Per Share ($ per 1%)"
          )
                st.plotly_chart(fig)

                st.write(":orange[**Pie Chart Stocks Display**]")
                chart2 = px.sunburst(
                df,
                path=["Project Name ", "Project Value (USD)"],
                values="Max Number of Investors",
                color="Share Percentage Available (%)"
                )
                st.plotly_chart(chart2)
                
                st.write(":orange[**Area Stock Chart**]")
                fig = px.area(
                  df,
                  x="Project Name ",
                  y="Project Value (USD)",
                  color="Cost Per Share ($ per 1%)",
                  line_group="Share Percentage Available (%)"
                  )
                st.plotly_chart(fig)

        if choice == "User Manual":
            st.empty()
        if choice == "Contact Us":
            st.empty()
        if choice == "Developer":
            st.empty()
with tab5:
     st.title(":orange[**Frequently Asked Question**]")
     st.write("- :blue[**Our filter Team has found these Requests and Reviews pressing**]")

     avatar = """
        <img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
        """

     faq1 = """
- **1.  When are guys giving us the directions ft?**
"""
     faq2 = """
- **2.  How much do you guys charge for deliveries**
"""
     faq3 = """
- **3.  Can i view your prices offline**
"""
     faq4 = """
- **4.  How original are the products you produce**
"""     

     with st.expander(faq1):
            st.markdown(avatar,unsafe_allow_html=True)
            st.write(":orange[**Am not into spoilers but probably next month you'll see**]")
     with st.expander(faq2):
            st.markdown(avatar,unsafe_allow_html=True)
            st.write(":blue[**Its absolutely freee, we value our customers that much**]")
     with st.expander(faq3):
            st.markdown(avatar,unsafe_allow_html=True)
            st.write(":blue[**[Pricinglist](wa.me/+263782012633)🪐 This is our whatsapp business catalog, tap the link**]")
     with st.expander(faq4):
            st.markdown(avatar,unsafe_allow_html=True)
            st.write(":orange[**All our products are from original sources, promotion or contract sales are also original products from our trusted sources dont worry**]")
