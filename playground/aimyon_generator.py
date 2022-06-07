# ライブラリ
import MeCab
import random


# 歌詞を読み込み
kashi_list = []
with open("/content/drive/MyDrive/Colab Notebooks/あいみょん歌詞/kashi.txt", "r") as f:
  for k in f:
    kashi_list.append(k)
    
# 分かち書きを読み込み
wakachi = []
with open("/content/drive/MyDrive/Colab Notebooks/あいみょん歌詞/wakachi.txt", "r") as f:
  for song in f:
    wakachi.append(song.split())

# 単語一覧を読み込み
unique = []
with open("/content/drive/MyDrive/Colab Notebooks/あいみょん歌詞/word.txt", "r") as f:
  for w in f:
    unique.append(w.replace("\n",""))

# 隣接リストを読み込む
ls = []
with open("/content/drive/MyDrive/Colab Notebooks/あいみょん歌詞/ls.txt", "r") as f:
  for low in f:
    ls.append([int(i) for i in low.split()])
    

# 初期番号
num = random.randint(0,len(unique))
w = None

while w != ";":
  num = random.choice(ls[num])
  w = unique[num]
  if "*" in w:
    for i in range(len(w)):
      print("")
  else:
    print(w, end="")
