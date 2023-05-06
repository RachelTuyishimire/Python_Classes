class Fruit:
    category = "Fresh fruits"
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste
    
    def eat(self):
        return f"Christelle is eating a {self.color} {self.name}"
    
    def remove(self):
        return f"Joshua is removing the seeds of a {self.name}"
    
    def tastes(self):
        return f"Prince is eating a {self.taste} {self.name}"