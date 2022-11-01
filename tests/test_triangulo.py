import src.triangulo.triangulo as triangulo

class Testclass:
    def test_triangulo1(self):
        assert triangulo.triangulo(1,2,3) == "não é um triangulo"
    def test_triangulo2(self):
        assert triangulo.triangulo(0,0,0) == "não é um triangulo"
    def test_triangulo3(self):
        assert triangulo.triangulo(3,5,6) == "é um triangulo"
    def test_triangulo4(self):
        assert triangulo.triangulo(5,5,15) == "não é um triangulo"