
def check_carrots(arr, capability):
    max_value = {
        'kg': 0.0,
        'price': 0.0
    }
    arr = sorted(arr, key=lambda d: d['price']) 
    for carrot in arr:
        if (max_value['kg'] < capability) and (max_value['kg']+ carrot['kg']) <= capability:
            max_value['kg'] = max_value['kg']+ carrot['kg']
            max_value['price'] = max_value['price'] + carrot['price']
    return max_value

if __name__ == '__main__':
    cap = float(input('Capability: '))
    n = int(input('Number of carrots: '))
    i = 0
    carrs = [] 
    while i < n:
        carrs.append(
            {
                'kg': float(input('kg: ')),
                'price': float(input('price: '))
            }
        )
        i +=1
    print(check_carrots(carrs, cap))