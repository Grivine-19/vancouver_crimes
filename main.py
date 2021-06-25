from multiapp import MultiApp
from apps import home, data, charts
import streamlit.components.v1 as stc
import streamlit as st

#Title for the page
HTML_BANNER = """
<div style="background-color:#b85212;padding:10px;border-radius:10px">
<h1 style="color:white;text-align:center;">Crime In Vancouver, Canada</h1>
</div>
    """
stc.html(HTML_BANNER)

st.sidebar.image(
    'https://www.macleans.ca/wp-content/uploads/2011/12/Crime_Vancouver_slide.jpg', width=300)

app = MultiApp()

#Adding all the applications here

app.add_app("Home", home.app)
app.add_app("Dataset", data.app)
app.add_app("Charts", charts.app)

#The main app
app.run()
