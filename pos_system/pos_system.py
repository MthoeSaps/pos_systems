import streamlit as st
import pandas as pd
import os
import plotly.graph_objects as go
import plotly.express as px
import datetime
from traceback import clear_frames
from streamlit.logger import get_logger
from streamlit_option_menu import option_menu
from streamlit_extras.colored_header import colored_header
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_extras.streaming_write import write
from streamlit_extras.badges import badge

LOGGER = get_logger(__name__)

def pos_system():
    st.set_page_config(page_title="MS Tech POS.", page_icon=":🅿️:", initial_sidebar_state="collapsed")     
    st.toast("MS Tech Hybrid POS System", icon="🅿️")
    colored_header(
        label = "**POS System 🅿️**",
        description = "**Saint Inc/Mthoe Sapps. Point of Sale Management System. Expand Sidebar for More**",
        color_name = "blue-70"
    )
    
    st.write("- :blue[**POS form, fill & submit to get started**]")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.form("my_form", 
                     clear_on_submit = True):
         customer_name = st.text_input("Enter Customer Name",
                                          placeholder = "Enter Customer Name",
                                          label_visibility = "collapsed")
         item_name = st.text_input("Enter Item Name",
                                      placeholder="Enter Item Name",
                                      label_visibility="collapsed")    
         item_price = st.number_input("Enter Item Price",
                                   min_value = 0.0,
                                   label_visibility="collapsed",
                                   placeholder="Enter Item Price",
                                   step = 0.01)
         item_quantity = st.number_input("Enter Item Quantity", 
                                    min_value = 1,
                                    label_visibility="collapsed",
                                    placeholder="Enter Item Quantity",
                                    step = 1)
         submitted = st.form_submit_button("Purchase")
    with col2:
        st.empty()
    with col3:
        if submitted:
            total = item_price * item_quantity
            st.write(f" 🧑 :orange[Customer Name:] {customer_name}")
            st.write(f" 🛍️ :orange[Item Name:] {item_name}")
            st.write(f" 💰 :orange[Item Price:] ${item_price:.2f}")
            st.write(f" 💹 :orange[Item Quantity:] {item_quantity}")
            st.write(f" 🅿️ :orange[Total:] ${total:.2f}")
            save_transaction(customer_name, item_name, item_price, item_quantity, total, "Ecocash")
            clear_form()
        
#__add a "Clear" button
        if st.button("Clear"):
            clear_form()   
            
def save_transaction(customer_name, item_name, item_price, item_quantity, total, payment_method):
    """Helper function to save transaction data to a CSV file"""
    transaction_data = {
        "Customer Name":[customer_name],
        "Item Name":[item_name],
        "Item Price":[item_price],
        "Item Quantity":[item_quantity],
        "Total":[total],
        "Payment Method":[payment_method]
        }
    #__create the dataframe
    df = pd.DataFrame(transaction_data)
    #st.dataframe(df)
     
    #__check if csv file exists
    if not os.path.exists("pos_system\dbs\pos_transactions.csv"):
        df.to_csv("pos_system\dbs\pos_transactions.csv", index = False)
    else:
        df.to_csv("pos_system\dbs\pos_transactions.csv", mode="a", index=False, header=not os.path.exists("pos_system\dbs\pos_transactions.csv"))
        st.success("Transaction Saved Succesfully!", icon ="🅿️")
        
def display_inventory():
    """Function to display inventory system"""
    #__read the csv file
    if os.path.exists("pos_system\dbs\pos_transactions.csv"):
        df = pd.read_csv("pos_system\dbs\pos_transactions.csv")
        
        #__group the data by item name and calculate the total quantity
        inventory_data = df.groupby("Item Name")["Item Quantity"].sum().reset_index()
        
        #__Display inventory information
        st.divider()
        st.title(":blue[**Inventory System**]")

        st.write(":blue[**Purchase dataframe**]")
        st.dataframe(inventory_data)
        
        #__create bar graph
        fig = go.Figure(data=[go.Bar(x=inventory_data["Item Name"], y=inventory_data["Item Quantity"])])
        fig.update_layout(
            title="Inventory Summary",
            xaxis_title="Product Name",
            yaxis_title="Total Quantity",
            )
        st.plotly_chart(fig, 
                        theme="streamlit",
                        use_container_width=True)
        st.divider()
            #__create pie chart
        inventory_by_item = inventory_data.groupby("Item Name")["Item Quantity"].sum().reset_index()
        fig_pie = px.pie(inventory_by_item, values="Item Quantity", names="Item Name", title="Pie chart analysis")
        st.plotly_chart(fig_pie,theme="streamlit", use_container_width=True)
    else:
        st.warning("No transaction data found. Please make some transactions first.")
    

def clear_form():
    """Helper function to clear the form fields"""
    st.session_state.customer_name = None
    st.session_state.item_name = None
    st.session_state.item_price = 0.0
    st.session_state.item_quantity = 1 

def footer():
     with st.sidebar:
          st.header(":blue[**Mthoe Saps Construction technologies. 2024**]")
          st.write("- :gray[**Welcome to POS system, Our Valued Customer**]")
          st.write("""
             - :gray[**Payment Designed by Mthokozisi Sapuwa and Saint Inc. With the purpose to support SMEs process Payments and payment data efficiently.**]
             """)
          st.divider()
          #footer
          st.divider()
          st.write(":gray[**Follow our company on social media**]")
          st.write(":gray[***Instagram page**]")
          st.write(":gray[***LinkeIn page**]")
     

          with st.container(border=True):
              st.write(":gray[**Report a bug**]")
              st.write("""- **Talk to our team of active developers if youre having trouble with the app**""")
              badge(type="github", name = "Crazypapi6" ,url="https://github.com/Crazypapi6")

          with st.container(border=True):
              st.write(":gray[**Donate to our cause**]")
              st.write("""- **10% of the women and children in the world go to be hungry, Its our vision to see them fed**""")
              st.markdown("""
              <a href="https://www.buymeacoffee.com/supremecro7"><img src="https://img.buymeacoffee.com/button-api/?text=Feed a soul&emoji=🐼&slug=supremecro7&button_colour=5F7FFF&font_colour=ffffff&font_family=Arial&outline_colour=000000&coffee_colour=FFDD00" /></a>
              """,
              unsafe_allow_html=True)
    
          
              st.write("- [Terms of sale](https://github.com/Crazypapi6)")
              st.write("- [Terms of use](https://github.com/Crazypapi6)")
         
              st.write("- [Privacy Statement](https://github.com/Crazypapi6)")
              st.write("- [Service Agreement](https://github.com/Crazypapi6)")
     
              st.write("- [Software License](https://github.com/Crazypapi6)")
              st.write("- [Trademarks](https://github.com/Crazypapi6)")    
            
if __name__ == "__main__":
    pos_system()
    

if __name__ == "__main__":
    display_inventory()

if __name__ == "__main__":
    footer()
