# Encoding the AST Tree using a strategy similar to word2vec, but applied to the context of AST's

This works is an attempt to learn vector representation for AST nodes. The original paper is: https://arxiv.org/abs/1409.3358 Since this paper is difficult to understand and implement, I applied the strategy similar to word2vec to learned embeddings of AST nodes. 

* Vectors are learned by a variation of word2vec instead of the proposed method.
* Adam is used instead of gradient descent.
* The dataset used in this implementation is smaller than in the original paper. I crawled Python algorithms from Github by myself since using the built in Python AST parser for Python code is more convenient and less time-consuming than writing the AST Parser for the C++ code in the original dataset, thus the node type is a little bit different.

The list of learned token vectors can be found here:
https://github.com/bdqnghi/ast-node-encoding/blob/master/data/vectors.txt

A visualization of learned token
--------------------------
![](ast_nodes_visualization.png)
