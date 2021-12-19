def Bisect(elem, sequence) -> bool:
    if len(sequence) == 1 and sequence[0] != elem:
        return False
    middle_index = len(sequence) // 2
    if sequence[middle_index] == elem:
        return True
    elif sequence[middle_index] < elem:
        return Bisect(elem, sequence[middle_index:])
    else:
        return Bisect(elem, sequence[:middle_index])
        
# для тестов
elem, seq = eval(input())
print(Bisect(elem, seq))
