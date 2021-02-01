"""
Module to pull players raw games data from https://www.basketball-reference.com

Test url - 'https://www.basketball-reference.com/players/h/hardeja01/gamelog/2011/'
"""
import pandas as pd
import requests
import bs4

def getPlayerData(player_first_name, player_last_name,years):
    """
    Go to basketball reference and pull player's game data

    player_first_name: str
    player_last_name: str
    years: list (int)
    """
    page = 'https://www.basketball-reference.com/players/h/'

    # grab HTML table from webpage TODO: add in asserts where player not found / iterate up a few digits to
    # check if player is found
    page = page + f'{player_last_name[0:5].lower()}{player_first_name[0:2].lower()}01/gamelog/{years}'

    tables = pd.read_html(page)

    # Subsets to the games table in the HTML
    df_games = [
            table for table in tables if table.shape[0] > 30
    ][0]
    
    return df_games

player_first_name = 'Ben'
player_last_name = 'Simmons'
getPlayerData(player_first_name,player_last_name,2020)