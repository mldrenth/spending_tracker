class Tag:
    def __init__(self, name, active = True, id = None):
        self.name = name
        self.active = active
        self.id = id
    
    def toggle_active(self):
        self.active = not self.active