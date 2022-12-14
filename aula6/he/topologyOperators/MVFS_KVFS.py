from he.dataStructure.vertex import Vertex
from he.dataStructure.face import Face
from he.dataStructure.shell import Shell
from he.dataStructure.halfedge import HalfEdge
from he.dataStructure.loop import Loop
from geometry.patch import Patch


# MakeVertexFaceShell class declaration
class MVFS:
    def __init__(self, point, vertex=None, face=None):

        if point is not None:
            self.shell = Shell()
            self.face = Face(self.shell)
            self.face.patch = Patch()
            self.vertex = Vertex(point)
        else:
            self.vertex = vertex
            self.face = face

    def name(self):
        return 'MVFS'

    def execute(self):

        #print('------------- MVFS -------------------')

        # create topological entities
        he = HalfEdge(self.vertex)
        loop_out = Loop(self.face)
        new_loop = Loop(self.face, he)

        # set parameters
        self.vertex.he = he
        shell = self.face.shell
        shell.face = self.face
        he.loop = new_loop
        he.prev = he
        he.next = he

    def unexecute(self):
        kvfs = KVFS(self.vertex, self.face)
        kvfs.execute()


# KillVertexFaceShell class declaration
class KVFS:
    def __init__(self, vertex, face):
        self.vertex = vertex
        self.face = face

    def name(self):
        return 'KVFS'

    def execute(self):

        #print('------------- KVFS -------------------')

        loop_out = self.face.loop
        loop = loop_out.next
        he = self.vertex.he

        self.vertex.he = None
        self.face.loop = None

        self.face.shell.delete()
        self.face.delete()
        self.vertex.delete()
        loop.delete()
        loop_out.delete()
        he.delete()
        del he

    def unexecute(self):
        mvfs = MVFS(None, self.vertex, self.face)
        mvfs.execute()
