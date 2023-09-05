import numpy as np
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
import pydot
from helper import draw_legend


class Node:
    def __init__(self, state, parent, action, level,left=None, right=None, top=None, down=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.level=level
        self.left=left
        self.right=right
        self.top=top
        self.down=down
        if self.parent==None:
            color="cyan"
        elif (self.state[0]== goal).all():
            color="gold"
        else:
            color="red"
        self.graph_node = pydot.Node(str(self), style="filled", fillcolor=color)
    def update_color(self):		
        if ((self.state[0]!=start).any() and (self.state[0]!=goal).any()):
            self.graph_node = pydot.Node(str(self), style="filled", fillcolor="green")
        
        

        
    def __str__(self):
        return str(self.state[0])
    
    
class StackFrontier:
    def __init__(self):
        self.stack = []

    def add(self, node):
        self.stack.append(node)

    def contains_state(self, state):
        return any((node.state[0] == state[0]).all() for node in self.stack)
    
    

class QueueFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any((node.state[0] == state[0]).all() for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    
    def first(self):
        if self.empty():
            raise Exception("Empty Frontier")
        return self.frontier[0]
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            self.frontier = self.frontier[1:]
            
class Puzzle:
    def __init__(self, start, startIndex, goal, goalIndex):
        self.start = [start, startIndex]
        self.goal = [goal, goalIndex] 
        

    def neighbors(self, state):
        mat, (row, col) = state
        results = []
        if col > 0:
            mat1 = np.copy(mat)
            mat1[row][col] = mat1[row][col - 1]
            mat1[row][col - 1] = 0
            results.append(('left', [mat1, (row, col - 1)]))
        if row > 0:
            mat1 = np.copy(mat)
            mat1[row][col] = mat1[row - 1][col]
            mat1[row - 1][col] = 0
            results.append(('up', [mat1, (row - 1, col)]))
        if col < 2:
            mat1 = np.copy(mat)
            mat1[row][col] = mat1[row][col + 1]
            mat1[row][col + 1] = 0
            results.append(('right', [mat1, (row, col + 1)]))
        if row < 2:
            mat1 = np.copy(mat)
            mat1[row][col] = mat1[row + 1][col]
            mat1[row + 1][col] = 0
            results.append(('down', [mat1, (row + 1, col)]))
        
        return results
    

    def solve(self):
        start = Node(state=self.start, parent=None, action=None, level=0)
        frontier= QueueFrontier()
        stack= StackFrontier()
        frontier.add(start)
        stack.add(start)
        graph = pydot.Dot(graph_type='digraph', label="8 Puzzle State Space (BFS)", fontsize="30", color="red",
                      fontcolor="blue", style="filled", fillcolor="black")
        
        graph.add_node(start.graph_node)
        while  frontier.empty() ==False:
            
            if stack.contains_state(self.goal)==True:
                draw_legend(graph)
                graph.write_png("StateSpaceTree.png")
                for z in range(len(stack.stack)):
                    print(f"Level:- {stack.stack[z].level}")
                    print(f"Action: {stack.stack[z].action}")
                    print(f"{stack.stack[z].state[0]} ")
                    print()
                                                
                
                return
                # while True:
                    
                # 	x=int(input("enter level: "))

                    # for z in range(len(stack.stack)):
                    # 	if stack.stack[z].level==x:
                    # 		print(f"Level:- {x}")
                    # 		print(f"{stack.stack[z].state[0]} and {stack.stack[z].action}")
                    # 		print()
                                                
                    # print(f"Level={stack.stack[z].level}, {stack.stack[z].state} and {stack.stack[z].action}")
                    # print()
                # return
            u= frontier.first()
            
            
            # if u==self.start:
            # 	return
            for action, state in self.neighbors(u.state):
                if stack.contains_state(state)==False :
                    
                    child = Node(state=state, parent=u, action=action, level=u.level+1)
                    child.parent.update_color()
                    graph.add_node(child.graph_node)
                    graph.add_node(child.parent.graph_node)
                    if child.action=="left":
                        u.left=child
                    if child.action=="right":
                        u.right=child
                    if child.action=="up":
                        u.up=child
                    if child.action=="down":
                        u.down=child
                    graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node,label=child.action))
                    frontier.add(child)
                    stack.add(child)
                
            frontier.remove()

            



start = np.array([[2,8,3], [1,6,4], [7, 0,5]])
goal = np.array([[1,2,3],[8,0,4],[7,6,5]])


startIndex = (2, 1)
goalIndex = (0,1)

p = Puzzle(start, startIndex, goal, goalIndex)

p.solve()


