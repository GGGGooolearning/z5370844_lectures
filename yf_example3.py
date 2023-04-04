"""Docstring for the yf_example3.py module.

The purpose of the yf_example3 module is to download
stock price data for Qantas for a given year and save
the information in a CSV file.

"""

import os  # standard library imports first

import tookit_config as cfg
import yf_example2


def qan_prc_to_csv(year):
    """Docstring for qan_prc_to_csv function.

    Download Qantas stock prices for a given
    year into a CSV file

    Parameters
    ----------
    var1 : year
        single (mandatory) parameter called year, an integer.

    Returns
    -------
    type
        The name of this file will be qan_prc_YYYY.csv, where
        the YYYY stands for the year in year

    Notes
    -----
    This file will be saved under the data folder.

    Remember that the location of this folder is already
    in the toolkit_config module.

    """
    tic = 'QAN.AX'
    start = f'{year}-01-01'
    end = f'{year}-12-31'
    pth = os.path.join(cfg.DATADIR, f'qan_prc_{year}.csv')
    yf_example2.yf_prc_to_csv(tic, pth, start, end)
    # pth = os.path.join(datadir, 'qan_prc_2020.csv')

if __name__ == "__main__":
    qan_prc_to_csv(2018)

'''
if __name__ == "__main__":
    tic = 'QAN.AX'
    # datadir = '\\toolkit\\data'
    pth = os.path.join(cfg.DATADIR, 'qan_prc_YYYY.csv')
    # pth = f'{datadir}\\qan_prc_2020.csv'
    yf_example2.yf_prc_to_csv(tic, pth)
'''