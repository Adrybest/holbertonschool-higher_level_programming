#!/usr/bin/python3
"""Task 5: Dragon"""

class SwimMixin:

    def swim(self):
        print("The creature swims!")



class FlyMixin:

    def fly(self):
        print("The creature flies!")



class Dragon(SwimMixin, FlyMixin):

    def roar(self):
        print("The dragon roars!")

    def spit_fire(self):
        print("The dragon spits fire!")

    def observe(self):
        print("The dragon observes!")

    def attack(self):
        print("The dragon attacks!")
