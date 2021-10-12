#citirea listei
def read_list():
    lst = []
    sir_numere = input('Dati valori separate prin spatiu: ')
    sir_numere_split = sir_numere.split(' ')
    for nr in sir_numere_split:
        lst.append(int(nr))
    return lst

#problema 8

def is_prime(x):
    '''
    Verificam daca un numar este prim
    :param x:int
    :return:True daca este prim, False in caz contrar
    '''
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def Suma(p):
    s = 0
    for i in range(len(p)):
         s = s + p[i]
    return s

def get_longest_sum_is_prime(lst: list[int]) -> list[int]:
    '''
    2.Suma numerelor este un numar prim
    :param lst: lista de numere intregi
    :return: ret_subsecv, cea mai lunga subsecventa cu proprietatea ca suma numerelor sa fie numar prim
    '''
    max_lungime = 0
    ret_subsecv = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            subsecv_curenta = lst[i: j+1]
            if len(subsecv_curenta) > max_lungime and is_prime(Suma(subsecv_curenta)):
                max_lungime = len(subsecv_curenta)
                ret_subsecv = subsecv_curenta
    return ret_subsecv

def test_get_longest_sum_is_prime():
    assert get_longest_sum_is_prime([2,3,5,4,7,2,1]) == [2,3,5,4,7,2]
    assert get_longest_sum_is_prime([2,3,5,4,7,2,1,2]) == [2,3,5,4,7,2]
    assert get_longest_sum_is_prime([2,3,5,4,7,2]) == [2,3,5,4,7,2]


#problema 18

def is_desc(nr):
    '''
    Determina daca cifrele unui numar sunt in ordine descrescatoare
    :param nr: int
    :return: True, daca toate cifrele sunt in ordine descrescatoare, False in caz contrar
    '''
    while nr > 9:
        if nr % 10 > nr // 10 % 10:
            return False
        nr = nr // 10
    return True

def get_longest_digit_count_desc(lst: list[int]) -> list[int]:
    '''
    Determina numerele care au cifrele in ordine descrescatoare
    :param lst: lista de numere intregi
    :return: lista cu numerele in ordine descrescatoare
    '''
    ret_subsecv = []
    for i in lst:
       if is_desc(i):
           ret_subsecv.append(i)
    return ret_subsecv

def test_get_longest_digit_count_desc():
    assert  get_longest_digit_count_desc([76, 56, 87, 35, 92]) == [76, 87, 92]
    assert get_longest_digit_count_desc([45, 56, 78, 89, 98, 51]) == [98, 51]
    assert get_longest_digit_count_desc([54, 76, 89, 68, 63]) == [54, 76, 63]

def print_menu():
    print('1. Citirea listei ')
    print('2. Afisare subsecventa maxima care are suma un numar prim ')
    print('3. Afisare subsecventa maxima care are numere cu cifrele in ordine descrescatoare ')
    print('4. Iesire')


def main():
    test_get_longest_sum_is_prime()
    test_get_longest_digit_count_desc()
    lst = []
    while True:
        print_menu()
        optiune = input('Alegeti o optiune: ')
        if optiune == '1':
            lst = read_list()
        elif optiune == '2':
             print(get_longest_sum_is_prime(lst))
        elif optiune == '3':
             print(get_longest_digit_count_desc(lst))
        elif optiune == '3':
            break

if __name__ == "__main__":
    main()