from tree_search import *
from cidades import *
from strips import *


class MyTree(SearchTree):

    def __init__(self,problem, strategy='breadth'): 
        super().__init__(problem,strategy)

    def hybrid1_add_to_open(self,lnewnodes):
        #IMPLEMENT HERE
        pass

    def hybrid2_add_to_open(self,lnewnodes):
        #IMPLEMENT HERE
        pass

    def search2(self):
        #IMPLEMENT HERE
        pass


    def search_from_middle(self):
        #IMPLEMENT HERE
        pass


class MinhasCidades(Cidades):

    # state that minimizes heuristic(state1,middle)+heuristic(middle,state2)
    def middle(self,city1,city2):
        #IMPLEMENT HERE
        pass

class MySTRIPS(STRIPS):
    def result(self, state, action):
        #IMPLEMENT HERE
        pass
    def sort(self,state):
        #IMPLEMENT HERE
        pass


