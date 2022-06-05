# ライブラリ
import MeCab
import random

kashi_list = pd.read_csv("kashi.csv")
kashi_list = list(kashi_list["0"].values)
tagger = MeCab.Tagger("-Owakati")

# 単語、分かち書き、単語一覧
words = []
wakachi = []
for k in kashi_list:
  s = tagger.parse(k).split()
  words += s
  wakachi += [s]
unique = list(set(words))

# 隣接リスト
ls = [[] for i in range(len(unique))]

for k in wakachi:
  for n,w in enumerate(k):
    if n == len(k)-1:
      continue
    w1 = w
    w2 = k[n+1]
    ls[unique.index(w1)].append(unique.index(w2))
    
# 初期番号
num = random.randint(0,len(unique))
# 文の長さ
length = 30

for i in range(length):
  num = random.choice(ls[num])
  print(unique[num], end="")
