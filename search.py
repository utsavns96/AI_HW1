# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    "print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    #DFS uses Stack for a LIFO approach to managing the fringe
    fringestack=util.Stack()
    #We maintain a set of nodes that have been visited for a graph-search approach to DFS
    visitedlist = set()
    #adding the first node + moves to the stack. We have no moves that we have made yet, so we start with null
    #making this a tuple because push() takes only 1 argument
    fringestack.push((problem.getStartState(), []))
    
    while not fringestack.isEmpty():
        #get a new node from fringe
        currentnode = fringestack.pop()
        #currentnode[0]=(x,y); currentnode[1]=direction list
        #print("Now At: ", currentnode[0], currentnode[1])
        if (problem.isGoalState(currentnode[0])):
            return currentnode[1]
        else:
            #First we check if this node has been visited.
            if (currentnode[0] not in visitedlist):
            #if (currentnode0 not in visitedList):
                    #if this node has not been not visited, we mark it as visited by adding it to the set
                    visitedlist.add(currentnode[0])
                    #get the children of the node, iterate through them and add them to fringe
                    for child in problem.getSuccessors(currentnode[0]):
                        #child[0]=(x,y); child[1]=Direction; child[2]=cost
                        #print("child node= ", child[0], "dir= ", child[1])
                        #pushes new child node into fringe with (x,y), direction from start + direction
                        fringestack.push((child[0],currentnode[1]+[child[1]]))
    util.raiseNotDefined()
   
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #print(problem)
    #BFS uses Queue for a FIFO approach to managing the fringe
    fringequeue=util.Queue()
    #We maintain a set of nodes that have been visited for a graph-search approach to BFS
    visitedlist = set()
    #adding the first node + moves to the stack. We have no moves that we have made yet, so we start with null
    #making this a tuple because push() takes only 1 argument
    fringequeue.push((problem.getStartState(), []))
    
    while not fringequeue.isEmpty():
        #get a new node from fringe
        currentnode = fringequeue.pop()
        #currentnode[0]=(x,y); currentnode[1]=direction list
        #print("Now At: ", currentnode[0], currentnode[1])
        if (problem.isGoalState(currentnode[0])):
            return currentnode[1]
        else:
            #First we check if this node has been visited.
            #print (currentnode)
            if (currentnode[0] not in visitedlist):
                    #if this node has not been not visited, we mark it as visited by adding it to the set
                    visitedlist.add(currentnode[0])
                    #get the children of the node, iterate through them and add them to fringe
                    for child in problem.getSuccessors(currentnode[0]):
                        #child[0]=(x,y); child[1]=Direction; child[2]=cost
                        #print("child node= ", child[0], "dir= ", child[1])
                        #pushes new child node into fringe with (x,y), direction from start + direction
                        fringequeue.push((child[0],currentnode[1]+[child[1]]))

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #UCS uses a Priority queue for managing the fringe. THe priority is set by the cost.
    fringepq=util.PriorityQueue()
    #We maintain a set of nodes that have been visited for a graph-search approach to UCS
    visitedlist = set()
    #adding the first node + moves , priority(cost) to the stack. We have no moves that we have made yet, so we start with null
    #making this a tuple because push() takes only 1 argument
    fringepq.push((problem.getStartState(), []),0)
    while not fringepq.isEmpty():
        #get a new node from fringe
        currentnode = fringepq.pop()
        #currentnode[0]=(x,y); currentnode[1]=direction list; currentnode[2] = cost
        #print("Now At: ", currentnode)
        if (problem.isGoalState(currentnode[0])):
            #print("visitedlist", visitedlist)
            return currentnode[1]
        else:
            #First we check if this node has been visited.
            if (currentnode[0] not in visitedlist):
                    #if this node has not been not visited, we mark it as visited by adding it to the set
                    visitedlist.add(currentnode[0])
                    #print("visitedlist", visitedlist)
                    #get the children of the node, iterate through them and add them to fringe
                    for child in problem.getSuccessors(currentnode[0]):
                        #child[0]=(x,y); child[1]=Direction; child[2]=cost
                        #print("child node= ", child[0], "dir= ", child[1])
                        #pushes new child node into fringe with (x,y), direction from start + direction, with priority as the cost to get to this child from start
                        fringepq.push((child[0],currentnode[1]+[child[1]]),problem.getCostOfActions(currentnode[1]+[child[1]]))

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #A* uses a Priority queue to manage the fringe 
    fringepq=util.PriorityQueue()
    #We maintain a set of nodes that have been visited for a graph-search approach to A*
    visitedlist = set()
    #adding the first node + moves , priority(fcost) to the stack. We have no moves that we have made yet, so we start with null
    fringepq.push((problem.getStartState(), []),0)
    while not fringepq.isEmpty():
        #get a new node from fringe
        currentnode = fringepq.pop()
        #currentnode[0]=(x,y); currentnode[1]=direction list
        #print("Now At: ", currentnode)
        if (problem.isGoalState(currentnode[0])):
            return currentnode[1]
        else:
            #First we check if this node has been visited.
            if (currentnode[0] not in visitedlist):
                    #if this node has not been not visited, we mark it as visited by adding it to the set
                    visitedlist.add(currentnode[0])
                    #print("visitedlist", visitedlist)
                    #get the children of the node, iterate through them and add them to fringe
                    for child in problem.getSuccessors(currentnode[0]):
                        #child[0]=(x,y); child[1]=Direction; child[2]=cost
                        #print("child node= ", child[0], "dir= ", child[1])
                        #taking fcost as a variable to improve readability of code
                        fcost=problem.getCostOfActions(currentnode[1]+[child[1]])+heuristic(child[0],problem)
                        #pushes new child node into fringe with (x,y), direction from start + direction, priority = fcost
                        fringepq.push((child[0],currentnode[1]+[child[1]]),fcost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
