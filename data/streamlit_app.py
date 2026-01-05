# bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import streamlit as st

#import datasets
df_elasticity_laptop = pd.read_csv('../data/finals/elasticidade_laptop.csv')

df_bp = pd.read_csv('../data/finals/business_performance.csv')
df_bp = df_bp.drop(columns={'Unnamed: 0'})

df_cpe = pd.read_csv('../data/finals/result_CPE.csv')


############################# Layout Streamlit ###################################
st.set_page_config(layout="wide")
st.header('Elasticidade de Preços dos Produtos')

tab1, tab2, tab3 = st.tabs(['Elasticidade de Preços dos Produtos', 'Business Performance', 'Elasticidade Cruzada de Preços'])

with tab1:
    tab5, tab6 = st.tabs(['Elasticidade de Preços dos Produtos - Gráfico', 'Elasticidade de Preços dos Produtos - Tabela'])
    with tab5:
        st.subheader('Elasticidade de Preços dos Produtos - Gráfico')

        df_elasticity_laptop['ranking'] = df_elasticity_laptop.loc[ : ,'price_elasticity'].rank( ascending = True).astype(int)
        df_elasticity_laptop = df_elasticity_laptop.reset_index(drop = True)
        fig, ax = plt.subplots()
        plt.figure(figsize = (12,4))
        ax.hlines(y = df_elasticity_laptop['ranking'] , xmin = 0, xmax = df_elasticity_laptop['price_elasticity'], alpha = 0.5, linewidth = 3)

        for name, p in zip(df_elasticity_laptop['name'], df_elasticity_laptop['ranking']):
            ax.text(4, p, name)

        for x, y, s in zip(df_elasticity_laptop['price_elasticity'], df_elasticity_laptop['ranking'], df_elasticity_laptop['price_elasticity']):
            ax.text(x, y, round(s, 2), horizontalalignment='right' if x < 0 else 'left', 
                     verticalalignment='center', fontdict={'color':'red' if x < 0 else 'green', 'size':10})

        #ax.gca().set(ylabel= 'Ranking Number', xlabel= 'Price Elasticity')
        #ax.title('Price Elasticity' , fontdict={'size':13})
        ax.grid(linestyle='--')
        st.pyplot(fig)

    with tab6:
        st.subheader('Elasticidade de Preços dos Produtos - Tabela')   
        df_order_laptop = df_elasticity_laptop[['ranking', 'name', 'price_elasticity']].sort_values(by='price_elasticity', ascending=False)
        df_order_laptop = df_order_laptop.set_index('name')
        st.dataframe(df_order_laptop)

with tab2:
    # apresentar a business performance
    st.subheader('Business Performance')
    df_bp = df_bp.set_index('name')
    st.dataframe(df_bp, use_container_width=True)
    
with tab3:
    # apresentar a elasticidade cruzada
    st.subheader('Elasticidade Cruzada de Preços')
    df_cpe = df_cpe.set_index('name')
    st.dataframe(df_cpe, use_container_width=True)
