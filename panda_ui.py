from direct.showbase.ShowBase import ShowBase
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
        vertexData = GeomVertexData("data", vertexFormat, Geom.UHStatic)
        vertexData.setNumRows(4)
        vertexWriter = GeomVertexWriter(vertexData, "vertex")
        colorWriter = GeomVertexWriter(vertexData, "color")
        vertexWriter.addData3f(-1, 0, -1)
        colorWriter.addData4f(1.0, 0.0, 0.0, 1.0)
        vertexWriter.addData3f(-1, 0, 1)
        colorWriter.addData4f(0.0, 1.0, 0.0, 1.0)
        vertexWriter.addData3f(1, 0, 1)
        colorWriter.addData4f(0.0, 0.0, 1.0, 1.0)
        vertexWriter.addData3f(1, 0, -1)
        colorWriter.addData4f(1.0, 0.0, 1.0, 1.0)
        geometry = Geom(vertexData)
        points = GeomPoints(Geom.UHStatic)
        points.addVertices(0, 1, 2, 3)
        geometry.addPrimitive(points)
        node = GeomNode("node")
        node.addGeom(geometry)
        self.nodePath = NodePath(node)
        self.nodePath.setPos(0, 0, 0)
        self.nodePath.setRenderModeThickness(10.0)
        self.camera.setPos(0.0, -10.0, 0.0)
        self.disableMouse()
        self.nodePath.reparentTo(self.render)

def main():
    application = Application()
    application.run()
