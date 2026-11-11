from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    return {name: age}


def list_to_dict(words: List[str]) -> Dict[str, int]:
    #declaration of list
    result = {}
    #for loop that traverses through the list
    for i in range(len(words)):
        #checks the current value that the index is pointed at
        cur_word = words[i]
        #saves tje current value to the index in the dictionary
        result[cur_word] = i
    return result 


# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
