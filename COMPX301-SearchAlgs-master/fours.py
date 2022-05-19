import mathexpressions


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


class State:
    parser = mathexpressions.Parser()
    goalNum = 0
    expressionString = "4"

    def __init__(self, goalNum, expressionString="4"):
        self.goalNum = goalNum
        self.expressionString = expressionString

    def eval(self):
        self.parser.parse_function(self.expressionString)
        if self.parser.calc_function() == self.goalNum:
            return True
        else:
            return False

    def expand(self):
        return [
            State(self.goalNum, self.expressionString + "+4"),
            State(self.goalNum, self.expressionString + "-4"),
            State(self.goalNum, self.expressionString + "*4"),
            State(self.goalNum, self.expressionString + "/4"),
            State(self.goalNum, self.expressionString + "^4"),
            State(self.goalNum, self.expressionString + "4"),
            State(self.goalNum, self.expressionString + ".4"),
            State(self.goalNum, "(" + self.expressionString + ")"),
        ]


def search(n: int) -> str:

    # BFS, therefore queue frontier
    frontier = Queue()

    # initial state
    print("input n: " + str(n))
    frontier.enqueue(State(n))

    # while there's still a frontier to explore...
    print("beginning frontier traversal")
    while frontier.size() > 0:
        currentState = frontier.dequeue()

        try:

            if currentState.eval() == True:
                return currentState.expressionString
            else:
                childStates = currentState.expand()
                for state in childStates:
                    frontier.enqueue(state)
        except Exception as e:
            # print("invalid state discarded: " + currentState.expressionString)
            pass


def main():
    print("answer: " + str(search(int(input()))))


main()
