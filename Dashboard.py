from pydoc import locate
import pandas as pd  
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Dashboard GIP", 
    page_icon=":bar_chart:", 
    layout="wide",
    initial_sidebar_state="expanded"
    )
    

#LOGO
from PIL import Image
image = Image.open('Logo2.PNG')

st.image(image, width=300)
   

#HOOFDPAGINA
st.title("Ratio analyse Packaging Donckers ")
st.subheader("Verschillende ratio's")
st.text('PACKAGING DONCKERS PRODUCEERT ONDERLEGGERS VOOR VOEDING VAN DE BESTE KWALITEIT.')
st.markdown("##")


#FOTO & VIDEO
col1, col2 = st.columns(2)

with col1:
    st.header("Foto")
    st.image("gebouw.jpg")

with col2:
    st.header("Video")
    st.video("PD.mp4")
    


#ZIJBALK
st.sidebar.header("Welke gegevens wilt u zien:")
boekjaar = st.sidebar.radio(
    "Kies een boekjaar:",
    ("Boekjaar 1","Boekjaar 2","Boekjaar 3"),
    index=0
)


#EXCEL LIQUIDITEIT 
def get_liq_from_excel():
    df = pd.read_excel(
        io="Analyse van de jaarrekening.xlsx",
        engine="openpyxl",
        sheet_name="Liquiditeit",
        usecols="A:D",
        nrows=32,
        header=1
    )
    
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    
    liq = ["Liquiditeit in ruime zin","Liquiditeit in enge zin"]
    df = df[df["Type"].isin(liq)]

#TRANSPONEREN
    df = df.T 
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","Liquiditeit in ruime zin","Liquiditeit in enge zin"] 
    
    
    return df

df_liq = get_liq_from_excel()

fig_liq = px.line(df_liq, x="Boekjaar", y=["Liquiditeit in ruime zin","Liquiditeit in enge zin"], color_discrete_sequence = ['light blue','black'], markers=True)
fig_liq.update_layout({
'plot_bgcolor': 'rgb(255, 255, 255)',
'paper_bgcolor': 'rgb(176, 224, 230)',})

fig_liq.update_traces(line=dict(width=6))
fig_liq.update_layout(title_text='Liquiditeit', title_x=0.5, yaxis_title = "Liquiditeit")
st.plotly_chart(fig_liq, use_container_width=True)

#EXCEL SOLVABILITEIT
def get_solv_from_excel():
    df = pd.read_excel(
        io="Analyse van de jaarrekening.xlsx",
        engine="openpyxl",
        sheet_name="Solvabiliteit",
        usecols="A:D",
        nrows=6,
        header=0
    )
    
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    
    solv = ["Solvabiliteit"]
    df = df[df["Type"].isin(solv)]

#TRANSPONEREN
    df = df.T 
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","Solvabiliteit"] 
    
    
    return df

df_solv = get_solv_from_excel()

fig_solv = px.line(df_solv, x="Boekjaar", y=["Solvabiliteit"], markers=True)
fig_solv.update_layout({'plot_bgcolor': 'rgb(255, 255, 255)',
'paper_bgcolor': 'rgb(176, 224, 230)',})

fig_solv.update_traces(line=dict(width=6))
fig_solv.update_layout(title_text='Solvabiliteit', title_x=0.5, yaxis_title = "Solvabiliteit")
st.plotly_chart(fig_solv, use_container_width=True)

#EXCEL RENTABILITEIT EV
def get_rev_from_excel():
    df = pd.read_excel(
        io="Analyse van de jaarrekening.xlsx",
        engine="openpyxl",
        sheet_name="REV",
        usecols="A:D",
        nrows=10,
        header=1
    )
    
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    
    rev = ["REV"]
    df = df[df["Type"].isin(rev)]

#TRANSPONEREN
    df = df.T 
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :]  
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","REV"] 
    
    
    return df

df_rev = get_rev_from_excel()

fig_rev = px.line(df_rev, x="Boekjaar", y=["REV"], markers=True)
fig_rev.update_layout({'plot_bgcolor': 'rgb(255, 255, 255)',
'paper_bgcolor': 'rgb(176, 224, 230)',})

