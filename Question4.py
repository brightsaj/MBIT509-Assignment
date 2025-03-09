# Define the Dog class
class Dog:
    def make_sound(self):
        return "Woof!"

# Define the Cat class
class Cat:
    def make_sound(self):
        return "Meow!"

# Define the process_sound function
def process_sound(sound_object):
    # The function doesn't need to know the specific type of sound_object
    # It just needs to know that it has a make_sound() method
    print(sound_object.make_sound())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Use the process_sound function with both Dog and Cat objects
process_sound(dog)  # Output: Woof!
process_sound(cat)  # Output: Meow!