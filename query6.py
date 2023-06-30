import streamlit as st
import pandas as pd
import aiohttp
import asyncio
from geopy.geocoders import Nominatim
from geopy.adapters import AioHTTPAdapter
import numpy as np
import plotly.express as px
st.set_page_config(layout="wide")


df = pd.read_csv('query_6.csv')
st.dataframe(df, use_container_width=True)
DF2 = df['registered_state'].unique()
df2 = pd.DataFrame(DF2)
df2.to_csv("states", index = False)
st.dataframe(df2)
df4 = pd.read_csv('states.csv')
df3 = pd.merge(df, df4, on='registered_state', how='inner')
st.dataframe(df3)

fig = px.scatter_geo(data_frame=df3, lat='Latitude', lon='Longitude', scope = 'asia', hover_name='registered_state', color = 'year', size='no_of_companies',height = 1200)
fig.update_layout(
    autosize=False,
    width=1000,
    height=600
)
st.plotly_chart(fig, use_container_width=True, style={'display': 'block', 'margin': 'auto'})          

# # Create a custom user_agent for the geocoder
# custom_user_agent = "specify_your_app_name_here"

# # Set the proxies for aiohttp session
# proxies = None  # Set to None if you don't need proxies

# # Create an aiohttp session with the necessary configurations
# connector = aiohttp.TCPConnector(ssl=False, proxies=proxies)  # Set ssl=False for skipping SSL verification
# session = aiohttp.ClientSession(connector=connector)

# # Create a geocoder instance with the custom user_agent and aiohttp session
# geolocator = Nominatim(user_agent=custom_user_agent, adapter_factory=AioHTTPAdapter, session=session)

# # Define an async function to geocode a location
# async def geocode_location(location):
#     try:
#         # Use geocoder to get the latitude and longitude of the location
#         geocode = await geolocator.geocode(location)
#         if geocode is not None:
#             return geocode.latitude, geocode.longitude
#         else:
#             return None, None
#     except:
#         return None, None

# # Apply the geocoding function to the 'registered_state' column of the dataframe
# async def geocode_dataframe(df):
#     geocoded_data = []
#     for loc in df['registered_state']:
#         result = await geocode_location(loc)
#         geocoded_data.append(result)
#     return geocoded_data

# geocoded_data = asyncio.run(geocode_dataframe(df))
# df['Latitude'], df['Longitude'] = zip(*geocoded_data)

# # Display the updated dataframe
# st.dataframe(df, use_container_width=True)
