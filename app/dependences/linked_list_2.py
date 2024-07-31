class Node:
    def __init__(self, Value):
        self.Value = Value
        self.Next = None

    def __str__(self) -> str:
        return str(self.value)


class LinkedLlist:
    def __init__(self) -> None:
        self.First = None
        self.Size = 0

    #
    #
    #
    #
    def Append(self, Value):
        MyNode = Node(Value)
        if self.Size == 0:
            self.First = MyNode
        else:
            Current = self.First
            while Current.Next != None:
                Current = Current.Next
            Current.Next = MyNode
        self.Size += 1

    #
    #
    #
    #
    #
    #
    #
    #
    def Remove(self, Value):
        if self.Size == 0:
            return False
        else:
            Current = self.First
            while Current.Next.Value != Value:
                if Current.Next == None:
                    return False  # break loop and Remove returns False
                else:
                    Current = Current.Next
            DeletedNode = Current.Next
            Current.Next = DeletedNode.Next

        self.Size -= 1

        return DeletedNode

    def __length__(
        self,
    ):
        self.Size

    def __str__(self) -> str:
        String = "["
        Current = self.First
        while Current != None:
            String += str(Current)  # str(Current) execute __str__ of Current
            String += str(",")
            Current = Current.Next
        String += "]"

        return String
