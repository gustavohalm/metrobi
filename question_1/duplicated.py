def find_duplicated(arr):
    itens = {}
    duplicated = []
    for i in arr:
        if i in itens:
            itens[i] = itens[i] +1
            if i not in duplicated:
                duplicated.append(i)
        else:
            itens[i] = 1
    return duplicated

if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    result = find_duplicated(arr)
    print(result)