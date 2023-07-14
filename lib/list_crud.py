def create_an_empty_list():
    return []

# assign the new_list to a global varibale
def create_a_list():
    global new_list 
    new_list = ['hi',3, False, 10]
    return new_list

def add_element_to_end_of_list(l, element):
    new_list.append(5)
    return new_list

def add_element_to_start_of_list(l, element):
    new_list.insert(0, element)
    return new_list

def remove_element_from_end_of_list(l):
    new_list.pop()
    return new_list


def remove_element_from_start_of_list(new_list):
    del new_list[0]
    return new_list


def retrieve_first_element_from_list(new_list):
    return new_list[0]

def retrieve_element_from_index(new_list, index):
    return new_list[1]

def retrieve_last_element_from_list(new_list):
    return new_list[-1]
