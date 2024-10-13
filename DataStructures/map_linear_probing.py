from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me

def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(int(num_elements / load_factor))
  
    scale = 1  
    shift = 0  
    
    table = [None] * capacity
    map_linear_probing = {
        'prime': prime,               
        'capacity': capacity,           
        'scale': scale,                 
        'shift': shift,                
        'table': table,              
        'current_factor': 0,           
        'limit_factor': load_factor,     
        'size': 0,                       
        'type': 'PROBING'               
    }
    
    return map_linear_probing


def put(my_map, key, value):
    index = mf.hash_value(my_map, key)
    capacity = my_map['capacity']
    table = my_map['table']
    entry = me.new_map_entry(key, value)
    
    for i in range(capacity):
        probing_index = (index + i) % capacity 
        current_entry = table[probing_index]
        
      
        if current_entry is None:
            table[probing_index] = entry
            my_map['size'] += 1
            my_map['current_factor'] = my_map['size'] / my_map['capacity']  
            return my_map
    
        elif me.get_key(current_entry) == key:
            table[probing_index] = me.set_value(current_entry, value)
            return my_map


def contains(my_map, key):
    index = mf.hash_value(my_map, key)
    capacity = my_map['capacity']
    table = my_map['table']
    
    for i in range(capacity):
        probing_index = (index + i) % capacity 
        current_entry = table[probing_index]
        if current_entry is None:
            continue 
      
        elif me.get_key(current_entry) == key:
            return True
  
    return False
  
def get(my_map, key):
    index = mf.hash_value(my_map, key)
    capacity = my_map['capacity']
    table = my_map['table']
    
    for i in range(capacity):
        probing_index = (index + i) % capacity 
        current_entry = table[probing_index]
    
        if current_entry is None:
            return None
       
        elif me.get_key(current_entry) == key:
            return me.get_value(current_entry)
    
    return None

def remove(my_map, key):
    index = mf.hash_value(my_map, key)
    capacity = my_map['capacity']
    table = my_map['table']
    
    for i in range(capacity):
        probing_index = (index + i) % capacity
        current_entry = table[probing_index]
      
        if current_entry is None:
            return my_map
    
        elif me.get_key(current_entry) == key:
            table[probing_index] = None  
            my_map['size'] -= 1  
            my_map['current_factor'] = my_map['size'] / my_map['capacity']  
            return my_map
    
    return my_map  

def size(my_map):

    return my_map['size']

def is_empty(my_map):
    
    return my_map['size'] == 0

def key_set(my_map):
    keys = []
    for entry in my_map['table']:
        if entry is not None:
            keys.append(me.get_key(entry))
    return keys

def value_set(my_map):
    values = []
    for entry in my_map['table']:
        if entry is not None:
            values.append(me.get_value(entry))
    return values



def find_slot(my_map, key, hash_value):
    capacity = my_map['capacity']
    table = my_map['table']
    
    for i in range(capacity):
        probing_index = (hash_value + i) % capacity
        current_entry = table[probing_index]
        
        if current_entry is None or current_entry == None:
            return (False, probing_index)
        elif me.get_key(current_entry) == key:
            return (True, probing_index)
    
    return (False, -1)

def is_available(table, pos):
    return table[pos] is None or table[pos] == None

def rehash(my_map):
    old_table = my_map['table']
    new_capacity = mf.next_prime(my_map['capacity'] * 2)
    my_map['table'] = [None] * new_capacity
    my_map['capacity'] = new_capacity
    my_map['size'] = 0
    
    for entry in old_table:
        if entry is not None:
            key = me.get_key(entry)
            value = me.get_value(entry)
            put(my_map, key, value)
    return my_map