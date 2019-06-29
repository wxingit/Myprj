from node import Node


class Controlnode(object):
    '控制节点'

    _nodelist = {}
    _resource = {}

    def __init__(self):
        pass

    def _nodeadd(self, inputobj):
        self._nodelist.update({inputobj : False})

    def _nodedel(self,delobj):
        self._nodelist.__delitem__(delobj)

    def _changenodestate(self, inputobj,controlvalue):
        self._nodelist[inputobj] = controlvalue

    def getnodestate(self,inputobj):
        if inputobj in self._nodelist:
            return self._nodelist[inputobj]
        else:
            return None

    def inputresource(self,inputresourceobj):
        resourcenode = Node(self,inputresourceobj)
        self._nodeadd(resourcenode)
        pass

    def delresource(self,delresourceobj):
        self._nodedel(delresourceobj)
        pass
