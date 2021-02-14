"""
Runner for making nba predictions for a player

Modes:
  1. parse-data: will pull player data over specified years (seasons) and save to a local dir
  2. feature-engineer: given output of `parse_data` will build a table that can be input into 
     a model 
  3. train-model: will run a pipeline to train a model predicting points per game 
  4. predict: given a model and opponent, will make a prediction of points per game 
""" 
import argparse
import logging
import sys
import os
import pandas as pd
import requests
import bs4
print(
    os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','..','data'))
)
from nba_predictions.player_scrape import getPlayerData

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger('nba_predictions')

def get_parser():
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
    
    # Probably remove this
    # parser.add_argument(
    #     '--player-first-name',
    #     dest='player_first_name',
    #     type=str,
    #     required=True,
    #     default='James',
    #     help=(
    #         'Player first name'
    #     )
    # )

    # -------------------------
    # mode1 parser - parse_data
    # -------------------------
    parse_data_desc = (
        'Parse player data'
    )
    parser_parse_data= subparsers.add_parser(
        'parse-data', help='Parse player data',
        formatter_class=def_formatter, description=parse_data_desc)

    # --------------------------------------------------
    # options for mode1 parser - add arguments for mode1
    # --------------------------------------------------
    parser_parse_data.add_argument(
        '--player-first-name',
        dest='player_first_name',
        type=str,
        required=True,
        default='James',
        help=(
            'Player first name'
        )
    )

    parser_parse_data.add_argument(
        '--player-last-name',
        dest='player_last_name',
        type=str,
        required=True,
        default='Harden',
        help=(
            'Player last name'
        )
    )    

    parser_parse_data.add_argument(
        '--years',
        dest='years',
        nargs='+',
        required=True,
        help=('Input years as follows: --years 2018 2019 2020')
    )

    # Default output-dir is the root directory of this repo in the data folder, which is included 
    # in the .gitignore
    parser_parse_data.add_argument(
        '--output-dir',
        dest='output_dir',
        type=str,
        default=os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)),'..','..','data')),
        required=False,
        help=('Directory in which to save player data as a csv. Default will ~/data in root dir of this package')
    )    

    # -------------------------------
    # mode2 parser - feature_engineer
    # -------------------------------
    feature_engineer_desc = (
        'Feature Engineer'
    )
    parser_feature_engineer= subparsers.add_parser(
        'feature-engineer', help='Feature engineer given output of parse_data',
        formatter_class=def_formatter, description=feature_engineer_desc)
    
    # ------------------------------------------
    # options for feature engineer parser - TODO
    # ------------------------------------------

    # --------------------------
    # mode3 parser - train_model
    # --------------------------
    train_model_desc = (
        'Train Model'
    )
    parser_train_model= subparsers.add_parser(
        'train-model', help='Train model given output of feature_engineer',
        formatter_class=def_formatter, description=train_model_desc)
    
    # -------------------------------------
    # options for train_model parser - TODO
    # -------------------------------------

    # ----------------------
    # mode4 parser - predict
    # ----------------------
    predict_desc = (
        'Predict'
    )
    parser_predict= subparsers.add_parser(
        'predict', help='given model make predictions for a new game',
        formatter_class=def_formatter, description=predict_desc)
    
    # ---------------------------------
    # options for predict parser - TODO
    # ---------------------------------

    return parser

def main():
    """Main entry point allowing external calls

    Define any functionality here using arguments define above
    as inputs

    Args:
      args ([str]): command line parameter list
    """
    # Parses args defined above
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    
    mode = args.command

    if mode == 'parse-data':
        # Check if output-dir specified
        if os.path.exists(args.output_dir):
            logger.info(f'Starting parse data for {args.player_first_name} {args.player_last_name} in {args.years}')

            # Get player data
            df_games = getPlayerData(
                args.player_first_name,
                args.player_last_name,
                args.years
            )
            if args.output_dir:
                if os.path.exists(args.output_dir):
                    df_games.to_csv(
                        os.path.join(args.output_dir,f'{args.player_first_name}_{args.player_last_name}_{"_".join(args.years)}.csv')
                    )                    
        else:
            print(f'hmm no such folder exists: {args.output_dir} \n please specify an existing directory..')

def run():
    main()

if __name__ == '__main__':
    run()