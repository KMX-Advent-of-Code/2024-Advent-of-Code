import networkx as nx
import numpy as np
from collections import defaultdict


def make_graph(myarray):
    graph = nx.grid_2d_graph(
        myarray.shape[0], myarray.shape[1], create_using=nx.DiGraph
    )  # connect everything in the grid
    graph.remove_edges_from(
        [(x, y) for x, y in graph.edges if (myarray[x] - myarray[y]) != -1]
    )
    return graph


def string_to_int_lists(s):
    return [[int(x) for x in list(x)] for x in s.split('\n')]


def undumb(l):
    return [tuple([int(y) for y in x]) for x in l]


def get_coords(arr, val):
    return undumb(zip(*np.where(arr == val)))


def solve(s):
    myarray = np.array(string_to_int_lists(s))
    graph = make_graph(myarray)
    out_dict = defaultdict(int)
    for zero in get_coords(myarray, 0):
        for nine in get_coords(myarray, 9):
            out_dict[zero] += int(nx.has_path(graph, zero, nine))
    return sum(out_dict.values())


def solve2(s):
    myarray = np.array(string_to_int_lists(s))
    graph = make_graph(myarray)
    out_dict = defaultdict(int)
    for zero in get_coords(myarray, 0):
        for nine in get_coords(myarray, 9):
            if nx.has_path(graph, zero, nine):
                out_dict[zero] += len(list(nx.all_shortest_paths(graph, zero, nine)))
    return sum(out_dict.values())
