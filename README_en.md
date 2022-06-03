# De Novo Assembler - part 1

In this task, you will begin to develop your own de novo assemler that is able to reconstruct a genome from NGS data. Initially, you will be working with exemplary error-free data, later error correction will be added.

In this first part, you will develop the basis for the creation of a de-Bruijn graph from NGS reads. For this, you have two FASTA files with reads in the data directory ("data/test.fasta" and "data/virus_perfectreads.fasta"). 

For the preparation, you need to develop a few classes and top level methods.

## Read

The class `Read` represents a single NGS read. Since reads are read from FASTA files, the class should be able to extract sequence information from FASTA-formatted lines.

A FASTA file is structured as follows:

```text
>Readname 1
Sequence line 1
Sequence line 2
.
.
Sequence line n
>Readname 2
Sequence line 1
Sequence line 2
.
.
Sequence line n
.
.
.
>Readname n
Sequence line 1
Sequence line 2
.
.
Sequence line n
```

So a FASTA file contains an arbitrary number of reads. Each read begins with a line with a read name, which is marked by the first character of the line being `>`. The read name is followed by at least one line with bases (A, G, T or C). If several lines of bases follow the read name, then all of these together describe the sequence, so they need to be concatenated. 

Implement a class `Read` with the following methods:

* A constructor that takes the lines describing this read (readname and sequence lines) as a string array. 
* `get_kmers(self, kmersize)`: Returns all k-mers of length k from the read sequence as a dictionary. The key is the k-mer sequence, the value is how often this k-mer occurs in the sequence. 
* `__str__(self)`: Returns the read as a string, in the format: "Name: Sequence". If the sequence is longer than 20 bases, only the first 20 bases followed by "..." should be printed, e.g. "Read 2: AGTCGTAGCGTACCGTAGCC..." 
* ```__repr__(self)```: Returns the same thing as ```__str__```    
* ```__eq__(self, other)```: This is the comparison operator that is called when two objects are compared to each other using `==`. This should return `true` iff the name and the sequence of the read `other` are identical with this read. Otherwise it should return false (please mind that `other` could be of any class - use `isinstance` to make sure that you are actually dealing with a `Read` before you start comparing).

## read_fasta

The reading of the whole FASTA file should happen in the top-level method `read_fasta(filename)`. This method should return a list of `Read` object representing the reads from the FASTA file `filename`.

## DBGNode

The class `DBGNode` represents a single node in the de-Bruijn graph - which is effectively a k-mer with a list of incoming and outgoing edges. Implement the following methods in this class:

* A constructor that takes the sequence of the node (the k-mer)
* `get_potential_from(self)`: Returns a list of all k-mer sequences that could theoretically have an edge to this node. Remember that the overlap length has to be exactly of length `k-1` and that DNA sequences have a limited alphabet (`["A", "G", "T", "C"]`) - so you can trivially enumerate all other k-mer sequences that can potentially have an edge to this one.
* `get_potential_to(self)`: Same as `get_potential_from(self)`, but returns a list of k-mer sequences that this node could have an edge to (not from).
* `add_edge_to(self, eto)`: Adds an edge to the `DBGNode` `eto` to an internal list of edges. If this edge is already present, increases the weight of the edge by 1 (so the edge list should be a dictionary with key=`DBGNode` and value = `weight`).
* `add_edge_from(self, efrom)`: Same as above, but adds an edge from the node `efrom` (not to).
* `get_edge_from_weight(self, other)`: Returns the weight of the edge from the `DBGNode` `other`, or 0 if that edge does not exist.
* ```get_edge_to_weight(self, other)```: Smae as above, but returns the weight of the edge to `other`, not from. 
