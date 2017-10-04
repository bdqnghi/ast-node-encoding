import pickle
import gensim
import os
import codecs
from sklearn.manifold import TSNE
from gensim.models.keyedvectors import KeyedVectors
import matplotlib.pyplot as plt
from node_map import NODE_LIST


test_words = ["BinOp","If","For","Break","While","FunctionDef"]

vectors = KeyedVectors.load_word2vec_format("./data/vectors.txt",binary=False)

for w in test_words:

	print w + " " + str(vectors.similar_by_vector(vectors[w], topn=6))