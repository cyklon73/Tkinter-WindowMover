from tkinter import Tk, Widget

from vector import Vector2


class WindowMover:

    def __init__(self, root: Tk, widgets: list):
        self.root = root
        self.bind(root)
        for w in widgets:
            if issubclass(type(w), Widget):
                self.bind(w)
        self.fix_point: Vector2 = None
        self.overflow: Vector2 = Vector2()

    def bind(self, w):
        w.bind("<Motion>", self.mouse_move)
        w.bind("<Button-1>", self.mouse_click)
        w.bind("<ButtonRelease-1>", self.mouse_release)

    def mouse_vec(self) -> Vector2:
        x, y = self.root.winfo_pointerxy()
        return Vector2(x, y)

    def relativ_position(self) -> Vector2:
        x, y = self.overflow.num()
        return self.mouse_vec().add(x, y)

    def pressed(self) -> bool:
        return self.fix_point is not None

    def mouse_click(self, event):
        self.fix_point = self.mouse_vec()
        x, y = self.fix_point.num()
        self.overflow = Vector2(self.root.winfo_x(), self.root.winfo_y()).subtract(x, y)

    def mouse_release(self, event):
        self.fix_point = None

    def mouse_move(self, event):
        if self.pressed():
            x, y = self.relativ_position().num()
            self.root.geometry(f"+{x}+{y}")
