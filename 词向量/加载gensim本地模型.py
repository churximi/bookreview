#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
功能：加载gensim保存的本地model
时间：2016年5月21日 19:21:57
"""

from gensim.models import word2vec

model = word2vec.Word2Vec.load(u"C:\\Users\\lenovo\\Desktop\\word2vec实验\\text8.model")
y = model.most_similar(positive=['woman', 'king'], negative=['man'], topn=2)
for item in y:
    print item[0], item[1]

# 以一种C语言可以理解的模式存储词向量
model.save_word2vec_format('text8.model.bin', binary=True)

# 也可以加载上面形式的存储
model_2 = word2vec.Word2Vec.load_word2vec_format(u"C:\\Users\\lenovo\\Desktop\\word2vec实验\\"
                                                 u"text8.model.bin", binary=True)

# 寻找对应关系
# "boy" is to "father" as "girl" is to ...?
y2 = model.most_similar(['girl', 'father'], ['boy'], topn=3)
for item in y2:
    print item[0], item[1]

more_examples = ["he his she", "big bigger bad", "going went being"]
for example in more_examples:
    a, b, x = example.split()
    predicted = model.most_similar([x, b], [a])[0][0]
    print "'%s' is to '%s' as '%s' is to '%s'" % (a, b, x, predicted)

# 寻找不合群的词
y3 = model.doesnt_match("breakfast cereal dinner lunch".split())
print y3

if __name__ == "__main__":
    pass
