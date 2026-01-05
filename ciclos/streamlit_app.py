import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# importar os dataframes
df_bp = pd.read_csv('data/business_performance.csv')
df_bp = df_bp.drop('Unnamed: 0', axis=1)
df_c = pd.read_csv('data/crossprice.csv')
df_e = pd.read_csv('data/df_elasticity.csv')


######### Layout Streamlit ##########
st.set_page_config(layout="wide")
st.header('Elasticidade de preços dos Produtos')

tab1, tab2, tab3 = st.tabs(['Elasticidade de Preços dos Produtos', 'Business Performance', 'Elasticidade Cruzada de Preços '])

with tab1:
    tab4, tab5 = st.tabs(['Elasticidade de Preços - Gráfico', 'Elasticidade de Preços - Dataframe'])
    
    with tab4:
        #apresentar elasticidade de preços graficamente
        st.header('Elasticidade de Preços - Gráfico')
        df_e['ranking'] = df_e.loc[ : ,'price_elasticity'].rank( ascending = True).astype(int)
        df_elasticity = df_e.reset_index(drop = True)
        fig, ax = plt.subplots()
        plt.figure(figsize = (12,4))
        ax.hlines(y = df_elasticity['ranking'] , xmin = 0, xmax = df_elasticity['price_elasticity'], alpha = 0.5, linewidth = 3)

        for name, p in zip(df_elasticity['name'], df_elasticity['ranking']):
            ax.text(4, p, name)

         #Add elasticity labels
        for x, y, s in zip(df_elasticity['price_elasticity'], df_elasticity['ranking'], df_elasticity['price_elasticity']):
            ax.text(x, y, round(s, 2), horizontalalignment='right' if x < 0 else 'left', 
                                        verticalalignment='center', 
                                        fontdict={'color':'red' if x < 0 else 'green', 'size':10})

        #ax.gca().set(ylabel= 'Ranking Number', xlabel= 'Price Elasticity')
        #ax.title('Price Elasticity' , fontdict={'size':13})
        ax.grid(linestyle='--')

        st.pyplot(fig)


    with tab5:
        #apresentar elasticidade de preços dataframe
        st.header('Elasticidade de Preços - Dataframe')
        df_order_elasticity = df_e[['ranking', 'name', 'price_elasticity']].sort_values(by='price_elasticity', ascending=False)
        st.dataframe(df_order_elasticity)

with tab2:
    # apresentar business performance
    st.header('Business Performance')
    df_bp = df_bp.set_index('name')
    st.dataframe(df_bp, use_container_width=True)
with tab3:
    # apresentar elasticidade cruzada de preços
    st.header('Elasticidade Cruzada de Preços')
    df_c = df_c.set_index('name')
    st.dataframe(df_c, use_container_width=True)






