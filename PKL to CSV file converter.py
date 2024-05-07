# PKL to CSV file converter

import streamlit as st
import pickle as pkl
import pandas as pd
import base64

# Load the data from the pickle file
@st.cache
def load_data(file_path):
    with open(file_path, "rb") as f:
        obj = pkl.load(f)
    return obj

# Main Streamlit app
def main():
    st.title("Download CSV File")
    
    # Load the data
    obj = load_data("Your file.pkl")
    
    # Convert data to DataFrame
    df = pd.DataFrame(obj)
    
    # Save DataFrame to CSV
    csv_file = df.to_csv(index=False)
    
    # Download link generation
    b64 = base64.b64encode(csv_file.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="file.csv">Click here to download the CSV file</a>'
    
    # Display download link
    st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
