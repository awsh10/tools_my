def convert_to_exponent_float(number_in, digit=-6, precision=3):
    exp = 'e'
    number_in = float(number_in)
    float_exp_str = '{:.{}g}'.format(number_in, precision)
    float_point_str, sep, digit_ = str(float_exp_str).lower().partition(exp)
    fractional_part = float_point_str.partition('.')[2]
    len_fractional_part = len(fractional_part)
    digit_ = int(digit_) if digit_ else 0
    digit_ -= digit
    diff = digit_ - (len_fractional_part)
    precision_ = 0 if diff > 0 else -diff
    float_exp_str = '{:.{}f}'.format(float((float_point_str + exp +
                                         str(digit_))), precision_) + exp + str(digit)
    error = (number_in - float(float_exp_str)) / number_in
    error_max = 5 * 10 ** -precision
    if error > error_max:
        print("Error: {} is more err-r max = {}".format(error, error_max))
    return float_exp_str

def control_func():
    number, exp_value = -12567, 2
    len_ = len(str(number))
    for i in range(10 , -10, -1):
        number_ = round(((number * 10 ** i)), abs(i))
        print('{0:>2} {1:>17} {2:>17}'.format(i, number_, convert_to_exponent_float(number_, exp_value , 3)))
    return

#control_func()
def rem():
    import os
    import glob
    from time import time
    start = time()
    files = glob.glob('/home/awsh/PycharmProjects/Lutz/chess/*')
    for f in files:
        os.remove(f)
    time_exec = time() - start
    print('execution time = {:.3g}'.format(time_exec))

