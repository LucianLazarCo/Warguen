import streamlit

streamlit.title('My Parents New Healty Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 2 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smootie')
streamlit.text('🐔 Hard-Boiled Freee-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruiy_list)
