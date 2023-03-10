class DragManager():
    def __init__(self):
        self.edit_mode = False

    def add_dragable(self, widget):
        widget.bind("<ButtonPress-1>", self.on_start)
        widget.bind("<B1-Motion>", self.on_drag)
        widget.bind("<ButtonRelease-1>", self.on_drop)
        widget.configure(cursor="hand2")

    def on_start(self, event):
        # you could use this method to create a floating window
        # that represents what is being dragged.
        if (self.edit_mode):
            widget = event.widget
            widget.startX = event.x
            widget.startY = event.y 
            widget["state"] = "disable"

    def on_drag(self, event):
        # you could use this method to move a floating window that
        # represents what you're dragging
        if (self.edit_mode):
            widget = event.widget
            x = widget.winfo_x() - widget.startX + event.x
            y = widget.winfo_y() - widget.startY + event.y
            widget.place(x=x, y=y)

    def on_drop(self, event):
        # find the widget under the cursor
        if (self.edit_mode):
            x, y = event.widget.winfo_pointerxy()
            target = event.widget.winfo_containing(x, y)
            try:
                target.configure(image=event.widget.cget("image"))
                event.widget["state"] = "active"
            except:
                pass

    def change_edit_mode(self):
        if self.edit_mode == True:
            self.edit_mode = False
        else:
            self.edit_mode = True

    def editing_on(self):
        if self.edit_mode == True:
            return True
        else:
            return False