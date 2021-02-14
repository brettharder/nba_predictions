"""
Module to pull players raw games data from https://www.basketball-reference.com

Test url - 'https://www.basketball-reference.com/players/h/hardeja01/gamelog/2011/'
"""
import pandas as pd
import requests
import bs4

import logging
logging.basicConfig(level = logging.INFO)
logger = logging.getLogger('player scrape')

def getPlayerData(player_first_name, player_last_name,years):
    """
    Go to basketball reference and pull player's game data

    player_first_name: str
    player_last_name: str
    years: list (int)
    """
    # grab HTML table from webpage TODO: add in asserts where player not found
    # or iterate up a few digits to check if player is found

    # list of game dataframes each year
    l_games = []

    for year in years:
        page = 'https://www.basketball-reference.com/players/h/'
        page = page + f'{player_last_name[0:5].lower()}'\
            f'{player_first_name[0:2].lower()}01/gamelog/{year}'
        #print(page)

        try:
            tables = pd.read_html(page)
            logger.info(
                f'Parsed data for {year}'
            )
            #print('worked!')

            # Subsets to the games table in the HTML
            df_games = [
                    table for table in tables if table.shape[0] > 30
            ][0]

            l_games.append(df_games)

        except:
            logger.info(f'hmm unable to get data for {player_first_name} {player_last_name} in {year}')
            #print(f'hmm unable to get data for {player_first_name} {player_last_name} in {year}')
            pass

    if len(l_games) > 0:
        df_seasons = pd.concat(l_games,ignore_index=True)
        
        # Drop rows where the HTML parser keeps column names as records
        df_seasons = df_seasons[df_seasons['Rk'] != 'Rk']
        
        return df_seasons
    
    else:
        logger.info('No data found please double check input player names and years')
        #print('No data found please double check input player names and years')

# Example
# player_first_name = 'Ben'
# player_last_name = 'Simmons'
# df_games = getPlayerData(player_first_name,player_last_name,[2020])
# df_games.head(50)