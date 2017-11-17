# Indention

We may meet the following problems:

- How can objects be created so that which objects to create can be specified at run-time?
- How can dynamically loaded classes be instantiated?

We can create some prototypes in advance. When we need to "new" some object, we clone objects from the already created prototypes. However, this requires that we maintain prototypes and create them in advance.


# Explanation of the example

We creates two prototypes `ConcretePrototype1` and `ConcretePrototype2`, and use these two prototypes to create new objects.


# CheckList

1. Have one abstract prototype, which has an abstract method `clone()`
2. Have several concrete prototypes, which implement `clone()`
3. Use concrete prototypes to create objects