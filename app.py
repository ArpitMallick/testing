import random

class GreetingGenerator:
    def __init__(self, greetings):
        self.greetings = greetings

    def generate_greeting(self):
        return random.choice(self.greetings)

class LanguageSelector:
    def __init__(self, languages):
        self.languages = languages

    def select_language(self):
        return random.choice(self.languages)

class HelloWorld:
    def __init__(self):
        self.greetings = ["Hello", "Bonjour", "Hola", "Ciao", "Hallo"]
        self.languages = ["English", "French", "Spanish", "Italian", "German"]
        self.greeting_generator = GreetingGenerator(self.greetings)
        self.language_selector = LanguageSelector(self.languages)

    def get_hello_world(self):
        greeting = self.greeting_generator.generate_greeting()
        language = self.language_selector.select_language()
        return f"{greeting}, World! ({language})"

def main():
    hello_world = HelloWorld()
    for _ in range(5):
        print(hello_world.get_hello_world())

if __name__ == "__main__":
    main()
