from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from panda3d.core import Geom
from panda3d.core import GeomNode
from panda3d.core import GeomPoints
from panda3d.core import GeomVertexData
from panda3d.core import GeomVertexFormat
from panda3d.core import GeomVertexWriter
from panda3d.core import NodePath

class UI(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        vertexFormat = GeomVertexFormat.getV3c4()
        self.vertexData = GeomVertexData("data", vertexFormat, Geom.UHDynamic)
        geometry = Geom(self.vertexData)
        self.primitive = GeomPoints(Geom.UHDynamic)
        geometry.addPrimitive(self.primitive)
        node = GeomNode("node")
        node.addGeom(geometry)
        self.nodePath = NodePath(node)
        self.nodePath.setPos(0, 0, 0)
        self.nodePath.setRenderModeThickness(10.0)
        self.camera.setPos(0.0, -10.0, 0.0)
        self.disableMouse()
        self.nodePath.reparentTo(self.render)

    def add_task(self, task):
        def task_wrapper(taskObject):
            task()
            return Task.cont
        self.taskMgr.add(task_wrapper)

    def set_points(self, position, color):
        assert len(position) == len(color)
        self.vertexData.setNumRows(len(position))
        self.primitive.clearVertices()
        for i in range(len(position)):
            self.primitive.addVertex(i)
        self.primitive.closePrimitive()
        positionWriter = GeomVertexWriter(self.vertexData, "vertex")
        colorWriter = GeomVertexWriter(self.vertexData, "color")
        for p, c in zip(position, color):
            positionWriter.addData3f(p[0], p[1], p[2])
            colorWriter.addData4f(c[0], c[1], c[2], c[3])

def main():

    application = Application()
    application.run()
