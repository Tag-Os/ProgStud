def find (mas,num):
    stack = mas[:]
    index = 0
    answer = None
    while stack:
        current = stack.pop(0)
        if isinstance(current,int):
            if current == num:
                return(index)
            else:index += 1
        else:
            stack = current[:]

    return(answer)

mas = [1, 2, [3, 4, [5, [6, []]]]]
print(find(mas,4))
print(find(mas,'spam'))
