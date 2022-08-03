#!/usr/bin/env python3

def dividing(n_num, m_num):
    div = m_num / n_num
    return div == int(div)

def get_divisors(num):
    res=[]
    for n in range(2,num):
        if dividing(n,num):
            res.append(n)

    return res


def show_divisors():
    all_nums = []
    for n in range(2,101):
        list_of_divisor = get_divisors(n)
        if len(list_of_divisor) != 0:
            all_nums.append( [ n, list_of_divisor ] )

    all_nums = sorted(all_nums, key = lambda num_list : len(num_list[1]))

    for entry in all_nums:
        print(entry)


show_divisors()


print("""
===
This program shows each number between 1..100 and it's divisors, The output is sorted by the number of divisors.

60 - the smallest number between 1..100 with 10 divisors
100 - has only 7 divisors.

That may be a reason why they had a base 60 system in Mesopotamia.
===
""")


