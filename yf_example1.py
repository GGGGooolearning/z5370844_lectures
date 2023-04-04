# Downloads Qantas share price beginning 1 January 2020
import yfinance as yf                                       # (1)

tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
# end = '2023-01-01'                                               # (4)
df = yf.download(tic, start, None)   # (5)

print(df)                                                 # (6)
df.to_csv('a_stk_prc.csv')# (7)


