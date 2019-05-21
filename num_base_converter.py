'''
Author: Chris Kraus
Input: A number formatted for the input number's base, the initial base, and output base.
Output: A string representative of a number converted to the expected output base.
'''

HEX_NUMS = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7',
            '8': '8', '9': '9', 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
            '10': 'A', '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F'}
HEX_BIN_NUMS = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
                '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
                'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
BIN_HEX_NUMS = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5',
                '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}


def convert_base():
    '''
    Retrieves the required inputs from the user and returns the result.
    Inputs: Original Num, Original Num's base, Output base.
    Outputs: A string representing the output num.
    '''

    original_num = input('Please enter the number you '
                         'would like to convert: ').upper()
    original_base = int(input('Please enter the base for the number you '
                              'just entered (i.e. 2 for binary 16 for '
                              'hexidecimal: '))
    output_base = int(input('Please enter the base for output number: '))

    if output_base == 2:
        return conv_to_bin(original_num, original_base)

    elif output_base == 16:
        return conv_to_hex(original_num, original_base)

    return conv_all_other_bases(original_num, original_base, output_base)


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


def conv_to_hex(num, num_base):
    '''
    @Params: original num, original base
    Output: A string representing the output num in hexidecimal form.
    '''

    hex_num = ''

    if num_base == 2:
        num.replace("", "")
        start_index = 0
        end_index = 4

        if len(num) % 4 != 0:
            num_zeros = (4 - (len(num) % 4)) * '0'
            num = num_zeros + num
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


def conv_all_other_bases(num, org_base, out_base):
    '''
    @Params: original num, original base, output base
    Output: A string representing the output num.
    '''

    output = ''
    org_base_pow = len(num) - 1
    base_10_num = 0

    for i in num:
        base_10_num += int(i) * org_base ** org_base_pow
        org_base_pow -= 1

    while int(base_10_num / out_base) > 0:
        output += str(base_10_num % out_base)
        base_10_num = int(base_10_num / out_base)
    output += str(base_10_num % out_base)

    return output[::-1]


CONVERT_NUM = True

while CONVERT_NUM:
    print convert_base()

    while CONVERT_NUM not in ['Y', 'N']:
        CONVERT_NUM = input('Would you like to convert another number? '
                            'Please enter "Y"/"N": ').upper()

    CONVERT_NUM = CONVERT_NUM[0] == 'Y'
