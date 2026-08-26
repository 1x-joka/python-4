# Crie uma classe que represente um retângulo pelas suas medidas
# Retangulo: _base, _altura, _area, @base, @altura, @medidas, @area

class Retangulo():
    def __init__(self, base = 0, altura = 0):
        self._base = base
        self._altura = altura
        self._area = base * altura

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, nova_base):
        self._base = nova_base
        self._area = self._base * self._altura
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, nova_altura):
        self._altura = nova_altura
        self._area = self._base * self._altura

    @property
    def medidas(self):
        return self._base, self._altura
    
    @property
    def area(self):
        return self._area
    
retangulo = Retangulo(10, 5)

print(f'Base: {retangulo.base}')
print(f'Altura: {retangulo.altura}')
print(f'Medidas: {retangulo.medidas}')
print(f'Área: {retangulo.area}')

retangulo.base = 20
print(f'\nNova base: {retangulo.base}')
print(f'Nova área: {retangulo.area}')

retangulo.altura = 10
print(f'Nova altura: {retangulo.altura}')
print(f'Nova área: {retangulo.area}')