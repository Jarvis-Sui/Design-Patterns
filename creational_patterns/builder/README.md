# Intention

Some objects contain *raw* fields. When using them, these fields are further processed and different scenarios require different processingof these fields. But, how these fields construct an object is common among different scenarios.

For example, constructing a car requires many steps. One is to add seats. However, the number of seats vary among different cars (some cars contain 2 seats and some contain 4 seats). If constructing a car directly, we have to maintain too many car constructors. Instead of using numerous constructors, the builder pattern uses another object, a builder, that receives each initialization parameter step by step and then returns the resulting constructed object at once.

So, *builder pattern* allows us to keep the internal aggregation and build different representations. 

# Explanation of the example

We have a product, which contains two parts `a` and `b`. Different types of product require different processing of part `a` and `b`. Instead of creating different constructors, we create two builders `ConcreteBuilder1` and `ConcreteBuilder2`, which build and return a product. We also need a `Director` class, which is to accept a builder and calls the steps to build a product.

