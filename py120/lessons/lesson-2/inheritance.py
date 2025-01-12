class Animal:
    def sleep(self):
        return 'sleeping!'
    
    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'


class Dog(Animal):
    def speak(self):
        return 'bark!'
    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'

class Cat(Animal):
     def speak(self):
        return 'meow!'

teddy = Bulldog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!
print(teddy.fetch())

ollie = Cat()
print(ollie.speak())

