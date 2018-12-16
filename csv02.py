import pandas as pd

READ_FILE_FULL_PATH_1   = "resources/sample11.csv"

df = pd.read_csv(READ_FILE_FULL_PATH_1 )

# print(df)       # show all column
#print(df['A'])  # show 'A' column
# print(df['合計作業時間（秒）'])  # show 'A' column


df = pd.read_csv(READ_FILE_FULL_PATH_1, usecols=['タスク名', '合計作業時間（秒）'])
# df = pd.read_csv(READ_FILE_FULL_PATH_1, usecols=[2, 3])
# print(df)
for row in df:
#     # print(', '.join(row))
#     # print(row)          # 1行づつ取得できる
#     # print(row[0])          # 1行づつ取得できる
#     print(row)
#     pass


