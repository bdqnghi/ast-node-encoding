# Encoding the AST Tree using a strategy similar to word2vec, but applied to the context of AST's.

This project aims to learn vector representations for AST nodes. [Building Program Vector Representations for Deep Learning] (https://arxiv.org/abs/1409.3358) is the original paper presented at AAAI 2015. Instead of the method proposed in this paper, I use a strategy similar to word2vec to learn AST node embeddings.

* Vectors are learned by using a variation of word2vec instead of the proposed method. The intuition is similar to the original paper in that it captures the context of a parent node by learning its children's vectors. The original paper attempted to minimize the distance between the parent node and the sum vectors of its children. Given a specific token type as input, look through its children and choose one at random. The network will tell us the likelihood of each token in our vocabulary being its child that we chose. Because the number of AST token types is limited, the vocabulary is relatively small (around 92 token types).

* Adam Optimizer is used instead of Stochastic Gradient Descent.

* The dataset used in this implementation is smaller than the dataset used in the original paper. I crawled Python algorithms from Github because using the built-in Python AST parser for Python code is more convenient and time-consuming than writing the AST Parser for C++ code in the original dataset, so the node type is different.

### How to run
```python
python2 train.py
```

The list of learned token vectors can be found here:
https://github.com/bdqnghi/ast-node-encoding/blob/master/data/vectors.txt

A visualization of learned token
--------------------------
![](ast_nodes_visualization.png)
