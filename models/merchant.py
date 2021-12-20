class Merchant:
    def __init__(self, name, active = True):
        self.name = name
        self.active = active
    
    def toggle_active(self):
        self.active = not self.active