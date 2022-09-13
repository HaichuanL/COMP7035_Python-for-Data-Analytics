class LAB:
    # def lab_1(self, input_str='you fail to input a string'):
    def lab_1(self, input_str):
        print(f'You input the string: {input_str}')
        print('result in uppercase: ', end='')
        print(input_str.upper())
        print('result in lowercase: ', end='')
        print(input_str.lower())
        print('result in titlecase: ', end='')
        print(input_str.title())
        return 'Lab_1'

    def lec_2(self):
        """define a list"""
        # append list
        list_n = []
        for i in range(5):
            list_n.append(i)
        print(list_n)
        # for loop simple way
        list_x = [i for i in range(6)]
        list_y = [range(6)]
        # 单个星号(*),如：*parameter是用来接受任意多个参数并将其放在一个元组中。
        list_y_v2 = [*range(6)]
        print(f'list_x is {list_x}')
        print(f'list_y is {list_y}')
        print(f'list_y_v2 is {list_y_v2}')

        """List Operation"""
        list_s = [5, 2.3, 'morning', True]
        print('First element:', list_s[0])
        print('Last element:', list_s[-1])
        print('List length:', len(list_s))
        for i in list_s:
            print(i)
        for i in range(len(list_s)):
            print(f'{i}th element is:', list_s[i])
        list_s_2 = list_s[:2]
        print('first two elements:', list_s_2)
        # caoncat two lists
        list_s_con = list_s + list_s_2
        print('list_s_sum:', list_s_con)
        # multiply list
        print('multiply list:', list_s * 3)
        # replace the element
        list_s[0] = 'mutable'
        print('after replacement:', list_s)

        """copy list: shallow copy & deep copy"""
        # shallow copy
        list_s_copy_s = list_s
        print('shallow copy:', list_s_copy_s)
        list_s_copy_s[0] = 'shallow'
        print('changed shallow copy:', list_s_copy_s)
        print('shallow copy also change the origin list:', list_s)
        # deep copy
        list_s_copy_d = list_s.copy()
        print('deep copy:', list_s_copy_d)
        list_s_copy_d[0] = 'deep'
        print('changed deep copy:', list_s_copy_d)
        print('deep copy wont change the origin list:', list_s)

        """List Methods"""
        # append
        list_a = []
        for i in range(10):
            list_a.append(i)
        print('append methods:', list_a)
        # extend
        list_b = ['x', 'y']
        list_a.extend(list_b)
        print('extend methods:', list_a)
        # pop: delete the i-th element, default is the last one
        list_p = [3, 5, 2]
        while len(list_p) > 0:
            elt = list_p.pop(0)
            print(f"Removed {elt}, a is now {list_p}")
        # remove: delete the exact element, when you know what it is
        list_a.remove('y')
        print(list_a)
        # insert: (i, element) put element into i-th position
        list_a.insert(0, 'zero')
        print(list_a)
        # sort
        list_sort = [6, 7, 9, 3, 1]
        list_sort.sort()
        print('sorted list_sort', list_sort)
        # count
        # index
        # reverse

        """List Comprehensions: easy way of for loop"""
        # origin loop
        s = []
        for x in range(21):
            if x % 3 == 0:
                s.append(x)
        print(s)
        # simple one
        s_sim = [x for x in range(21) if x % 3 == 0]
        print(s_sim)
        # e.g.
        print([i**2 for i in range(5)])

        return True


if __name__ == '__main__':
    res = LAB
    '''lab1'''
    # input_str = 'MonDAY, tuesday, FRIDAY, sUnday'
    # res_1 = res.lab_1(res, input_str)
    '''lec2'''
    lec_2 = res.lec_2(res)


