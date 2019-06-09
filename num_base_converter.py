'''
Author: Chris Kraus
Input: A number formatted for the input number's base, the initial base,
and output base. Output: A string representative of a number converted
to the expected output base.
'''

HEX_NUMS = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
            '6': '6', '7': '7', '8': '8', '9': '9', 'A': 10, 'B': 11, 'C': 12,
            'D': 13, 'E': 14, 'F': 15, '10': 'A', '11': 'B', '12': 'C',
            '13': 'D', '14': 'E', '15': 'F'}
HEX_BIN_NUMS = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
                '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
BIN_HEX_NUMS = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
                '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

original_num = ''
original_base = 0
output_base = 0


def func_picker(num, num_base, out_base):
    '''
    func_picker initializes a dictionary with keys in range(1, 101) with
    a value pair that is the function needed to convert the input value to
    the appropriate output value.
    '''
    picker = {}
    for i in range(1, 101):
        if i == 2:
            picker[i] = conv_to_bin(num, num_base)
        elif i == 16:
            picker[i] = conv_to_hex(num, num_base)
        else:
            picker[i] = conv_all_other_bases(num, num_base, out_base)
    return picker[out_base]


def reset():
    '''
    Resets the global variables back to their default setting each time
    the program is run.
    '''
    global original_num
    global original_base
    global output_base
    original_num = ''
    original_base = 0
    output_base = 0


def get_nums():
    '''
    Retrieves input from the user and validates the input before moving
    forward.
    '''
    global original_num
    original_num = input('Please enter the number you '
                         'would like to convert: ')
    original_num = original_num.replace(' ', '').upper()

    def get_org_base():
        try:
            global original_base
            while original_base not in range(1, 101):
                original_base = int(input('Please enter the base for the '
                                          'number you just entered (i.e. 2 for'
                                          ' binary 16 for hexidecimal): '))
                if original_base not in range(1, 101):
                    print(f'Sorry but {original_base} is not within the '
                          'range from 1 - 100, please try again.')
        except ValueError:
            print('\nPlease only enter whole numbers in range 1 - 100.')
            get_org_base()
    get_org_base()

    def get_out_base():
        try:
            global output_base
            while output_base not in range(1, 101):
                output_base = int(input('Please enter the base '
                                        'for output number: '))
                if original_base not in range(1, 101):
                    print(f'Sorry but {output_base} is not within the '
                          'range from 1 - 100, please try again.')
        except ValueError:
            print('\nPlease only enter whole numbers in range 1 - 100.')
            get_out_base()
    get_out_base()


def prepend_zeros():
    '''
    Adds 0's to the front of the global num until len(global num) is evenly
    divisible by 4. This prevents errors later when using the dictionaries.
    '''
    global original_num
    original_num = ((4 - len(original_num) % 4) * '0') + original_num


def convert_base():
    '''
    Retrieves the required inputs from the user and returns the result.
    Inputs: Original Num, Original Num's base, Output base.
    Outputs: A string representing the output num.
    '''
    get_nums()
    return func_picker(original_num, original_base, output_base)


def conv_to_bin(num, num_base):
    '''
    @Params: original num, original base
    Output: A string representing the output num in binary form.
    '''
    bin_num = ''

    if num_base == 2:
        return num

    elif num_base == 16:
        for i in num:
            bin_num += HEX_BIN_NUMS[i]

    else:
        try:
            if num_base != 10:
                orgn_num = int(conv_all_other_bases(num, num_base, 10))

            else:
                orgn_num = int(num)

            while int(orgn_num / 2) > 0:
                bin_num += str(orgn_num % 2)
                orgn_num = int(orgn_num / 2)
            bin_num += str(orgn_num % 2)
            bin_num = bin_num[::-1]

            index = 4
            while index < len(bin_num) and index != len(bin_num) - 1:
                bin_num = bin_num[:index] + ' ' + bin_num[index:]
                index += 5

            return bin_num
        except ValueError:
            print('Oops! Something went wrong. The program expected a number' +
                  f' but instead you entered: {num}')
            num = input('Please enter the number again formatted properly: ')
            return conv_to_bin(num, num_base)


def conv_to_hex(num, num_base):
    '''
    @Params: original num, original base
    Output: A string representing the output num in hexidecimal form.
    '''
    hex_num = ''
    try:
        if num_base == 2:
            prepend_zeros()
            num = original_num
            start_index = 0
            end_index = 4
            while end_index < len(num) and end_index != len(num):
                hex_num += BIN_HEX_NUMS[num[start_index:end_index]]
                start_index = end_index
                end_index += 4
            hex_num += BIN_HEX_NUMS[num[start_index:]]
            return hex_num
        elif num_base == 16:
            return num
        else:
            if num_base != 10:
                orgn_num = int(conv_all_other_bases(num, num_base, 10))
            else:
                orgn_num = int(num)
            while int(orgn_num / 16) > 0:
                hex_num += HEX_NUMS[str(orgn_num % 16)]
                orgn_num = int(orgn_num / 16)
            hex_num += HEX_NUMS[str(orgn_num % 16)]
            return hex_num[::-1]
    except ValueError:
        print('Oops! Something went wrong. The program expected a number'
              f' but instead you entered: {num}')
        num = input('Please enter the number again formatted properly: ')
        return conv_to_hex(num, num_base)


def conv_all_other_bases(num, org_base, out_base):
    '''
    @Params: original num, original base, output base
    Output: A string representing the output num.
    '''
    try:
        output = ''
        org_base_pow = len(num) - 1
        base_10_num = 0
        if org_base == 16:
            for i in num:
                base_10_num = int(HEX_NUMS[i])*16**org_base_pow
                if out_base == 10:
                    return base_10_num
        else:
            for i in num:
                base_10_num += int(i) * org_base ** org_base_pow
                org_base_pow -= 1
            while int(base_10_num / out_base) > 0:
                output += str(base_10_num % out_base)
                base_10_num = int(base_10_num / out_base)
            output += str(base_10_num % out_base)
        return output[::-1]
    except ValueError:
        print('Oops! Something went wrong. The program expected a number'
              f' but instead you entered: {num}')
        num = input('Please enter the number again formatted properly: ')
        return conv_all_other_bases(num, org_base, out_base)


def run_program():
    CONVERT_NUM = True

    while CONVERT_NUM:
        print(convert_base())
        reset()
        while CONVERT_NUM not in ['Y', 'N']:
            CONVERT_NUM = input('Would you like to convert another number? '
                                'Please enter "Y"/"N": ').upper()

        CONVERT_NUM = CONVERT_NUM[0] == 'Y'


run_program()
