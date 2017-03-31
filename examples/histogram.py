"""
 Shows an histogram window

"""
import random
from pylibui.core import App
from pylibui.controls import *
from pylibui import libui

histogram = None

class MyWindow(Window):

    def onClose(self, data):
        super().onClose(data)
        app.stop()

class MySpinBox(Spinbox):

    def onChanged(self, data):
        super().onChanged(data)
        histogram.redrawAll()

class MyColorButton(ColorButton):

    def onColorChanged(self, data):
        super().onColorChanged(data)
        histogram.redrawAll()

class MyArea(Area):
    def __init__(self):
        super().__init__(MyAreaHandler())

xoffLeft = 20
yoffTop = 20
xoffRight = 20
yoffBottom = 20
pointRadius = 5

colorButton = None
datapoints = []
currentPoint = -1

def graphSize(clientWidth, clientHeight):
    return (clientWidth - xoffLeft - xoffRight,
                clientHeight - yoffTop - yoffBottom)

def inPoint(x, y, xtest, ytest):
    # TODO switch to using a matrix
    x -= xoffLeft
    y -= yoffTop

    return ((x >= xtest - pointRadius) and
                (x <= xtest + pointRadius) and
                (y >= ytest - pointRadius) and
                (y <= ytest + pointRadius))

def pointLocations(width, height):
    xincr, yincr = float(width) / 9, float(height) / 100

    i = 0
    xs = []
    ys = []
    for spinbox in datapoints:
        n = 100 - spinbox.getValue()

        xs.append(xincr * i)
        ys.append(yincr * n)

        i += 1

    return xs, ys

def constructGraph(width, height, extend):
    xs, ys = pointLocations(width, height)
    path = libui.uiDrawNewPath(libui.uiDrawFillModeWinding)

    libui.uiDrawPathNewFigure(path, xs[0], ys[0])

    for i in range(1, 10):
        libui.uiDrawPathLineTo(path, xs[i], ys[i])

    if extend:
        libui.uiDrawPathLineTo(path, width, height);
        libui.uiDrawPathLineTo(path, 0, height);
        libui.uiDrawPathCloseFigure(path);

    libui.uiDrawPathEnd(path)

    return path

class MyAreaHandler(AreaHandler):
    def onDraw(self, a, params):
        brush = libui.uiDrawBrush()
        brush.R = 1.0
        brush.G = 1.0
        brush.B = 1.0
        brush.A = 1.0

        path = libui.uiDrawNewPath(libui.uiDrawFillModeWinding)
        libui.uiDrawPathAddRectangle(path, 0, 0,
                                         params.AreaWidth,
                                         params.AreaHeight)
        libui.uiDrawPathEnd(path)
        libui.uiDrawFill(params.Context, path, brush)
        libui.uiDrawFreePath(path)

        graphWidth, graphHeight = graphSize(params.AreaWidth,
                                                params.AreaHeight)

        sp = libui.uiDrawStrokeParams()
        # make a stroke for both the axes and the histogram line
        sp.Cap = libui.uiDrawLineCapFlat
        sp.Join = libui.uiDrawLineJoinMiter
        sp.Thickness = 2
        sp.MiterLimit = libui.uiDrawDefaultMiterLimit
        
        brush.R = 0.0
        brush.G = 0.0
        brush.B = 0.0
        brush.A = 1.0
        
        path = libui.uiDrawNewPath(libui.uiDrawFillModeWinding)
        libui.uiDrawPathNewFigure(path,
                                xoffLeft, yoffTop)
        libui.uiDrawPathLineTo(path,
                             xoffLeft, yoffTop + graphHeight)
        libui.uiDrawPathLineTo(path,
                             xoffLeft + graphWidth, yoffTop + graphHeight)
        libui.uiDrawPathEnd(path)
        libui.uiDrawStroke(params.Context, path, brush, sp)
        libui.uiDrawFreePath(path)

        #now transform the coordinate space so (0, 0) is the top-left corner of the graph
        m = libui.uiDrawMatrix()
        libui.uiDrawMatrixSetIdentity(m)
        libui.uiDrawMatrixTranslate(m, xoffLeft, yoffTop)
        libui.uiDrawTransform(params.Context, m)

        # now get the color for the graph itself and set up the brush
        graphR, graphG, graphB, graphA = colorButton.getColor();
        brush.Type = libui.uiDrawBrushTypeSolid;
        brush.R = graphR;
        brush.G = graphG;
        brush.B = graphB;
        # we set brush->A below to different values for the fill and stroke

        #now create the fill for the graph below the graph line
        path = constructGraph(graphWidth, graphHeight, True);
        brush.A = graphA / 2;
        libui.uiDrawFill(params.Context, path, brush);
        libui.uiDrawFreePath(path);

        # now draw the histogram line
        path = constructGraph(graphWidth, graphHeight, False);
        brush.A = graphA;
        libui.uiDrawStroke(params.Context, path, brush, sp);
        libui.uiDrawFreePath(path);
        
        # now draw the point being hovered over
        for i in range(10):
            xs, ys = pointLocations(graphWidth, graphHeight)
            path = libui.uiDrawNewPath(libui.uiDrawFillModeWinding)
            libui.uiDrawPathNewFigureWithArc(path,
                xs[i], ys[i],
                pointRadius,
                0, 6.23, # TODO pi
                0)
            libui.uiDrawPathEnd(path)
                # use the same brush as for the histogram lines
            libui.uiDrawFill(params.Context, path, brush)
            libui.uiDrawFreePath(path)
        if currentPoint != -1:
            brush.R = 1.0;
            brush.G = 0.0;
            brush.B = 0.0;
            xs, ys = pointLocations(graphWidth, graphHeight)
            path = libui.uiDrawNewPath(libui.uiDrawFillModeWinding)
            libui.uiDrawPathNewFigureWithArc(path,
                xs[currentPoint], ys[currentPoint],
                pointRadius,
                0, 6.23, # TODO pi
                0)
            libui.uiDrawPathEnd(path)
                # use the same brush as for the histogram lines
            libui.uiDrawFill(params.Context, path, brush)
            libui.uiDrawFreePath(path)

    def onMouseEvent(self, area, e):
        graphWidth, graphHeight = graphSize(e.AreaWidth, e.AreaHeight)
        xs, ys = pointLocations(graphWidth, graphHeight)

        found = -1
        for i in range(10):
            if inPoint(e.X, e.Y, xs[i], ys[i]):
                found = i
                break

        global currentPoint
        currentPoint = found
        
        #TODO only redraw the relevant area
        area.redrawAll()
        
app = App()

window = MyWindow('pylibui Histogram Example', 640, 480)
window.setMargined(True)

hbox = HorizontalBox()
hbox.setPadded(1)
window.setChild(hbox)

vbox = VerticalBox()
vbox.setPadded(1)
hbox.append(vbox)

for i in range(10):
    spinbox = MySpinBox(0, 100)
    spinbox.setValue(random.randint(0, 100))
    datapoints.append(spinbox)
    vbox.append(spinbox)

colorButton = MyColorButton()
colorButton.setColor((float(0x1E) / 255, float(0x90) / 255, float(0xFF) / 255, 1))
vbox.append(colorButton)

histogram = MyArea()
hbox.append(histogram, True)

window.show()

app.start()
app.close()
