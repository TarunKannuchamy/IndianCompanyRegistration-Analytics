import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import altair as alt
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(layout="wide")
st.markdown('<style>body { font-size: 72px; }</style>', unsafe_allow_html=True)
st.title("Companies registered since 1857")

#Query 1
st.write("1. Based on the sector display the number of companies")
df = pd.read_csv("query_1.csv")
x_column = 'company_class'  
y_column = 'count'  
tab2, tab1 = st.tabs(["Graph", "data"])
with tab1:
    st.dataframe(df,use_container_width=True)
with tab2:
    chart_data = df[[x_column, y_column]]
    chart_data.set_index(x_column, inplace=True)
    st.bar_chart(chart_data, height=600)

#Query 2
st.write("2. list the number of companies that had been registered in each decade")
tab2, tab1 = st.tabs(["Graph", "data"])
df = pd.read_csv("query_2.csv")
x_column = 'decade'  
y_column = 'no_of_companies'  
with tab1:
    st.dataframe(df,use_container_width=True)
with tab2:
    chart_data = df[[x_column, y_column]]
    chart_data.set_index(x_column, inplace=True)
    st.bar_chart(chart_data, height=600)

#Query 3
st.write("3. Find top 5 companies with highest paid up capital as a list in each leap year after 2000")
tab2, tab1 = st.tabs(["Graph", "data"])
data = pd.read_csv('query_3.csv')
columns = ["company_name","paidup_capital","year","rank"]
with tab1:
    st.dataframe(data,use_container_width=True)
with tab2:
    # c = alt.Chart(data).mark_circle().encode(
    #     x=alt.X('company_name', scale=alt.Scale(zero=False)), y='paidup_capital', 
    #     size='rank', color='year', 
    #     tooltip=["company_name","paidup_capital","year"]).properties(height=600)

    # st.altair_chart(c, use_container_width=True)
    # data = data.orderBy("company_name")
    fig = px.line(data, x="company_name", y="paidup_capital", animation_frame = "year", height = 500)
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        xaxis = dict(showgrid = False),
        yaxis = dict(showgrid = False)
    )
    st.plotly_chart(fig, use_container_width=True)

#Query 4
st.write("4. Find top 5 companies that has highest paid up capital in each state.")
data = pd.read_csv('query_4.csv')
states = data['registered_state'].unique()

selected_state = st.selectbox("Select the state", states, key = "state_select")

for state in states:
        if state == selected_state:
            df1 = data.loc[data['registered_state'] == f"{state}"]
            tab2, tab1 = st.tabs(["Graph", "data"])
            with tab1:
                st.dataframe(df1, use_container_width= True)
            with tab2:
                x_column = 'company_name'  
                y_column = 'paidup_capital'  
                chart_data = df1[[x_column, y_column]]
                chart_data.set_index(x_column, inplace=True)
                st.bar_chart(chart_data, height=600)

# columns = ["company_name","paidup_capital","registered_state","rank"]
# with tab1:
#     st.dataframe(data,use_container_width=True)
# with tab2:
#     # Convert data to Altair DataFrame
#     alt_data = alt.Data(values=data)
#     legend_selection = alt.selection_multi(fields=['registered_state'], bind='legend')
#     c = alt.Chart(alt_data).mark_circle().encode(
#         # column=alt.Column('company_name'),
#         x=alt.X('company_name', scale=alt.Scale(zero=True), axis = None), y='paidup_capital', 
#         size='rank',     color=alt.condition(
#         legend_selection,
#         alt.Color('registered_state', legend=None),
#         alt.value('lightgray')),tooltip=["company_name", "paidup_capital", "registered_state"]
#         ).properties(height=600).add_selection(legend_selection)

#     st.altair_chart(c, use_container_width=True)

#Query 5
st.write("5. Which state has highest companies registered")
tab2, tab1 = st.tabs(["Graph", "data"])
df = pd.read_csv("query_5.csv")
x_column = 'registered_state'  
y_column = 'num_of_companies'  
with tab1:
    st.dataframe(df,use_container_width=True)
with tab2:
    chart_data = df[[x_column, y_column]]
    chart_data.set_index(x_column, inplace=True)
    st.bar_chart(chart_data, height=600)
    max_state = df.loc[df['num_of_companies'].idxmax(), 'registered_state']
    st.write("State with the highest number of registered companies : ", max_state)

#query 6
st.write("6. Find the year on which each state has their maximum registration")
tab2, tab1 = st.tabs(["Graph", "data"])
data = pd.read_csv('query_6.csv')
columns = ["no_of_companies","registered_state","year"]
with tab1:
    st.dataframe(data,use_container_width=True)
with tab2:
    c = alt.Chart(data).mark_circle().encode(
        x=alt.X('year', scale=alt.Scale(zero=False)), y='no_of_companies', 
        size='registered_state', color='registered_state', 
        tooltip=['no_of_companies', 'registered_state', 'year']).properties(height=600)

    st.altair_chart(c, use_container_width=True)

#Query 7 
st.write("7. Find the sector that is most common in each state")
# tab2, tab1 = st.tabs(["Graph", "data"])
data = pd.read_csv('query_7_2.csv')
states = data['registered_state'].unique()

selected_state = st.selectbox("Select the state", states)

