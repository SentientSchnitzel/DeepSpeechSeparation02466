import pandas as pd
df = pd.DataFrame([range(1+i,101+i) for i in range(1,101)],)
# print(df)
df.to_csv("100x100_numbers.csv", sep=",")