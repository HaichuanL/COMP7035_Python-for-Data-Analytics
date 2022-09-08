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


if __name__ == '__main__':
    res = LAB
    input_str = 'MonDAY, tuesday, FRIDAY, sUnday'
    res_1 = res.lab_1(res, input_str)

