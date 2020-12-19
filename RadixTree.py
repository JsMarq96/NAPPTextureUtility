#!/usr/bin/env python3

'''
    Radix tree utility for speeding up the directory comparison
    by Juan S. Marquerie
'''

'''
Que tiene que hacer
Dada un string, decir sis e tiene que escalar con que proporciones
'''

'''
    Returns the char similarity count between 2 strigs
'''
def str_compare(str1, str2):
    i = 0
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            return i + 1;
    return i

class RT_Node:
    def __init__(self):
        self.base_str = ''
        self.result = None
        self.nodes = [None] * 256

class RadixTree:
    def __init__(self, default_value=None):
        self.base_node = RT_Node()
        self.default_result = default_value

    def add(self, search_str, result):
        # Comparar la search str entre todos los nodos que tenga
        # Caso 1: No similarity
        # Case 2: Kinda similar on the end
        # Case 3: Similar on the start, up to the middle
        # Are 2 and 3 the same...?

        # Base node insert
        if self.base_node.nodes[int(search_str[0])] == None:
            tmp = RT_Node()
            tmp.base_str = search_str
            tmp.result = result
            self.base_node.nodes[int(search_str[0])] = tmp

            return

        iter_node = self.base_node.nodes[int(search_str[0])]

        while True:
            base_similarity = str_compare(search_str, iter_node.base_str)
            crop_search_str = search_str[base_similarity:]
            search_index = int(crop_search_str[0])

            if iter_node.nodes[search_index] == None:
                tmp = RT_Node()
                tmp.base_str = crop_search_str
                tmp.result = result
                self.base_node.nodes[int(search_str[0])] = tmp

                return
            else:

                if len(iter_node.base_str) > base_similarity:
                    # Substitute root with the new node, with two leaves
                    # Before ---[P1] --...
                    # After:
                    #             --[N2]
                    # ------[N1]-|--[P1]

                    prev_root_node_index = int(self.base_node.base_str[base_similarity + 1])
                    new_root_node = RT_Node()
                    new_root_node.base_str = self.base_node.base_str[0:base_similarity]
                    new_root_node.nodes[prev_root_node_index] = self.base_node
                    new_root_node.nodes[prev_root_node_index].base_str = new_root_node.nodes[prev_root_node_index].base_str[base_similarity+1:]

                    self.base_node = new_root_node
