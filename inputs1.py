import streamlit as st
import numpy as np
import plotly.express as pe
st.title("Income tax Department")
name=st.text_input("Enter your name")
val=st.number_input("Enter your annual Income")
tax=0
if st.button("Calc"):
    if val<500000:
        tax=0
    elif val<750000:
        tax=val*5/100
    else:
        tax=val*10/100
    st.write(f"Tax to be paid is Rs. {tax}")

st.title("Graph Generator")
s=st.number_input("Enter starting range",format="%d",value=0)
e=st.number_input("Enter ending range",format="%d",value=0)
x=np.linspace(s,e,300)

choose=st.selectbox("Select type of graph",["power","trignometry"])
if choose=="power":
    y1=st.number_input("Enter exponent",format="%d",value=0)
    y=x**y1;
else:
    choose1=st.selectbox("Select type of graph",["Sin","Cos","Tan"])
    if choose1=="Sin":
        y=np.sin(x)
    elif choose1=="Cos":
        y=np.cos(x)
    else:
        y=np.tan(x)
if st.button("plot"):
    st.plotly_chart(pe.line(x=x,y=y,title=f"y"))
    
