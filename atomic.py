#!/usr/bin/env python
class Subshell:
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

class Atom:
    def __init__(self, atomic_number, name=None):
        self.atomic_number = atomic_number
        self.name = name
        self.electron_configuration = self.stable_electrons

    @staticmethod
    def generate_configurations():
        for n, subshell in ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p"]:
            for position in Subshell(int(n), subshell):
                yield position

    @property
    def stable_electrons(self):
        return "123"


if __name__ == "__main__":
    configurations = Atom.generate_configurations()
    print([ str(c) for c in configurations ])
    
    atomic_number = int(input("Enter atomic number: "))
    atom = Atom(atomic_number)
    print(atom.stable_electrons)
