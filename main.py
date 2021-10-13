#citirea listei
def read_list():
    lst = []
    lst_str = input("Introduceti numerele separate printr-un spatiu: ")
    lst_str_split = lst_str.split(' ')
    for number in lst_str_split:
        lst.append(number)

    return lst

def converteste_lista_int(lst):

    list_int = []
    for i in lst:
        list_int.append(int(i))

    return list_int

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

def Suma(l):
    s = 0
    for i in range(len(l)):
         s = s + l[i]
    return s


def get_longest_sum_is_prime(lst: list[int]) -> list[int]:
    '''
    Suma numerelor este un numar prim
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


#problema 10

def Numerele_sunt_Pare(l):
    '''
    Determinam daca in lista toate numerele sunt pare
    :param l: lista de numere intregi
    :return: True, daca toate numerele din lista sunt pare sau False, in caz contrar
    '''
    for i in l:
        if i%2!=0:
            return False
    return True

def test_Numerele_sunt_Pare():
    assert Numerele_sunt_Pare([5, 6, 7, 4, 6, 8]) == False
    assert Numerele_sunt_Pare([4, 6, 8, 2]) == True
    assert Numerele_sunt_Pare([1, 3, 5, 7, 9]) == False

def get_longest_all_even(lst: list[int]) -> list[int]:
    '''
    Cea mai lunga subsecventa de numere pare
    :param lst: lista de numere intregi
    :return: Cea mai lunga subsecventa de numere pare
    '''
    max_subsecv = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if Numerele_sunt_Pare(lst[i: j+1]) and len(max_subsecv)< len(lst[i: j+1]):
                max_subsecv = lst[i: j+1]
    return max_subsecv

def test_get_longest_all_even():
    assert get_longest_all_even([1, 4, 6, 8, 3, 4, 8, 9]) == [4, 6, 8]
    assert get_longest_all_even([1, 4, 8, 9, 6, 5, 2, 1]) == [4, 8]
    assert get_longest_all_even([1, 3, 5, 7, 9]) == []


def print_menu():
    print('1. Citirea listei ')
    print('2. Afisare subsecventa maxima care are suma un numar prim ')
    print('3. Afisare subsecventa maxima care are numere cu cifrele in ordine descrescatoare ')
    print('4. Afisare subsecventa maxima care are toate numerele pare ')
    print('5. Iesire ')


def main():
    test_get_longest_sum_is_prime()
    test_get_longest_digit_count_desc()
    test_get_longest_all_even()
    lst = []
    while True:
        print_menu()
        optiune = input('Alegeti o optiune: ')
        if optiune == '1':
             lst = read_list()
        elif optiune == '2':
            int_list1 = converteste_lista_int(lst)
            print(f"Afisare subsecventa maxima care are suma un numar prim: {get_longest_sum_is_prime(int_list1)}")
        elif optiune == '3':
            int_list1 = converteste_lista_int(lst)
            print(f":Afisare subsecventa maxima care are numere cu cifrele in ordine descrescatoare: {get_longest_digit_count_desc(int_list1)}")
        elif optiune == '4':
            int_list1 = converteste_lista_int(lst)
            print(f"Afisare subsecventa maxima care are toate numerele pare: {get_longest_all_even(int_list1)}")
        elif optiune == '5':
            break

if __name__ == "__main__":
    test_get_longest_sum_is_prime()
    test_get_longest_digit_count_desc()
    test_get_longest_all_even()
    main()
