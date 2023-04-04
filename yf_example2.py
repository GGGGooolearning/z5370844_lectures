""" yf_example2.py

Example of a function to download stock prices from Yahoo Finance.
"""

import yfinance as yf


def yf_prc_to_csv(tic, pth, start=None, end=None):
    """ Downloads analysts recommendation from Yahoo Finance and saves the
    information in a CSV file

    Parameters
    ----------
    tic : str
        Ticker

    pth : str
        Location of the output CSV file

    start: str, optional
        Download start date string (YYYY-MM-DD)
        If None (the default), start is set to '1900-01-01'

    end: str, optional
        Download end date string (YYYY-MM-DD)
        If None (the default), end is set to the most current date available
    """
    df = yf.download(tic, start=start, end=end)
    df.to_csv(pth)


''' Example
tic = 'QAN.AX'
pth = 'qan_stk_prc.csv'
yf_prc_to_csv(tic, pth)
'''

# REMEMBER TO DELETE THIS!!!
# This will print the value of __name__
#print(f"The value of __name__ is: '{__name__}'")

#完整版
'''
if __name__ == "__main__":
    tic = 'QAN.AX'
    pth = 'qan_stk_prc.csv'
    yf_prc_to_csv(tic, pth)
'''
#存储csv到文件夹
if __name__ == "__main__":
    tic = 'QAN.AX'
    datadir = 'C:\\home\\breno\\codes\\pycharm\\tmp\\toolkit\\data'
    pth = f'{datadir}\\qan_stk_prc.csv'
    yf_prc_to_csv(tic, pth)
