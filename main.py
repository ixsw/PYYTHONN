class City:
    def __init__(self, name: str, population: int, area: float, country: str):
        self._name = name
        self._population = population
        self._area = area
        self._country = country

    def get_population_density(self) -> float:
        return self._population / self._area

    def display_info(self) -> None:
        print(f"City: {self._name}")
        print(f"Population: {self._population}")
        print(f"Area: {self._area} km^2")
        print(f"Country: {self._country}")

    def __str__(self) -> str:
        return f"{self._name}, {self._country}"


class District(City):
    def __init__(self, name: str, population: int, area: float, country: str):
        super().__init__(name, population, area, country)


class Arrondissement(City):
    def __init__(self, number: int, name: str, population: int, area: float, country: str):
        super().__init__(name, population, area, country)
        self._number = number  # Номер округа

    def __str__(self) -> str:
        return f"Arrondissement {self._number} ({self._name}): population - {self._population}"


# Примеры использования:
city1 = City("Paris", 2148000, 105.4, "France")
city1.display_info()
print("Population density:", city1.get_population_density())

arrondissement_1 = Arrondissement(1, "Louvre", 16537, 10.4, "France")
arrondissement_2 = Arrondissement(2, "Bois de Boulogne", 20164, 8.6, "France")
arrondissement_3 = Arrondissement(3, "Temple", 35401, 12.2, "France")

print(arrondissement_1)
print(arrondissement_2)
print(arrondissement_3)

district1 = District("Antony", 61000, 12.8, "France")
district2 = District("Clichy", 61000, 3.1, "France")
district3 = District("Drancy", 72000, 7.8, "France")

print(district1)
print(district2)
print(district3)
