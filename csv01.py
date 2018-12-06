import csv

READ_FILE_FULL_PATH_1   = "resources/sample11.csv"
CREATE_FILE_FULL_PATH_1 = "resources/sample11_after_.csv"


with open(READ_FILE_FULL_PATH_1,'r', newline='', encoding="utf-8") as csvfile:
    # spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    # for row in spamreader:
    #     print(', '.join(row))


    # spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    # for row in spamreader:
    #     print(row)          # 1行づつ取得できる

# with open(FILE_NAME_FULL_PATH_1 , 'r',encoding="utf-8") as f:
#     reader = csv.reader(f)
#     header = next(reader)  # ヘッダーを読み飛ばしたい時

#     for row in reader:
#         print("a")          # 1行づつ取得できる

