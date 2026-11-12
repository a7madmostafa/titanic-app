import streamlit as st
from utils.data import load_data
from utils.figures import plot_family_size, plot_outcome, plot_heatmap


st.set_page_config(layout="wide")

# Load data
df = load_data()

# Filters
with st.sidebar:
    classes = st.multiselect("Select classes", df["class"].unique(), default=df["class"].unique())
    gender = st.radio("Select gender", list(df['sex'].unique()) + ["All"], horizontal=True)
    age = st.slider("Age", 0, 80, (0, 80))
    
    st.write(f"Made by [**Ahmad Mostafa**](https:/www.linkedin.com/in/ahmadmostafa/)")
if gender == "All":
    data = df[df["class"].isin(classes) & df["age"].between(*age)]
else:   
    data = df[(df["class"].isin(classes)) & (df["sex"] == gender) & df["age"].between(*age)]

st.session_state.data = data


# Pages
pages = [
    st.Page("views/overview.py", title="Overview", icon=":material/dashboard:", default=True),
    st.Page("views/conclusion.py", title="Conclusion", icon=":material/table:"),
]
st.navigation(pages, position="top").run()