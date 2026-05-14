def create_collection_manager():
    """
    Создаёт менеджер коллекций с возможностью добавления элементов и получения результата.
    """
    collection = []

    def change_collection(*new_collection):
        if new_collection and new_collection[0] == "stop":
            result = collection.copy()
            collection.clear()
            return result
        else:
            collection.extend(new_collection)
            return None
    return change_collection

def validate_and_call(func):
    """
    Декоратор для проверки параметров перед вызовом функции.
    """
    def wrapper(x, y=None):
        if y is not None and x > 0 and isinstance(y, str):
            return func(x, y)
        else:
            return func("incorrect")
    return wrapper
