import pickle
import gensim
import os
import codecs
from sklearn.manifold import TSNE
from gensim.models.keyedvectors import KeyedVectors
import matplotlib.pyplot as plt
with open("./data/vectors.pkl", "rb") as sample_file:
	samples = pickle.load(sample_file)

print samples

def search_dict_by_value(value,node_map):
	result = None
	for word, index in node_map.iteritems():
		if value == index:
			result = word
	return result

def print_word2vec_format(outfile):
	vectors = outfile[0]
	node_map = outfile[1]
	
	with open("./data/vectors.txt","a") as f:
		f.write(str(len(node_map)) + " " + str(30) + "\n")

	index = 0
	for vector in vectors:

		
		word = search_dict_by_value(index, node_map)
		
		
		print vector
		print "word : " + word + " has index " + str(index)

		
		vector_list = list()
		for feature in vector.ravel():
			# vector_str += str(feature) + " "
			vector_list.append(str(feature))

		row = word + " " + " ".join(vector_list)

		with open("./data/vectors.txt","a") as f:
			f.write(row + "\n")
		index += 1

words = list()
for key, value in samples[1].items():
	words.append(key)

words = tuple(words)
# print_word2vec_format(samples)	



vectors = KeyedVectors.load_word2vec_format("./data/vectors.txt",binary=False)

print vectors["Module"]
tsne = TSNE(n_components=2, random_state=0)


Y = tsne.fit_transform(samples[0])

plt.scatter(Y[:,0],Y[:,1])
for label, x, y in zip(words,Y[:,0],Y[:,1]):
	# color = "blue"
	# if "cs" in label:
	# 	color = "red"
	
	plt.annotate(label,xy=(x,y),xytext=(0,0),textcoords="offset points",color="blue")


plt.show()
