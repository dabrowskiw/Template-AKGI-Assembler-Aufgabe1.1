# De Novo Assembler - part 2

After you have implemented the necessary base classes and methods in the last exercise, now you can actually build the graph.
## DBGraph

The class `DBGraph` represents the graph, which is basically a list of nodes. It should contain the following methods:

* An empty constructor that initializes the internal data structures
* `add_kmers(self, kmers)`: Adds the k-mers from the dictionary `kmers` to the graph. This is exactly the dictionary returned by `Read.get_kmers()`. This method also should create the appropriate edges: If a k-mer is added to the graph, you need to check whether other k-mers already exist in the graph that need to have edges to or from the newly added k-mer. You can use the methods `get_potential_to` and `get_potential_from`, so you don't need to go through all k-mers and can instead just specifically check for the existence of the relevant k-mers. This is why the construction of the de Bruijn graph is so performant. It is also important to ensure that the graph only contains k-mers of the same length. If an attempt is made to add a k-mer to the graph that has a length different to the k-mers already present in the graph, a `ValueError` should be raised.
* `count_edges(self)`: Returns the number of edges in the graph. An edge should only be counted once - if there is an edge from node A to node B, then this edge is saved in both nodes (in the list of edges_from of node B and the list of edges_to in node A). However, this needs to be counted as only one edge in `count_edges()`.
* `count_nodes(self)`: Returns the number of nodes in the graph.
* `__str__(self)`: Returns a string with information on what the k-mer length of the graph is and how many edges and nodes it contains. 

## build_graph

Now you can finally create a graph from the reads in a FASTA file: Implement a top-level method `build_graph(filename, kmersize)` that creates and returns a graph with k-mer length `kmersize` from the FASTA file in path `filename`.
      
You can use the file test.fasta from the data directory to test the results. With a k-mer length of 6 you should see:

```text
4 k-mers/nodes
3 edges
```

With a k-mer length of 2 you should get:

```text
8 k-mers/nodes
17 edges
```

Then, construct a graph from virus_perfectreads.fasta. with a k-mer length of 100 you should get:

```text
2331 k-mers
2330 edges
```

and with k-mer length of 10:

```text
2414 k-mers
2460 edges
```

Take a moment to think about what it means when the number of edges = number of kmers - 1. What is the graph likely to look like? Is it easier or harder to reconstruct the genome when the number of edges is larger than the number of nodes?
