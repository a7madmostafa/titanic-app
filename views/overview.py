import streamlit as st
from utils.figures import plot_family_size, plot_outcome, plot_heatmap

data = st.session_state.data
st.set_page_config(layout="wide")

# Header
st.markdown("<h1 style='text-align: center;'>Titanic Survival Prediction App</h1>",
            unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Data from "
            "<a href='https://www.kaggle.com/c/titanic/data'>https://www.kaggle.com/c/titanic/data</a></p>",
            unsafe_allow_html=True)

left, mid, right = st.columns([1, 3, 1])
with mid:
    st.image("utils/titanic.jpg", use_container_width=True)
    
show_data = st.checkbox("Show sample data")
if show_data:
    st.dataframe(df.head(10), hide_index=True)

# Metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Passengers", len(data), border=True)
col2.metric("Survival rate", f"{data['survived'].mean():.0%}", border=True)
col3.metric("Median age", f"{data['age'].median():.0f}", border=True)
col4.metric("Median fare", f"£{data['fare'].median():.2f}", border=True)

# Plots
tab1, tab2 = st.tabs(["Heatmap", "Family size vs outcome"])
with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.plotly_chart(plot_family_size(data))

    with c2:
        st.plotly_chart(plot_outcome(data))

with tab2:
    st.plotly_chart(plot_heatmap(data))
   
