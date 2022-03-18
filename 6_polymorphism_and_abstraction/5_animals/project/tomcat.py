from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")
        self.sound = "Hiss"

    def make_sound(self):
        return self.sound
