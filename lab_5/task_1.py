def make_collection():
    collection = []
    def change_collection(*new_collection):
        if new_collection[0] == "stop":
            result = collection.copy()  
            collection.clear()          
            return result
        else:
            collection.extend(new_collection)
    return change_collection
test = make_collection()

test(1,4,7)
test('sosiska')
print(test('stop'))