fig_rev.update_traces(line=dict(width=6, color='black'))
fig_rev.update_layout(title_text='Rentabiliteit van het EV', title_x=0.5, yaxis_title = "Rentabiliteit EV")
st.plotly_chart(fig_rev, use_container_width=True)

#EXCEL VOORRAAD
def get_voorraad_from_excel():
    df = pd.read_excel(
        io="Analyse van de jaarrekening.xlsx",
        engine="openpyxl",
        sheet_name="Voorraad",
        usecols="A:D",
        nrows=6,
        header=0
    )
    
    df.columns = ["Type","Boekjaar 1","Boekjaar 2","Boekjaar 3"]
    
    voorraad = ["Omlooptijd"]
    df = df[df["Type"].isin(voorraad)]

#TRANSPONEREN
    df = df.T 
    df = df.rename(index={"Boekjaar 1":"1","Boekjaar 2":"2",
                    "Boekjaar 3":"3"})
    df = df.iloc[1: , :] 
    df.insert(0,"Boekjaar",["Boekjaar 1","Boekjaar 2",
                    "Boekjaar 3"],True)
    df.columns = ["Boekjaar","Voorraad"] 
    
    return df

df_voorraad = get_voorraad_from_excel()

fig_voorraad = px.bar(df_voorraad, x="Boekjaar", y="Voorraad")
fig_voorraad.update_layout({'plot_bgcolor': 'rgb(255, 255, 255)',
'paper_bgcolor': 'rgb(176, 224, 230)',})

fig_voorraad.update_traces(width=0.30)
fig_voorraad.update_layout(title_text='Omlooptijden van de voorraad', title_x=0.5)
st.plotly_chart(fig_voorraad, use_container_width=True)

#HIDE STREAMLIT STYLE
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#EXCEL ACTIVA
@st.cache
def get_activa_from_excel():
    df = pd.read_excel(
        io="Analyse van de jaarrekening.xlsx",
        engine="openpyxl",
        sheet_name="verticale analyse balans",
        usecols="A:E",
        nrows=102,
        header=2
    )

    
    activa = ["VASTE ACTIVA","VLOTTENDE ACTIVA"]
    df = df[df['ACTIVA'].isin(activa)]

    return df

df_activa = get_activa_from_excel()

# overzicht activa boekjaar 
fig_activa = px.pie(df_activa, 
            values=boekjaar, 
            names='ACTIVA',
            title=f'Overzicht activa {boekjaar}',
            color_discrete_sequence=px.colors.sequential.Jet)

fig_activa.update_traces(textfont_size=15, pull=[0, 0], marker=dict(line=dict(color='blue', width=3)))
fig_activa.update_layout(legend = dict(font = dict(size = 10),yanchor= "bottom", y=-0.30, xanchor= "left", x=0.01), title = dict(font = dict(size = 25)))
fig_activa.update_layout({
'plot_bgcolor': 'rgb(255, 255, 255)',
'paper_bgcolor': 'rgb(176, 224, 230)',})

#EXCEL PASIVA
@st.cache
def get_passiva_from_excel():
    df = pd.read_excel(
        io="Analyse van de jaarrekening.xlsx",
        engine="openpyxl",
        sheet_name="verticale analyse balans",
        usecols="A:E",
        nrows=102,
        header=50
    )

    
    passiva = ["EIGEN VERMOGEN","VOORZIENINGEN EN UITGESTELDE BELASTINGEN","SCHULDEN"]
    df = df[df['PASSIVA'].isin(passiva)]

    return df

df_passiva = get_passiva_from_excel()

# overzicht pasiva boekjaar 
fig_passiva = px.pie(df_passiva, 
            values=boekjaar, 
            names='PASSIVA',
            title= f' Overzicht passiva {boekjaar}', 
            color_discrete_sequence=px.colors.sequential.Jet)           
            
fig_passiva.update_traces(textfont_size=15, pull=[0, 0], marker=dict(line=dict(color='blue', width=3)))
fig_passiva.update_layout(legend=dict(font = dict(size = 10),yanchor= "bottom", y=-0.30, xanchor= "left", x=0.01), title = dict(font = dict(size = 25)))
fig_passiva.update_layout({
'plot_bgcolor': 'rgb(255, 255, 255)',
'paper_bgcolor': 'rgb(176, 224, 230)',})

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_activa, use_container_width=True)
right_column.plotly_chart(fig_passiva, use_container_width=True)