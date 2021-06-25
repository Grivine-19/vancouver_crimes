import streamlit as st
import os


def save_uploadedfile(uploadedfile):
    with open(os.path.join("data", uploadedfile.name), "wb") as f:
         f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to data".format(uploadedfile.name))


def app():
    datafile = st.file_uploader("Upload CSV",type=['csv'])
    if datafile is not None:
        file_details = {"FileName":datafile.name,"FileType":datafile.type}
        st.write(file_details)
        save_uploadedfile(datafile)
