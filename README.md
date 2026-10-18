Unit1_discussion

This assignment explores object-oriented programming (OOP) concepts in Python, including inheritance, namespaces, and object copying

Learning Objectives

- Create parent and child classes
- Use inheritance to extend functionality
- Understand class and instance namespaces
- Demonstrate shallow and deep copying
- Apply object-oriented design principles

Requirements

Complete all TODO sections in the source code:

1. Create a parent class.
2. Create a child class using inheritance.
3. Demonstrate class and instance namespaces.
4. Demonstrate shallow and deep copying.
5. Create and test objects in `main()`.
6. Add a student-created extension.

Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Compare OOP to procedural programming.
4. Discuss the benefits of maintainability and reusability and apply this managing overhead, practical application development, and future use.

Reflection

Completing this smart-home ecosystem assignment deepened my understanding of object-oriented programming (OOP) in Python. I mastered method overriding and the use of super().__init__()to extend parent class constructors. Visualizing namespaces through __dict__clarified how Python dynamically manages class and instance attributes. Additionally, I learned the critical difference between shallow and deep copying when dealing with mutable nested data like sensor zone lists.
My primary challenge was managing how nested lists behave during a shallow copy. I initially expected the copied object to be completely isolated, but modifying the original list inadvertently altered the copy. I overcame this by studying the copymodule and implementing deepcopyto create recursive, independent object duplicates.
Compared to procedural programming , which structures code linearly around top-down functions, OOP groups data and behaviors into cohesive objects. This provides massive benefits for reusability and maintainability . In practical application development, if a new smart device needs to be added, I can simply inherit from SmartDeviceinstead of rewriting basic setup code. This lowers future development overhead, simplifies debugging, and ensures scalable future use.
