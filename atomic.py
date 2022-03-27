#!/usr/bin/env python
class Position:
    def __init__(self, subshell, exponent):
        self.subshell = subshell
        self.exponent = exponent

    def __str__(self):
        return f"{self.subshell}{self.exponent}"


class Subshell:
    all_subshells = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p"]
    capacities = { "s": 2, "p": 6, "d": 10, "f": 14 }
    def __init__(self, n, subshell):
        self.n = n
        self.subshell = subshell
        self.capacity = Subshell.capacities[self.subshell]

    def __str__(self):
        return f"{self.n}{self.subshell}"

    def __iter__(self):
        for exp in range(1, self.capacity+1):
            yield Position(self, exp)

    @staticmethod
    def get_all():
        for n, subshell in Subshell.all_subshells:
            yield Subshell(int(n), subshell)


class Atom:
    def __init__(self, atomic_number, name="Atom"):
        self.atomic_number = self.free_electrons = atomic_number
        self.name = name
        self.electron_configuration = []
        self.restabilize_electrons()

    def restabilize_electrons(self):
        self.free_electrons = self.atomic_number
        self.electron_configuration = []

        for subshell in Subshell.get_all():
            if self.free_electrons <= subshell.capacity:
                for location in subshell:
                    self.add_electron(location)
                    if not self.free_electrons:
                        return
            else:
                self.add_subshell(subshell)
                if not self.free_electrons:
                    return


    def add_electron(self, location):
        # print(f"Adding {location}, removing 1 from {self.free_electrons}")
        self.electron_configuration.append(location)
        self.free_electrons -= 1
        
    def add_subshell(self, subshell):
        # print(f"Adding {subshell}, removing {subshell.capacity} from {self.free_electrons}")
        self.electron_configuration.append(subshell)
        self.free_electrons -= subshell.capacity

    def __str__(self):
        return f"{self.name} (" + ", ".join(str(cf) for cf in self.electron_configuration) + ")"

if __name__ == "__main__":
    #configurations = Subshell.get_all_locations()
    #print(list(configurations))
    
    atomic_number = int(input("Enter atomic number: "))
    atom = Atom(atomic_number)
    print(atom)
