# class_static_methods_demo.py

class Calculator:
    # Class attribute shared by all instances and accessible through cls
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method:
        Performs addition of two numbers.
        Does not require access to class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method:
        Performs multiplication of two numbers.
        Has access to the class (via cls) and can use class-level attributes.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
