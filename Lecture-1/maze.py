import sys


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __int__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1] # Finding the node
            self.frontier = self.frontier[:-1] # Removing the node by creating a new list from previous list
            return node
        
class QueueFrontier(StackFrontier): # "(StackFrontier)" means it inherits from the StackFrontier

    def remove(self): # Overloading
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

def solve(self):
    # Finds solution to maze

    # keeps track of states explored:
    self.num_explored = 0

    # intialize the frontier to just the staring point;
    start = Node(state=self.start, parent=None, action=None)
    frontier = StackFrontier()
    frontier.add(start)

    # intialize an empty explored set:
    self.explored = set()

    # keep looping until solution is found:
    while True:
        if frontier.empty():
            raise Exception('no solution')

        node = frontier.remove()
        self.num_explored += 1

        if node.state == self.goal:
            actions = []
            cells = []

            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
            actions.reverse()
            cells.reverse()
            self.solution = (actions, cells)
            return

        self 