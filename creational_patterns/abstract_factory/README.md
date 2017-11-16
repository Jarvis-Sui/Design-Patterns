# Intention

The *factory pattern* is to hide instance creation and provide a central place to manage instance creation. By doing so, it is flexible to create instances for different scenarios.

If you have found that **"platform independence" and creation services are the current source of pain**, it's maybe the time to use *factory pattern*.

# Explanation of the example

In this example, we define several classes:

1. `AbstractFactory`
2. `ConcreteFactory1`
3. `ConcreteFactory2`
4. `AbstractProductA`
5. `ConcreteProductA`
5. `ConcreteProductA2`
6. `AbstractProductB`
7. `ConcreteProductB`
7. `ConcreteProductB2`

The scenario here is:

- we have different "platforms", aka, `ConcreteFactory1` and `ConcreteFactory2`
- different platforms require/provides different services, aka, `ConcreteProductA/B` and `ConcreteProductA2/B2`. 

see the code:

```python
    for factory in [ConcreteFactory1(), ConcreteFactory2()]:
        product_a = factory.create_product_a()
        product_b = factory.create_product_b()
        product_a.interface_a()
        product_b.interface_b()
```

It'll be messy if we create services (aka, ConcreteProduct) directly and pass platform info to the construtors and it requires a lot effort to maintain and modify if we're doing so. Instead, we use factory to hide the details of creating services. All the platform dependencies are handled in the factory.


# Check List

1. Decide if "platform independence" and creation services are the current source of pain.
2. Map out a matrix of "platforms" versus "products".
3. Define a factory interface that consists of a factory method per platform.
4. Define a factory derived class for each platform that encapsulates all references to the new operator.
5. The client should retire all references to new, and use the factory methods to create the product objects.