for state in states:
        if state == selected_state:
            df1 = data.loc[data['registered_state'] == f"{state}"]
            most_common = df1.loc[df1['no_of_companies'].idxmax(), 'company_class']
            st.write(f'As seen below in {state}, the most common sector is {most_common}')
            tab2, tab1 = st.tabs(["Graph", "data"])
            with tab1:
                st.dataframe(df1, use_container_width= True)
            with tab2:
                labels = df1['company_class'].tolist()
                values = df1['no_of_companies'].tolist()
                fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
                most_common = df1.loc[df1['no_of_companies'].idxmax(), 'company_class']
                st.plotly_chart(fig, use_container_width=True, style={'display': 'block', 'margin': 'auto'})            # # Create the figure and axes for the pie chart


#Query 8
st.write("8. Based on sub_category give the count for companies in each state")
tab2, tab1 = st.tabs(["Graph", "data"])
data = pd.read_csv('query_8.csv')
columns = ["registered_state","no_of_companies","company_sub_category"]
with tab1:
    st.dataframe(data,use_container_width=True)
with tab2:
    # c = alt.Chart(data).mark_circle().encode(
    #     x=alt.X('registered_state', scale=alt.Scale(zero=False)), y='no_of_companies',color='company_sub_category', 
    #     tooltip=["registered_state","registered_state","company_sub_category"]).properties(height=600)

    # st.altair_chart(c, use_container_width=True)
    # categories = data['registered_state'].tolist()
    # values = data['no_of_companies'].tolist()
    # colors = px.colors.qualitative.Plotly[:len("company_sub_category")]

    fig = px.bar(data, x='registered_state', y='no_of_companies', color='company_sub_category', height = 700, width = 1500)
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        xaxis = dict(showgrid = False),
        yaxis = dict(showgrid = False)
    )
    st.plotly_chart(fig)

#Query 9
st.write("9. list the companies that have been recently enrolled in each state")
data = pd.read_csv('query_9_2.csv')
# columns = ["decade","paidup_capital","company_name"]
states = data['registered_state'].unique()

selected_state = st.selectbox("Select the state", states)

for state in states:
        if state == selected_state:
            st.write(f"This is the content for {state}")
            df1 = data.loc[data['registered_state'] == f"{state}"]
            tab1, tab2 = st.tabs(["Data", "Graph"])
            with tab1:
                st.dataframe(df1,use_container_width=True)            
            with tab2:
                c = alt.Chart(df1).mark_circle().encode(
                    x=alt.X('company_name', scale=alt.Scale(zero=False)), y='date', color='company_name', 
                    tooltip=["date","company_name"]).properties(height=600)
                st.altair_chart(c, use_container_width=True)

#Query 10
st.write("10. Find the count of companies per company_status")
tab2, tab1 = st.tabs(["Graph", "data"])
df = pd.read_csv("query_10.csv")
x_column = 'company_status'  
y_column = 'no_of_companies'  
with tab1:
    st.dataframe(df,use_container_width=True)
with tab2:
    chart_data = df[[x_column, y_column]]
    chart_data.set_index(x_column, inplace=True)
    st.bar_chart(chart_data, height=600)

#Query 11
st.write("11. Find the top 2 companies per principal business activity in 19th century")
tab2, tab1 = st.tabs(["Graph", "data"])
data = pd.read_csv('query_11.csv')
columns = ["PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN","paidup_capital","company_name","rank"]
with tab1:
    st.dataframe(data,use_container_width=True)
with tab2:
    # chart = alt.Chart(data, title='Top 2 Companies per Principal Business Activity in the 19th Century').mark_bar(
    #     opacity=1
    # ).encode(
    #     # column=alt.Column('PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN:N', spacing=0.1, header=alt.Header(labelOrient="bottom")),
    #     x=alt.X('PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN:N'),
    #     y=alt.Y('paidup_capital:Q'),
    #     color=alt.Color('company_name:N')
    # ).configure_view(stroke='transparent').properties(height=600)

    # # Display the chart in Streamlit
    # st.altair_chart(chart, use_container_width=True)
    fig = px.bar(data, x='PRINCIPAL_BUSINESS_ACTIVITY_AS_PER_CIN', y='paidup_capital', color='company_name', height = 700, barmode  = "overlay")
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        xaxis = dict(showgrid = False),
        yaxis = dict(showgrid = False)
    )
    st.plotly_chart(fig, use_container_width = True)


#Query 12
st.write("12. Find the company with higest paidup capital in each decade")
tab2, tab1 = st.tabs(["Graph", "data"])
data = pd.read_csv('query_12.csv')
columns = ["decade","paidup_capital","company_name"]
with tab1:
    st.dataframe(data,use_container_width=True)
with tab2:
    import plotly.express as px
    columns = ["decade","paidup_capital","company_name"]
    fig = px.scatter(data, x="company_name", y="decade", color = "paidup_capital", height = 700)
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        xaxis = dict(showgrid = False),
        yaxis = dict(showgrid = False)
    )
    st.plotly_chart(fig, use_container_width = True)

#     c = alt.Chart(data).mark_point().encode(
#         x=alt.X('company_name', scale=alt.Scale(zero=False)), y='paidup_capital', size = alt.value(200), color='decade', 
#         tooltip=["decade","paidup_capital","company_name"]).properties(height=600).configure_mark(
#     filled=True,
#     color='blue'
# ).configure_axis(
#     labelFontSize=12,
#     titleFontSize=14
# )


#     st.altair_chart(c, use_container_width=True)

