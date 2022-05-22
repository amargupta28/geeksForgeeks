#User function Template for python3
from collections import OrderedDict
# design the class in the most optimal way

class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self,cap):
        #code here
        self.cap=cap
        self.cache=OrderedDict()
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
       if key not in self.cache:
           return -1
       else:
           self.cache.move_to_end(key)
           return self.cache[key]
            
        
        
    #Function for storing key-value pair.   
    def set(self, key, value):
        if key in self.cache:
            self.cache[key] =value
        else:
            if len(self.cache) >= self.cap:
                self.cache.popitem(last=False)
            self.cache[key]=value
        self.cache.move_to_end(key)
        
