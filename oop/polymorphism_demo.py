# class_static_methods_demo.py

class Calculator:
    # Class attribute shared by all instances
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: performs addition.
        It does not access or modify class or instance data.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: performs multiplication.
        It can access class-level attributes using 'cls'.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
