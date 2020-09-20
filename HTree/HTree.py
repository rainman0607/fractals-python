from drawingpanel import *


class HTree:
    def __init__(self, n):
        self.canvas = DrawingPanel(500, 500).canvas
        self.draw_htree(n)

    def draw_htree(self, n):
        self.draw_htree_helper(n, 200, 250, 250)

    def draw_h(self, size, x, y):
        self.canvas.create_line(x - size / 2, y - size / 2, x - size / 2, y + size / 2)  # l
        self.canvas.create_line(x - size / 2, y, x + size / 2, y)  # center
        self.canvas.create_line(x + size / 2, y - size / 2, x + size / 2, y + size / 2)  # r

    def draw_htree_helper(self, n, size, x, y):
        '''HTree is centered at (x,y)
        of height = width = size '''
        if n == 1:
            self.draw_h(size, x, y)
            return

        self.draw_h(size, x, y)

        self.draw_htree_helper(n - 1, size / 2, x - size / 2, y + size / 2)  # top left
        self.draw_htree_helper(n - 1, size / 2, x - size / 2, y - size / 2)  # bottom left
        self.draw_htree_helper(n - 1, size / 2, x + size / 2, y + size / 2)  # top right
        self.draw_htree_helper(n - 1, size / 2, x + size / 2, y - size / 2)


HTree(3)
