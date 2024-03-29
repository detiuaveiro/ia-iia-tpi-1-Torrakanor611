# Pedro Abreu, 93240, MIECT
# aconselhei-me com Maria Rocha, LEI, 93320
# também com Ana Filipe, MIECT, 93350 
# e consultei múltiplos websites na net

from tree_search import *
from cidades import *
from strips import *
import sys
import operator

class MyTree(SearchTree):
    def __init__(self,problem, strategy='breadth'): 
        super().__init__(problem,strategy)
        # redifine root to be Aux Instance
        self.root = Aux(problem.initial, None)
        # redifine self.open_ones
        self.open_nodes = [self.root]
        self.from_init = None
        self.to_goal = None

    def hybrid1_add_to_open(self,lnewnodes):
        for i in range(len(lnewnodes)):
            if i % 2 != 0:
                self.open_nodes.extend([lnewnodes[len(lnewnodes) - 1 - i]])
            else:
                self.open_nodes.insert(0, lnewnodes[i])
    
    def hybrid2_add_to_open(self,lnewnodes):
        self.open_nodes.extend(lnewnodes)
        self.open_nodes = sorted(self.open_nodes, key = lambda x : (x.depth - x.offset))

    def search2(self):
        # clear rel
        # rel is a dict wich contains the last offset mapped to that depth
        rel = {}
        while self.open_nodes != []:
            node = self.open_nodes.pop(0)
            if self.problem.goal_test(node.state):
                self.terminal = len(self.open_nodes)+1
                self.solution = node
                return self.get_path(node)
            self.non_terminal+=1
            node.children = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                if newstate not in self.get_path(node):
                    newnode = Aux(newstate,node)
                    newnode.depth = get_depth(newnode)
                    if node.depth not in rel.keys():
                        rel[node.depth] = 0
                    else:
                        rel[node.depth] += 1
                    newnode.offset = rel[node.depth]
                    node.children.append(newnode)
            self.add_to_open(node.children)
        return None

    def search_from_middle(self):
        m = self.problem.domain.middle(self.problem.initial, self.problem.goal)

        self.from_init = MyTree(SearchProblem(self.problem.domain, self.problem.initial, m))
        self.to_goal = MyTree(SearchProblem(self.problem.domain, m, self.problem.goal))

        return list(dict.fromkeys(self.from_init.search() + self.to_goal.search()))

class Aux(SearchNode):
    def __init__(self,state,parent):
        super().__init__(state, parent)
        self.depth = 0
        self.offset = 0

class MinhasCidades(Cidades):

    # state that minimizes heuristic(state1,middle)+heuristic(middle,state2)
    def middle(self,city1,city2):
        # 1 linha
        return [con[0] for con in self.connections if float(self.heuristic(city1, con[0])) + float(self.heuristic(con[0], city2)) in [min(list(map(lambda x : float(self.heuristic(city1, x[0]) + self.heuristic(x[0], city2)) if x[0] not in [city1, city2] else sys.maxsize, self.connections)))]][0]

class MySTRIPS(STRIPS):
    def result(self, state, action):
        return [c for c in state if c not in action.neg] + action.pos

    def sort(self,state):
        return sorted(list(map(lambda x : str(x), state)))

def get_depth(item):
    if item.parent == None:
        return 0
    return 1 + get_depth(item.parent)

# def order_actions(actions, city):
#     new_actions = []
#     for act in actions:
#         if act[1] == city:
#             new_actions.append((act[1], act[0]))
#             continue
#         new_actions.append(act)
#     return new_actions

# def get_num(node):
#     if node.parent == None:
#         return 0

#     depth = 1 + get_num(node.parent)

#     print("node " + str(node))
#     print(depth)
#     print(node.parent.children)

#     return depth - ( node.parent.children.index(node) if len(node.parent.children) != None else 0)        

# def get_num(node, newnode_parent, offset):
#     if node.depth < newnode_parent.depth:
#         for nodex in node.children:
#             return get_num(nodex, newnode, offset)
#     elif node == newnode_parent.depth:
#         return offset + len(node.children)

# tentativa ex.2:
# # state that minimizes heuristic(state1,middle)+heuristic(middle,state2)
    # def middle(self,city1,city2):
    #     min = (city1, 10000)
    #     # actions todos as actions possíveis
    #     actions = self.actions(city1)
    #     actions = order_actions(actions, city1)
    #     actions = self.filter_actions(actions, city2)
    #     for act in actions:
    #         aux = self.middle_aux(city1, act[1], city2)
    #         if aux[1] < min[1]:
    #             min = aux
    #     return min
    #         # if act[1] == city2:
    #         #     return (act[0], self.heuristic(city1, act[0]) + self.heuristic(act[0], city2))
    #         # mid_heuristic = (act[1], self.heuristic(city1, act[1]) + self.heuristic(act[1], city2))
    #         # min_heuristic = self.middle(act[1], city2)
    #         # return min_heuristic if min_heuristic[1] < mid_heuristic[1] else mid_heuristic

    # def middle_aux(self, city1, m, city2):
    #     min_heuristic = (city1, 1000)
    #     # actions todos as actions possíveis
    #     actions = self.actions(m)
    #     actions = order_actions(actions, m)
    #     actions = self.filter_actions(actions, city2)
    #     for act in actions:
    #         if act[1] == city2:
    #             return (act[0], self.heuristic(city1, act[0]) + self.heuristic(act[0], city2))
    #         mid_heuristic = (act[0], self.heuristic(city1, act[0]) + self.heuristic(act[0], city2))
    #         min_heuristic = self.middle_aux(city1, act[1], city2)
    #         return min_heuristic if min_heuristic[1] < mid_heuristic[1] else mid_heuristic

    # def filter_actions(self, actions, city2):
    #     new_actions = []
    #     for act in actions:
    #         if self.heuristic(act[0], city2) > self.heuristic(act[1], city2):
    #             new_actions.append(act)
    #     return new_actions

# tentativa ex.3:
    # def do_search(self, city1, city2):
    #     return SearchProblem(self.problem.domain, city1, city2)
    #     m = self.problem.domain.middle(city1, city2)

    #     # print("city1: " + city1)*
    #     # print("city2: " + city2)
    #     # print("middle: " + str(m))

    #     if self.problem.domain.result(city1, (city1, city2)) != None:
    #         return city1

    #     s
    #     self.to_goal += self.do_search(m, city2)

    #     return  + path2