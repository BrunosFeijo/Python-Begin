from enum import Enum


class Pais(Enum):
    BRASIL = 'Brasil'
    EUA = 'Estados Unidos'
    CANADA = 'Canada'
    ARGENTINA = 'Argentina'
    ESPANHA = 'Espanha'
    ALEMANHA = 'Alemanha'

    def __str__(self):
        return f'{self.value}'
