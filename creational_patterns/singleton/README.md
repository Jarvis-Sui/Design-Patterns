Singleton pattern is quite simple. When there should be exactly one object in use and all related operations are delegated to the object, you can use this pattern. 

However, it is easy to overuse this pattern. Sometimes a global variable or usual class is better.

Another problem along with singleton is to delete or destruct the singleton object. Since many objects may refer to the singleton object, deleting it may cause problems.