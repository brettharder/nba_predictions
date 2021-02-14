"""
Runner for making nba predictions for a player TODO: This will be the main runner for the project

Modes:
  1. parse_data: will pull player data over specified years (seasons) and save to a local dir
  2. feature_engineer: given output of `parse_data` will build a table that can be input into 
     a model 
  3. train_model: will run a pipeline to train a model predicting points per game 
  4. predict: given a model and opponent, will make a prediction of points per game 
""" 
import argparse
import logging
import sys
import os
import pandas as pd
import requests
import bs4

from nba_predictions.player_scrape import getPlayerData

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger('nba_predictions')

def parse_args(args):
    """
    Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    parser_desc = (
        'NBA Predictions - train a model to predict how many points a player will score in the next NBA game'
    )

    parser = argparse.ArgumentParser(description=parser_desc)
    subparsers = parser.add_subparsers(help='sub-command help', dest='command')
    def_formatter = argparse.ArgumentDefaultsHelpFormatter

    # ----------------
    # Main parser args
    # ----------------
    parser.add_argument(
        '--player-first-name',
        dest='player_first_name',
        type=str,
        required=True,
        default='James',
        help=(
            'Player first name'
        )
    )

    parser.add_argument(
        '--player-last-name',
        dest='player_last_name',
        type=str,
        required=True,
        default='Harden',
        help=(
            'Player last name'
        )
    )

    parser.add_argument(
        '--years',
        dest='years',
        nargs='+',
        required=True,
        help=('Input years as follows: --years 2018 2019 2020')
    )

    parser.add_argument(
        '--output_dir',
        dest='output_dir',
        type=str,
        required=False,
        help=('Directory in which to save player data as a csv')
    )    

    return parser.parse_args(args)


def main(args):
    """Main entry point allowing external calls

    Define any functionality here using arguments define above
    as inputs

    Args:
      args ([str]): command line parameter list
    """
    # Parses args defined above
    args = parse_args(args)

    df_games = getPlayerData(
        args.player_first_name,
        args.player_last_name,
        args.years
    )
    print(df_games)

def run():
    main(sys.argv[1:])

if __name__ == '__main__':
    run()