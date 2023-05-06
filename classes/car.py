class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.year = year
    
    def get_make(self):
        return f"Rachel owns a black {self.make}"
    
    def get_model(self):
        return f"Its model is {self.model}"
    
    def get_year(self):
        return f"I {self.make} I am of model {self.model} and I am of year {self.year}"
    
    def drive(self):
        return f"Rachel drives a grey {self.make} which is {self.model} of {self.year}"