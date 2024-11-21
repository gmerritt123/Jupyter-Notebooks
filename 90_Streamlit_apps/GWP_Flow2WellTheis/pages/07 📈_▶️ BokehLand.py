# Loading the required Python libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.special
import streamlit as st
import streamlit_book as stb

import streamlit.components.v1 as components
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.embed import file_html

st.title('Building a bokeh app here')

st.subheader(':green-background[Just a basic bokeh app embedded into existing streamlit application]', divider="green")

st.markdown(""" 
            ### Some initial thoughts for the investigation
            This notebook illustrate the drawdown in a confined and an unconfined aquifer in response to pumping.
"""
)

src = ColumnDataSource(data={'x':list(range(-100,100,1)),'y':list(range(-100,100,1))})

f = figure(height=600,width=800,title='Example',sizing_mode='stretch_both')

r = f.line(x='x',y='y',source=src)
sl = Slider(value=1,step=1,start=0,end=4,width=800,title='exponent',sizing_mode='stretch_both')

cb = CustomJS(args=dict(sl=sl,src=src)
              ,code='''
              src.data['y'] = src.data['x'].map(x=>x**sl.value)
              src.change.emit()
              ''')
sl.js_on_change('value',cb)
lo = column([f,sl],sizing_mode='stretch_both')

bk_html = file_html(models=lo,resources='cdn')

components.html(bk_html,height=1000)



# Navigation at the bottom of the side - useful for mobile phone users     
        
columnsN1 = st.columns((1,1,1), gap = 'large')
with columnsN1[0]:
    if st.button("Previous page"):
        st.switch_page("pages/04_📈_▶️ Real Data Parameter Estimation.py")
with columnsN1[1]:
    st.subheader(':orange[**Navigation**]')
with columnsN1[2]:
    if st.button("Next page"):
        st.switch_page("pages/06_👉_About.py")
        
