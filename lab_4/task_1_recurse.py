def find (mas,number):
    for i in range (len(mas)):
        if  isinstance(mas[i],list):
            result = find(mas[i],number) 
            if isinstance(result,int):
                return(result + i)
        else:
            if mas[i] == number:return(i)
    
    return
mas = [1, 2, [3, 4, [5, [6, []]]]]
print(find(mas,4))
print(find(mas,'spam'))