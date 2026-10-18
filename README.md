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

Working through this project really helped me wrap my head around object-oriented programming. It was cool to see how super().__init__()passes data up to the parent class, and using __dict__it made it click how Python actually tracks variables behind the scenes. The biggest eye-opener, though, was learning how shallow and deep copying work when dealing with lists inside an object.
My main roadblock was definitely the shallow copy. I thought copying an object meant it was completely independent. When I modified a temperature zone in the original object and saw it change in the copy too, I was so confused. It took some digging into Python's copy modules to realize they were still sharing the same list. Switching to deep copy fixed it by forcing a full, independent clone.
If I look at procedural programming—where you just have a long list of functions—OOP feels much cleaner. It data groups and logic where they belong. For real-world apps, this is a lifesaver for maintainability. If I want to add a smart light bulb tomorrow, I don't have to rewrite everything from scratch; I just inherited from SmartDevice. It saves a ton of time and keeps the code ready for whatever comes next.
