import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')

ans = 0
xavg = round(np.mean(data['Date']), 2)
print(xavg)
n = 0
for i in data['Date']:
    n += 1
    a = round((round(i, 2)-xavg)**2, 4)
    print(f'{n} | {i} | {round(i-xavg, 2)} | {a} |')

    print('-'*len(str(n)), '|', '-'*len(str(i)), '|', '-'*len(str(round(i-xavg, 2))), '|', '-'*len(str(round((i-xavg)**2, 4))), '|')

    if n >= 38 and n != 50:
        ans += a

print(round(ans, 4))
