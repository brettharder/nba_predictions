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

    # parser.add_argument(
    #     '--opponent',
    #     dest='opponent',
    #     type=str,
    #     required=False,
    # )

    # # Add an argument to overall module
    # parser.add_argument(
    #     '--optional-overall-argument',
    #     dest='optional_overall_argument',
    #     type=str,
    #     required=False,
    #     default='some_default_value',
    #     help=(
    #         'General argument that you may want to use for all modes'
    #     )
    # )

    # ------------
    # mode1 parser
    # ------------
    mode1_desc = (
        'some description for mode1 '
    )
    parser_mode1= subparsers.add_parser(
        mode1, help='Helpful quick sentence for mode1',
        formatter_class=def_formatter, description=mode1_desc)

    # --------------------------------------------------
    # options for mode1 parser - add arguments for mode1
    # --------------------------------------------------
    parser_mode1.add_argument(
        '-a', '--a-argument',
        dest='a_argument',
        required=True,
        default='',
        help=('An argument for mode1 parser')
    )

    parser_mode1.add_argument(
        '-b', '--b-argument',
        dest='b_argument',
        required=True,
        default='',
        help=('Another argument for mode1 parser')
    )

    # Argument for multiple inputs
    parser_mode1.add_argument(
        '--list-arg',
        dest='list_arg',
        required=False,
        nargs='+',
        help=('Input as follows: --list-arg val1 val2 val3')
    )

    # ------------
    # mode2 parser
    # ------------
    mode2_desc = (
        'some description for mode2 '
    )
    parser_mode2= subparsers.add_parser(
        mode2, help='Helpful quick sentence for mode2',
        formatter_class=def_formatter, description=mode2_desc)

    # --------------------------------------------------
    # options for mode2 parser - add arguments for mode2
    # --------------------------------------------------
    parser_mode2.add_argument(
        '-a', '--a-argument',
        dest='a_argument',
        required=True,
        default='',
        help=('An argument for mode2 parser')
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
    mode = args.command

    # Get general args
    optional_overall_argument = args.optional_overall_argument

    # ----------------
    # Split into modes
    # ----------------
    if mode == mode1:
        # Note can add any functionality here for mode1 using mode1 args
        logger.info('Running mode1 ...')
        print('Running mode1 ...')
        print(args.a_argument)
        print(args.b_argument)

    elif mode == mode2:
        # Note can add any functionality here for mode2 using mode2 args
        logger.info('Running mode2 ...')
        print('Running mode2 ...')

    else:
        raise Exception(
            "Please choose runner mode in ('mode1','mode2')"
        )

def run():
    main(sys.argv[1:])

if __name__ == '__main__':
    run()
