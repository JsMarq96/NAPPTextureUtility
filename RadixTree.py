#!/usr/bin/env python3

'''
    Radix tree utility for speeding up the directory comparison
    by Juan S. Marquerie
'''


def str_compare(str1, str2):
    '''Returns the char similarity count between 2 strigs'''
    i = 0
    for i in range(min(len(str1), len(str2))):
        if str1[i] != str2[i]:
            return i + 1
    return i + 1

class RT_Node:
    '''Node of a radix tree'''
    def __init__(self):
        self.base_str = None
        self.result = None
        self.nodes = [None] * 128

class RadixTree:
    '''Custom radix tree implementation'''
    def __init__(self, default_value=None):
        self.base_node = RT_Node()
        self.default_result = default_value

    def get(self, search_str):
        '''Fethc an element from the radix tree'''
        iter_node = self.base_node.nodes[ord(search_str[0])]
        while not iter_node is None:
            similarity = str_compare(search_str, iter_node.base_str)

            #print(':+SEARCH ', similarity, search_str, iter_node.base_str)
            if similarity == len(search_str) and similarity == len(iter_node.base_str):
                return iter_node.result
            elif similarity == 0 or similarity < len(iter_node.base_str):
                return self.default_result
            else:
                # Split the similar part of the serach and continues search on another node
                search_str = search_str[similarity:]
                iter_node = iter_node.nodes[ord(search_str[0])]

        return self.default_result

    def get_with_wildcard(self, search_str):
        '''Flexibilices the get procedure with the addiciont of * wildcards'''
        if 'magma' in search_str:
            print(search_str, '--------<<<<<<<')
        iter_node = self.base_node.nodes[ord(search_str[0])]
        while not iter_node is None:
            similarity = str_compare(search_str, iter_node.base_str)

             # Addition of the wildcard
            if iter_node.base_str[similarity - 1] == '*':
                return iter_node.result
            if similarity == len(search_str) and similarity == len(iter_node.base_str):
                return iter_node.result
            elif similarity == 0 or similarity < len(iter_node.base_str):
                return self.default_result
            else:
                # Split the similar part of the serach and continues search on another node
                search_str = search_str[similarity:]
                iter_node = iter_node.nodes[ord(search_str[0])]

        return self.default_result

    def add(self, search_str, result):
        '''Append an element to the radix tree'''
        # Base node insert
        if self.base_node.nodes[ord(search_str[0])] is None:
            tmp = RT_Node()
            tmp.base_str = search_str
            tmp.result = result
            self.base_node.nodes[ord(search_str[0])] = tmp

            return

        iter_node = self.base_node.nodes[ord(search_str[0])]

        while True:
            base_similarity = str_compare(search_str, iter_node.base_str)
            crop_search_str = search_str[base_similarity:]
            print('~~~crop search str', crop_search_str, 'search_str', search_str)
            search_index = ord(crop_search_str[0])

            if base_similarity < len(iter_node.base_str):
                old_root_node = RT_Node()
                old_root_node.nodes = iter_node.nodes
                old_root_node.base_str = iter_node.base_str[base_similarity-1:]
                old_root_node.result = iter_node.result

                iter_node.base_str = search_str[:base_similarity-1]
                iter_node.nodes = [None] * 128

                iter_node.nodes[ord(old_root_node.base_str[0])] = old_root_node

                new_node = RT_Node()
                new_node.base_str = search_str[base_similarity-1:]
                new_node.result = result

                iter_node.nodes[ord(new_node.base_str[0])] = new_node

                return
            elif base_similarity > len(iter_node.base_str):
                if iter_node.nodes[search_index] is None:
                    new_node = RT_Node()
                    new_node.base_str = crop_search_str
                    new_node.result = result

                    iter_node.nodes[search_index] = new_node
                    return

                iter_node = iter_node.nodes[search_index]
                search_str = crop_search_str
            else:
                if iter_node.nodes[search_index] is None:
                    new_node = RT_Node()
                    new_node.base_str = crop_search_str
                    new_node.result = result

                    iter_node.nodes[search_index] = new_node
                    return
                search_str = crop_search_str
                iter_node = iter_node.nodes[search_index]

if __name__ == '__main__':
    rt = RadixTree(True)

    test_arr = ['assets/minecraft/textures/gui/title/background/panorama_0.png',
                'assets/minecraft/textures/gui/title/background/panorama_4.png',
                'assets/minecraft/textures/gui/title/background/panorama_3.png',
                'assets/minecraft/textures/gui/title/background/panorama_5.png',
                'assets/minecraft/textures/gui/title/background/panorama_2.png',
                'assets/minecraft/textures/gui/title/background/panorama_1.png']

    for t in test_arr:
        print('Inserting ', t)
        rt.add(t, False)
        for v in test_arr:
            print(v, rt.get(v))
        print('==========')
