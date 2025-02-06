import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def main():
    st.title("This is the app for ecom i am creating")
    st.sidebar.title("you can uplaod your file here")

    upload_file = st.sidebar.file_uploader("uplaod your file",type =['csv','xlsx'])

    if upload_file is not None :
        try :
            if upload_file.name.endswith('csv'):
                data = pd.read_csv(upload_file)
            else :
                data = pd.read_excel(upload_file)
            st.sidebar.success("file uploaded successfully")

            st.subheader("I am going to show you a date details")
            st.dataframe(data.head())
            st.dataframe(data.tail())
            st.subheader("lets see some more details in date")
            st.write("shape of the data",data.shape)
            st.write("cloumn name inside in data is",data.columns)
            st.write("missing value into column", data.isnull().sum())

            st.subheader("i will show you the bit of stats")
            st.write(data.describe())

            
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()

