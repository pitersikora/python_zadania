# Program do symulacji "Problemu Jozefa Flawiusza" - w parametrach startowych programu
# nalezy podac liczbe rycerzy bioracych udzial w symulacji.

import sys

def get_input(user_input):
    print ('Program symulujacy problem Jozefa Flawiusza\n')
    try:
        if user_input.isdigit() == False:
            print ('\033[91mPodana wartosc nie jest liczba !!!\033[00m')
            exit(2)
    except Exception as exc:
        print (exc)
        print ('\033[91mPodaj liczbe rycerzy w parametrach startowych programu !!!\033[00m')
        exit(1)
    print ("Liczba rycerzy: %s" % user_input)
    return int(user_input)

def generate_knights(knights):
    generated_ring = []
    if knights == None:
        print ('\033[91mNiewlasciwy argument funkcji!!!\033[00m')
        exit(3)
    for i in range(0, int(knights)):
        generated_ring.append(i+1)
    return generated_ring

def simulate_problem(array_to_simulate):
    if array_to_simulate == None:
        print ('\033[91mNiewlasciwy argument funkcji!!!\033[00m')
        exit(3)
    round_counter = 1
    while len(array_to_simulate) != 1:
        round_string = ""
        temporary_list = []
        print ("\nRunda: %s\n" % round_counter)
        for i in range(0, len(array_to_simulate)):
            if i % 2 == 0:
                round_string += str(array_to_simulate[i]) + " "
                temporary_list.append(array_to_simulate[i])
            else:
                round_string += "\033[1;31;49m%s \033[00m" % str(array_to_simulate[i])
        print (round_string)
        if len(array_to_simulate) % 2 == 1:
            temporary_list.insert(0, temporary_list[-1])
            del temporary_list[-1]
        array_to_simulate = temporary_list
        round_counter += 1
    return array_to_simulate

def print_result(array_to_fill, knights):
    print ("\nW kregu smierci zlozonym z %s rycerzy, lepiej zebys stal na \033[92m%d\033[00m miejscu !!!" % (knights, array_to_fill[0]))

def main():
    knights_ammount = get_input(sys.argv[1])
    print (knights_ammount)
    death_ring = generate_knights(knights_ammount)
    death_ring = simulate_problem(death_ring)
    print_result(death_ring, knights_ammount)

if __name__ == "__main__":
    main()