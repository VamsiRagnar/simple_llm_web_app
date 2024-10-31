import streamlit as st
import helpers

st.title('Player Name Generator')

nationality = st.sidebar.text_input("Enter the nationality")
sport = st.sidebar.text_input("Enter the sport")
year = st.sidebar.text_input("Enter the year")


if year and sport and nationality:
    response = helpers.generate_player_names(year, sport, nationality)
    player_names = response['player_names'].strip().split(",")
    st.write("** Team Player Names **")

    for name in player_names:
        st.write("--", name)