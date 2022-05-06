import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Ratio analyse packaging Donckers', anchor=None)

st.subheader("Verschillende ratio's", anchor=None)

st.subheader('Liquiditeit', anchor=None)
liq = pd.read_excel(
    io='Analyse van de jaarrekening.xlsx',
    engine="openpyxl",
    sheet_name='Liquiditeit', 
    usecols='A:D',
    nrows=100, skiprows=1)

liq.columns= ["type","Boekjaar 1","Boekjaar 2", "Boekjaar 3"]
type= ['Liquiditeit in ruime zin','Liquiditeit in enge zin']
liq= liq[liq['type'].isin(type)]

st.write(liq)
st.line_chart(liq, x="Boekjaar", y=["Liquiditeit"], markers=True)
fig.update_traces(line=dict(width=3))
st.plotly_chart(fig, use_container_width=True)

st.subheader('Solvabiliteit', anchor=None)
sol = pd.read_excel(
    io='Analyse van de jaarrekening.xlsx',
    engine="openpyxl",
    sheet_name='Solvabiliteit', 
    usecols='A:D',
    nrows=100)

sol.columns= ["type","Boekjaar 1","Boekjaar 2", "Boekjaar 3"]
type= ['Solvabiliteit']
sol= sol[sol['type'].isin(type)]

st.write(sol)
st.line_chart(sol)

st.subheader('REV', anchor=None)
rev = pd.read_excel(
    io='Analyse van de jaarrekening.xlsx',
    engine="openpyxl",
    sheet_name='REV', 
    usecols='A:D',
    nrows=100, skiprows=1)

rev.columns= ["type","Boekjaar 1","Boekjaar 2", "Boekjaar 3"]
type= ['REV']
rev= rev[rev['type'].isin(type)]

st.write(rev)
st.line_chart(rev)


st.subheader('Omloopsnelheid voorraad', anchor=None)
vrr = pd.read_excel(
    io='Analyse van de jaarrekening.xlsx',
    engine="openpyxl",
    sheet_name='Liquiditeit', 
    usecols='A:D',
    nrows=100, skiprows=1)

vrr.columns= ["type","Boekjaar 1","Boekjaar 2", "Boekjaar 3"]
type= ['Omlooptijd','Omloopsnelheid voorraden']
vrr= vrr[vrr['type'].isin(type)]

st.write(vrr)
st.line_chart(vrr)