import streamlit as st 
import pandas as pd
import time
#import pdfplumber
#from escpos.printer import Usb

#__load the excel file
df = pd.read_excel("pos_system/dbs/kwaMondli_updated_pos_database.xlsx")

#__set the title of the app
st.title("KwaMondli POS System")

selected_item = st.selectbox("Select Item", df['item name'])

#__get the corresponding price and quantity
selected_price = df.loc[df["item name"] == selected_item, 'price'].values[0]
selected_quantity = st.number_input("Quantity", min_value=1, step=1)

#__calculate the total price
total_price = selected_price*selected_quantity

#__display total price
st.write(f"Item: {selected_item}")
st.write(f"Quantity: {selected_quantity}")
st.write(f"Total Price: ${total_price:.2f}")

#__save the purchase to the excel file and generate the receipt
if st.button("Save Purchase"):
    #__get the current timestamp
    purchase_time = time.strftime("%Y-%m-%d %H:%M:%S")

    #__update the existing row in the dataframe
    row_index = df.loc[df['item name'] == selected_item].index[0]
    df.at[row_index, 'quantity'] = selected_quantity
    df.at[row_index, 'total price'] = total_price
    df.at[row_index, 'purchase time'] = purchase_time

    # Save the updated DataFrame to the Excel file
    df.to_excel('pos_system/dbs/kwaMondli_updated_pos_database.xlsx', index=False)
    
    # Generate the receipt text
    receipt_text = f"""
    Receipt
    -------
    Item: {selected_item}
    Price: ${selected_price:.2f}
    Quantity: {selected_quantity}
    Total Price: ${total_price:.2f}
    Purchase Time: {purchase_time}
    """

    # Print the receipt using the receipt printer
   # try:
    #    p = Usb(0x0canc, 0x0your_model, 0)
    #   p.text(receipt_text)
     #   p.cut()
      #  st.success("Purchase saved to the Excel file and receipt printed.")
    #except Exception as e:
     #   st.error(f"Error printing receipt: {e}")

# Add a button to delete the last entry
if st.button("Delete Last Entry"):
    # Remove the last row from the DataFrame
    df = df.iloc[:-1]
    
    # Save the updated DataFrame to the Excel file
    df.to_excel('pos_system/dbs/kwaMondli_updated_pos_database.xlsx', index=False)
    st.success("Last entry deleted from the Excel file.")

# Add a button to delete the entire database
if st.button("Delete Entire Database"):
    # Create a new empty DataFrame
    df = pd.DataFrame(columns=['item name', 'price', 'quantity', 'total price', 'purchase time'])
    
    # Save the new DataFrame to the Excel file
    df.to_excel('pos_system/dbs/kwaMondli_updated_pos_database.xlsx', index=False)
    st.success("Entire database deleted from the Excel file.")        
