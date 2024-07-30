class Node:
    def __init__(self, value: int, nextNode: "Node" = None) -> None:
        self.value = value
        self.nextNode = nextNode


class LinkedList:
    def __init__(self) -> None:
        self._size = 0
        self._firstNode = None

    ##
    ##
    ##
    ##
    ##
    ##
    def add(self, position: int, element: int):
        newNode = Node(value=element)

        # Add at the beginning
        if position == 0:
            newNode.nextNode = self._firstNode
            self._firstNode = newNode

        # Add at a specific position
        else:
            currentNode = self._firstNode
            for _ in range(position - 1):
                if currentNode is None:
                    raise IndexError("Position out of bounds")
                currentNode = currentNode.nextNode

            newNode.nextNode = currentNode.nextNode
            currentNode.nextNode = newNode

        self._size += 1

    ##
    ##
    ##
    ##
    ##
    ##
    def delete(self, position: int):
        if position < 0 or position >= self._size:
            raise IndexError("Position out of bounds")

        # Delete the first node
        if position == 0:
            self._firstNode = self._firstNode.nextNode

        # Delete a node at a specific position
        else:
            currentNode = self._firstNode
            for _ in range(position - 1):
                currentNode = currentNode.nextNode

            currentNode.nextNode = currentNode.nextNode.nextNode

        self._size -= 1

    def print_list(self):
        currentNode = self._firstNode
        while currentNode is not None:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.nextNode
        print("None")
