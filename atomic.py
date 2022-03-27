#!/usr/bin/env python
class Subshell:
    all_subshells = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p"]
    capacities = { "s": 2, "p": 6, "d": 10, "f": 14 }
    def __init__(self, n, subshell):
        self.n = n
        self.subshell = subshell
        self.capacity = Subshell.capacities[self.subshell]

    def __str__(self):
        return f"{self.n}{self.subshell}{self.capacity}"

    def __iter__(self):
        for exp in range(1, self.capacity+1):
            yield f"{self.n}{self.subshell}{exp}"

    @staticmethod
    def get_all_locations():
        for n, subshell in Subshell.all_subshells:
            for position in Subshell(int(n), subshell):
                yield position

class Atom:
    def __init__(self, atomic_number, name=None):
        self.atomic_number = self.free_electrons = atomic_number
        self.name = name
        self.electron_configuration = []
        self.restabilize_electrons()

    def restabilize_electrons(self):
        free_electrons = self.atomic_number
        self.electron_configuration = []

        for location in Subshell.get_all_locations():
            self.add_electron(location)
            if not self.free_electrons:
                return

    def add_electron(self, location):
        self.electron_configuration.append(location)
        self.free_electrons -= 1

if __name__ == "__main__":
    configurations = Subshell.get_all_locations()
    print(list(configurations))
    
    atomic_number = int(input("Enter atomic number: "))
    atom = Atom(atomic_number)
    print(atom.electron_configuration)
