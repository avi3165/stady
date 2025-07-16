import random


class Animal:
    def __init__(self,color,typeof_d,n_o_f_a_b,n_o_l):
        self.color = color
        self.type_of_digestive_system=typeof_d
        self.Number_of_fetuses_at_birth=n_o_f_a_b
        self.number_of_legs = n_o_l

    def add_tail(self,tail):
        self.tail = tail
class Tail:
    def __init__(self,len,speed,ovi):
        self.len=len
        self.speed=speed
        self.ovi=ovi
class Cat(Animal):

    def __init__(self,color,len_whisker):
        super().__init__(color,"normal",5,4)
        self.counter_mouse = 0
        self.len_whisker=len_whisker
    def get_hunted_mice(self):
        return f"you hunted {self.counter_mouse} mice"
    def hunt_mouse(self):
        self.counter_mouse+=1
        return "go hunt mouse"

mitzi = Cat("red",1)
print(mitzi.hunt_mouse())
print(mitzi.get_hunted_mice())