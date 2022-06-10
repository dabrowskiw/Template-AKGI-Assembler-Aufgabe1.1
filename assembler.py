#! /usr/bin/python3

import sys


class Read:
    def __init__(self, lines):
        pass

    def get_kmers(self, kmersize):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __eq__(self, other):
        pass


class DBGnode:
    def __init__(self, kmer):
        pass

    def add_edge_to(self, eto):
        pass

    def add_edge_from(self, efrom):
        pass

    def get_potential_from(self):
        pass

    def get_potential_to(self):
        pass

    def get_edge_to_weight(self, other):
        pass

    def get_edge_from_weight(self, other):
        pass

class DBGraph:
    def __init__(self):
        pass

    def add_kmers(self, kmers):
        pass

    def count_edges(self):
        pass

    def count_nodes(self):
        pass

    def __str__(self):
        pass


def read_fasta(readfile):
    pass


def build_graph(filename, kmersize):
    pass


if __name__ == "__main__":
    pass
