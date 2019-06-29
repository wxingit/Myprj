
class Node(object):
    '单个节点类'

    nodename = ""
    controlroot = None

    def __init__(self,inputcontrolroot,name):
        self.nodename = name
        self.__inputcount = 0
        self.__outputcount = 0
        self.controlroot = inputcontrolroot
        return

    def NodeOutPut(self):
        if self.controlroot.GetNodeState(self.nodename) == True:
            return self
        else:
            return None

