import streamlit as st
import pandas as pd
from datetime import datetime

def calculate_gas_sold(amount_paid):
    gas_price = 2.00  # $2 per 1kg of gas
    gas_sold = amount_paid / gas_price
    return gas_sold

def save_to_excel(amount_paid, gas_sold):
    # Load the existing Excel file
    try:
        df = pd.read_excel('pos_system/dbs/t1gases_dbs.xlsx')
    except (FileNotFoundError, pd.errors.EmptyDataError):
        # If the file doesn't exist or is empty, create a new DataFrame
        df = pd.DataFrame(columns=['amount sold', 'kgs gas sold', 'gas price', 'time stamp'])

    # Create a new row with the current data
    new_row = {
        'amount sold': amount_paid,
        'kgs gas sold': gas_sold,
        'gas price': 2.00,
        'time stamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    # Append the new row to the DataFrame
    df.loc[len(df)] = new_row

    # Save the updated DataFrame to the Excel file
    df.to_excel('pos_system/dbs/t1gases_dbs.xlsx', index=False)

def delete_last_entry():
    # Load the existing Excel file
    try:
        df = pd.read_excel('pos_system/dbs/t1gases_dbs.xlsx')
    except (FileNotFoundError, pd.errors.EmptyDataError):
        # If the file doesn't exist or is empty, do nothing
        return

    # Drop the last row
    df = df.iloc[:-1]

    # Save the updated DataFrame to the Excel file
    df.to_excel('pos_system/dbs/t1gases_dbs.xlsx', index=False)

def reset_database():
    # Create a new empty DataFrame
    df = pd.DataFrame(columns=['amount sold', 'kgs gas sold', 'gas price', 'time stamp'])

    # Save the empty DataFrame to the Excel file
    df.to_excel('pos_system/dbs/t1gases_dbs.xlsx', index=False)

def main():
    st.title("Gas Selling App")
    st.write("Price: $2.00 per 1kg of gas")

    # Load the existing Excel file
    try:
        df = pd.read_excel('pos_system/dbs/t1gases_dbs.xlsx')
    except (FileNotFoundError, pd.errors.EmptyDataError):
        # If the file doesn't exist or is empty, create a new DataFrame
        df = pd.DataFrame(columns=['amount sold', 'kgs gas sold', 'gas price', 'time stamp'])

    # Calculate the totals
    total_gas_sold = df['kgs gas sold'].sum()
    total_sales = df['amount sold'].sum()

    # Display the totals in Streamlit metric cards
    st.metric(label="Total Gas Sold (kg)", value=f"{total_gas_sold:.2f}")
    st.metric(label="Total Sales ($)", value=f"{total_sales:.2f}")

    amount_paid = st.number_input("Enter the amount paid (in $):", min_value=0.0, step=0.01)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Enter Payment"):
            gas_sold = calculate_gas_sold(amount_paid)
            save_to_excel(amount_paid, gas_sold)
            st.write(f"You bought {gas_sold:.2f} kg of gas.")
 
        # Calculate the totals
        #total_gas_sold = df['kgs gas sold'].sum()
        #total_sales = df['amount sold'].sum() 
        #st.metric(label="Total Gas Sold (kg)", value=f"{total_gas_sold:.2f}")

        #save_to_excel(amount_paid, gas_sold)
            #st.write("Data saved to 'c:/Users/mthoe/OneDrive/Desktop/t1gases_dbs.xlsx'.")
    with col2:
        if st.button("Delete Last Entry"):
            delete_last_entry()
            st.write("Last entry deleted from the database.")
    with col3:
        if st.button("Reset Database"):
           reset_database()
           st.write("Database has been reset.")

if __name__ == "__main__":
    main()