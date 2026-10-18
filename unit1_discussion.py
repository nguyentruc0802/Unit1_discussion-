"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class SmartDevice:
    # Class variable (Shared by all devices in the ecosystem)
    ecosystem_version = "v2.4"

    def __init__(self, device_id, brand):
        # Instance variables (Specific to each device)
        self.device_id = device_id
        self.brand = brand

    def get_status(self):
        """Returns information about the device status."""
        return f"ID: {self.device_id}, Brand: {self.brand}, Ecosystem: {self.ecosystem_version}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class SmartThermostat(SmartDevice):
    # New class variable
    device_type = "Climate Control"

    def __init__(self, device_id, brand, target_temp, schedule_zones=None):
        # Calling the constructor of the parent class
        super().__init__(device_id, brand)
        # Two new instance variables (including a nested mutable list for climate zones)
        self.target_temp = target_temp
        self.schedule_zones = schedule_zones if schedule_zones is not None else []

    # New method
    def adjust_temperature(self, degrees):
        self.target_temp += degrees
        return f"Temperature adjusted by {degrees}°F. New target: {self.target_temp}°F."

    # Overridden method from the parent class (Method Overriding)
    def get_status(self):
        base_status = super().get_status()
        return f"{base_status}, Type: {self.device_type}, Target: {self.target_temp}°F, Zones: {self.schedule_zones}"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    # 1. Create two objects of the child class (Temperatures in Fahrenheit)
    thermostat1 = SmartThermostat("TH-101", "Nest", 71.0)
    thermostat2 = SmartThermostat("TH-102", "Ecobee", 72.5)

    # 2. Access a class variable through the class itself
    print(f"Class variable via class: {SmartThermostat.device_type}")

    # 3. Access the same class variable through an object
    print(f"Class variable via object (thermostat1): {thermostat1.device_type}")

    # 4. Add a new attribute to only ONE object after it is created
    thermostat1.firmware_patch = "2026.10"
    print(f"\n[Info] Dynamic attribute 'firmware_patch' added to thermostat1.")

    # 5. Display instance namespaces using __dict__
    print(f"Namespace of thermostat1: {thermostat1.__dict__}")  # Contains 'firmware_patch'
    print(f"Namespace of thermostat2: {thermostat2.__dict__}")  # Does not contain 'firmware_patch'

    # 6. Display class namespace information
    print(f"\nClass Namespace (Excerpt):")
    for key, value in SmartThermostat.__dict__.items():
        if not key.startswith('__'):  # Filters out built-in attributes for better readability
            print(f"  {key}: {value}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    # 1. Create an object with nested mutable data (the list 'schedule_zones')
    original_device = SmartThermostat("TH-200", "Honeywell", 68.0, ["Living Room", "Kitchen"])

    # 2. Create a shallow copy
    shallow_device = copy(original_device)

    # 3. Create a deep copy
    deep_device = deepcopy(original_device)

    # 4. Modify the original object's nested data
    original_device.schedule_zones.append("Bedroom")
    original_device.device_id = "TH-MODIFIED"  # Also changes a top-level attribute for demonstration

    # 5. Display the results
    print(f"Original (modified): {original_device.get_status()}")
    print(f"Shallow Copy:        {shallow_device.get_status()}")
    print(f"Deep Copy:           {deep_device.get_status()}")

    """
    EXPLANATION OF COPYING BEHAVIOR:
    - Shallow Copy (copy): Creates a new top-level object but only copies references 
      to the nested objects inside it. Since 'schedule_zones' is a list (mutable), 
      the original and the shallow copy share the exact same list reference. This is why 
      "Bedroom" appears in 'shallow_device' too. However, the top-level attribute 'device_id' 
      was independent, which is why 'shallow_device' still has "TH-200".

    - Deep Copy (deepcopy): Copies the top-level object AND recursively creates real, 
      independent copies of all nested objects. 'deep_dog' remains completely unaffected 
      by any changes made to 'original_device'.
    """


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n--- Testing Parent Object ---")
    # Create and test an object of the parent class
    basic_hub = SmartDevice("HUB-01", "Samsung")
    print(basic_hub.get_status())

    print("\n--- Testing Child Object ---")
    # Create and test an object of the child class
    living_room_thermostat = SmartThermostat("TH-555", "Bosch", 66.0, ["Basement"])
    print(living_room_thermostat.get_status())
    # Demonstrating inheritance and new methods
    print(living_room_thermostat.adjust_temperature(4.0))

    # Call the demonstration functions
    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()