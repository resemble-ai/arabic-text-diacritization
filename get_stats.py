import matplotlib.pyplot as plt
import numpy as np
import pickle


charset = {}
trn = "../dataset/train.txt"
val = "../dataset/val.txt"
tst = "../dataset/test.txt"

# files = [""]
# text = ""
lens = []
for f in [trn, val, tst]:
    with open(trn) as fp:
        for line in fp:
            lens.append(len(line.strip()))
            for char in line.strip():
                charset[char] = 1

# x = set(text)

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
bins = np.linspace(0, 2000, 100)
hist, bins_, _ = ax.hist(lens, bins=bins)
ax.set_yscale('log')
ax.set_title(f"Longest: {max(lens)}")
ax.set_ylabel("Frequency")
ax.set_xlabel("Length")
fig.tight_layout()
fig.savefig('test.png')
plt.close()    


with open("constants/ARABIC_LETTERS_LIST.pickle", "rb") as fp:
    arabic = pickle.load(fp)

with open("constants/CLASSES_LIST.pickle", "rb") as fp:
    cla = pickle.load(fp)

with open("constants/DIACRITICS_LIST.pickle", "rb") as fp:
    dia = pickle.load(fp)


set(charset.keys()) - set(arabic) - set(cla) - set([str(i) for i in range(10)]) - set(r" .,:!;[](){}~*«»\"\'،؛؟/")

len(arabic) + len(cla) + len([str(i) for i in range(10)]) + len(r" .,:!;[](){}~*«»\"\'،؛؟/")


charset_ = set(charset.keys())

arabic_ = set(arabic) 
cla_ = set(cla)
digit_ = set([str(i) for i in range(10)])
punct_ = set(r"`- .,;:![](){}'~*«»،؛؟/" + '"')
spec = set(["–", "\u200f"])


len(arabic_)+ len(cla_)+ len(digit_)+ len(punct_)+ len(spec)


import pickle

with open("constants/ARABIC_LETTERS_LIST.pickle", "rb") as fp:
    arabic = pickle.load(fp)

with open("constants/CLASSES_LIST.pickle", "rb") as fp:
    cla = pickle.load(fp)

with open("constants/DIACRITICS_LIST.pickle", "rb") as fp:
    dia = pickle.load(fp)


# make 0 a padding symbol/index
# NOTE: the dash is chr(8212), not chr(8211)
char_list = [chr(0)] + \
    list(arabic) + \
    cla + \
    list([str(i) for i in range(10)]) + \
    list(" .,:;!") + \
    list("،؟؛") + \
    list("()[]{}\"'«»") + \
    list("`*~/") + \
    list("-—") +\
    ["\u200f"]

with open("arabic_char_list_81.pkl", "wb") as fp:
    pickle.dump(char_list, fp)
