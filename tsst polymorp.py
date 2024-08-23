class Polygon:
    def noofsides(self):
        print("unknown")
class triangle(Polygon):
    def noofsides(self):
        print("sides equal 3")
class quad(Polygon):
    def noofsides(self):
        print("sides equal 4")
class penta(Polygon):
    pass
class hexagon(Polygon):
    def noofsides(self):
        print("sides equal 6")

shapes = [triangle(), quad(), penta(), hexagon()]
for i in shapes:
    i.noofsides()