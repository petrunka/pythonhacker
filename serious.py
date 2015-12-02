from firstday import to_number

def prime_sieve(n):
    all_numbers = set(x for x in range(2, n + 1))
    for i in range(2, n + 1):
        not_prime = set(x for x in range(i*2, n + 1, i))
        all_numbers = set(all_numbers) - set(not_prime)
    return sorted(list(all_numbers))

def is_transversal(transversal, family):
    for group in family:
        it =[x for x in group if x in transversal]
        if len(it) == 0 or len(it) > 1:
            return False
    return True

def count_words(n):
    word_counter = {}
    word = ''
    occurance = 0
    for i in n:
        word = i
        for j in range(0,len(n)):
            if n[j] == word:
                occurance+=1
            else:
                pass
        word_counter.update({word:occurance})
        occurance = 0
    return word_counter

def nan_expand(n):
    not_a_nan=''
    for i in range(0,n):
        not_a_nan+='Not a '
    not_a_nan+='NaN'
    return not_a_nan

def iterations_of_nan_expand(n):
    counter = 0
    if 'Not a' not in n:
        return False
    if 'NaN' not in n:
        return False
    for i in range(0, len(n)-5):
        if n[i:i+5] == 'Not a':
            counter+=1
    return counter

def group(n):
    groups = []
    subgroups = []
    subgroups.append(n[0])
    i = 1
    pointer = 0
    while i<len(n):
        if n[pointer] == n[i]:
            subgroups.append(n[i])
        else:
            groups.append(subgroups)
            subgroups = []
            subgroups.append(n[i])
        i+=1
        pointer+=1
    i = len(n)-1
    pointer = i-1
    subgoups = []
    if n[pointer] != n[i]:
        subgoups.append(n[i])
        groups.append(subgroups)
    else:
        while n[pointer] == n[i]:
            subgoups.append(n[i])
            i-=1
            pointer-=1
        groups.append(subgroups)
    return groups
            
def max_consecutive(items):
    lists = group(items)
    lengths = []
    for i in lists:
        lengths.append(len(i))
    max_value = lengths[0]
    for i in range(1, len(lengths)):
        if lengths[i] > max_value:
            max_value = lengths[i]
        else:
            pass
    return max_value

def gas_stations(distance, tank_size, stations):
    stations.append(distance)
    stops = []
    stops.append(0)
    for i in range(0, len(stations) - 1):
        if stations[i+1] > stops[len(stops)-1] + tank_size:
            stops.append(stations[i])
    stops.remove(0)
    return stops

def sum_of_numbers(n):
    suma = 0
    groups = []
    subgroups = []
    if n[0] =='0' or n[0] =='1' or n[0] =='2' or n[0] =='3' or n[0] =='4' or n[0] =='5' or n[0] =='6' or n[0] =='7' or n[0] =='8' or n[0] =='9':
        subgroups.append(int(n[0]))
    i = 1
    while i<len(n) - 1:
        if n[i] =='0' or n[i] =='1' or n[i] =='2' or n[i] =='3' or n[i] =='4' or n[i] =='5' or n[i] =='6' or n[i] =='7' or n[i] =='8' or n[i] =='9':
            subgroups.append(int(n[i]))
        elif n[i+1] =='0' or n[i+1] =='1' or n[i+1] =='2' or n[i+1] =='3' or n[i+1] =='4' or n[i+1] =='5' or n[i+1] =='6' or n[i+1] =='7' or n[i+1] =='8' or n[i+1] =='9':
            groups.append(subgroups)
            subgroups = []
        i+=1
    i = len(n)-1
    subgroups = []
    if n[i] !='0' and n[i] !='1' and n[i] !='2' and n[i] !='3' and n[i] !='4' and n[i] !='5' and n[i] !='6' and n[i] !='7' and n[i] !='8' and n[i] !='9':
        groups.append(subgroups)
    else:
        while n[i] =='0' or n[i] =='1' or n[i] =='2' or n[i] =='3' or n[i] =='4' or n[i] =='5' or n[i] =='6' or n[i] =='7' or n[i] =='8' or n[i] =='9':
            subgroups.append(int(n[i]))
            i-=1
        groups.append(subgroups)
    numbers = []
    for i in range(0, len(groups)):
        numbers_str = ''
        for j in range(0, len(groups[i])):
            numbers_str+=str(groups[i][j])
        numbers.append(numbers_str)
    if '' in numbers:
        numbers.remove('')
    if len(numbers) > 0:
        for i in numbers:
            suma+=int(i)
    else:
        pass
    return suma

def numbers_to_message(n):
    chars = group(n)
    return chars

print(prime_sieve(20))
print(is_transversal([2,3,6], [[1,2,9], [3,5,11], [4,6,7]]))
print(count_words(['book', 'book', 'book', 'beauty', 'sex', 'sex']))
print(nan_expand(4))
print(iterations_of_nan_expand('Not a Not a Not a Not a Not a NaN'))
print(iterations_of_nan_expand('I am a boy'))
print(group([1, 1, 1, 2, 3, 1, 1]))
print(max_consecutive([1, 1, 1, 2, 3, 1, 1, 4, 4, 4, 4,4]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))
print(sum_of_numbers("19.07.1992"))
print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))
