from math import sqrt

def palindrome(n):
    r=n[:-1]
    for i in range(0, (len(n)+1)//2):
        if r[i]!=n[i]:
            return False
    return True

def is_number_balanced(n):
    sum_a = 0
    sum_b = 0
    f = str(n)
    if len(f) == 1:
        return True
    else:
        for i in range(0, (len(f)//2), 1):
            sum_a+=int(f[i])
            sum_b+=int(f[len(f)- i - 1])
        if sum_a == sum_b:
            return True
        else:
            return False

def is_increasing(n):
    for i in range(1, len(n), 1):
        if n[i]<=n[i-1]:
            return False
    return True

def is_decreasing(n):
    for i in range(1, len(n), 1):
        if n[i]>=n[i-1]:
            return False
    return True

def get_largest_palindrome(n):
    largest_palindrome = 0
    number = n
    while palindrome(number) == False:
        number-=1
    return number

def prime_numbers(n):
    prime_numbers = []
    flag = 0
    for i in range(2, n,1):
        for j in range(2, int(sqrt(i))+1, 1):
            if i % j == 0:
                flag = 1
        if flag == 0:
            prime_numbers.append(i)
        flag = 0
    return prime_numbers

def is_anagram(a,b):
    a = a.lower()
    b = b.lower()
    anagram_a = []
    anagram_b = []
    for i in range(0, len(a)):
        anagram_a.append(a[i])
    for j in range(0, len(b)):
        anagram_b.append(b[j])
    anagram_a.sort()
    anagram_b.sort()
    if anagram_a == anagram_b:
        return True
    else:
        return False

def birthday_ranges(birthday, ranges):
    birthday_in_range = []
    counter = 0
    for tuples in ranges:
        for i in range(tuples[0], tuples[1]+1):
            for j in birthday:
                if i == j:
                    counter+=1
        birthday_in_range.append(counter)
        counter = 0
    return birthday_in_range

def sum_matrix(m):
    amount = 0
    for i in m:
        for j in i:
            amount+=j
    return amount
