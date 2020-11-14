from tree_search import *
from cidades import *
from strips import *
import sys


class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth'): 
        super().__init__(problem,strategy)
        self.mylist = []

    def hybrid1_add_to_open(self,lnewnodes):
        # for i in range(len(lnewnodes) - 1):
        #     if i % 2 == 0:
        #         self.open_nodes.extend([lnewnodes[i]])
        #     else:
        #         self.open_nodes[:0] = [lnewnodes[i]]
        self.mylist.extend(lnewnodes)
        len("len of mylist: "+ len(self.))
    
    def hybrid2_add_to_open(self,lnewnodes):
        self.open_nodes.extend(lnewnodes)
        self.open_nodes = sorted(self.open_nodes, key=sorter)

    def search2(self):
        while self.open_nodes != []:
            # print(len(self.open_nodes))
            node = self.open_nodes.pop(0)
            if self.problem.goal_test(node.state):
                self.terminal = len(self.open_nodes)+1
                self.solution = node
                print(self.get_path(node))
                return self.get_path(node)
            self.non_terminal+=1
            node.children = []
            for a in self.problem.domain.actions(node.state):
                newstate = self.problem.domain.result(node.state,a)
                if newstate not in self.get_path(node):
                    newnode = SearchNode(newstate,node)
                    node.children.append(newnode)
            self.add_to_open(node.children)
        print("sou none type!")
        return None

    def search_from_middle(self):
        #IMPLEMENT HERE
        pass


class MinhasCidades(Cidades):

    # state that minimizes heuristic(state1,middle)+heuristic(middle,state2)
    def middle(self,city1,city2):

        # print([min(list(map(lambda x : float(self.heuristic(city1, x[0]) + self.heuristic(x[0], city2) - float(self.heuristic(city1, city2))), self.connections)))])
        # 1 linha
        return [con[0] for con in self.connections if float(self.heuristic(city1, con[0])) + float(self.heuristic(con[0], city2)) in [min(list(map(lambda x : float(self.heuristic(city1, x[0]) + self.heuristic(x[0], city2)) if x[0] not in [city1, city2] else sys.maxsize, self.connections)))]][0]
    
    # aux = [connection for connection in [min(list(map(lambda x : float(self.heuristic(city1, x[0]) + self.heuristic(x[0], city2)), self.connections)))]) if self.heuristic(city1, x[0]) + self.heuristic(x[0], city2)]


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



class MySTRIPS(STRIPS):
    def result(self, state, action):
        return [c for c in state if c not in action.neg] + action.pos

    def sort(self,state):
        return sorted(list(map(lambda x : str(x), state)))

# def order_actions(actions, city):
#     new_actions = []
#     for act in actions:
#         if act[1] == city:
#             new_actions.append((act[1], act[0]))
#             continue
#         new_actions.append(act)
#     return new_actions

def sorter(item):
    depth = get_depth(item)

    return depth - item.parent.children.index(item)

def get_depth(item):
    if item.parent == None:
        return 1
    return 1 + get_depth(item.parent)
            


