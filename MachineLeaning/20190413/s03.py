import pandas as pd


# データの読み込み（df: data frame）
df = pd.read_csv('wine_class.csv')


# データの表示（先頭の３件）
a1 = df.head(3)

# print(a1)

# 教師データ（先頭のClass）
t = df.iloc[:, 0]  # アイロック。
#           [0:5, 1:3]  #=> 0～5行、1～3列。先頭を省略すると、一番最初から。末尾を省略すると、末尾まで。


# 入力変数（1番目から最後まで）
x = df.iloc[:, 1:]

# 表示して確認
x.head(3)

print(x.head(3))


# サイズの確認
x.shape

print(x.shape)


type(x)

type(x.values)

t.min()

t.max()

# Numpyにデータ型を変換し、ラベルを0から始める
t = t.values - 1
x = x.values

type(t)

type(x)

t.dtype

# 32bitに変換
x = x.astype('float32')
t = t.astype('int32')

x.dtype

t.dtype

# Chainerで使用できるデータセットの形式
dataset = list(zip(x, t))

len(dataset)

# 訓練データのサンプル数
n_train = int(len(dataset) * 0.7)

# 訓練データ(train)と検証データ(test)に分割
train, test = chainer.datasets.split_dataset_random(dataset, n_train, seed=1)





