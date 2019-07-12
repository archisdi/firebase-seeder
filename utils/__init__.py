import datetime

def generate_store_code(initial =''):
    """
        Generator for store code
        initial : E - External
                  I - Internal
    """

    epoch = datetime.datetime(2017, 1, 1, 0, 0)

    def int2base(x, b=36, alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        """ Convert an integer to its string representation in a given base """

        if isinstance(x, complex):  # return a tuple
            return (int2base(x.real, b, alphabet), int2base(x.imag, b, alphabet))

        if x <= 0:
            if x == 0:
                return alphabet[0]
            else:
                return '-' + int2base(-x, b, alphabet)

        # else x is non-negative real
        rets = ''
        while x > 0:
            x, idx = divmod(x, b)
            rets = alphabet[idx] + rets
        return rets

    return initial + str(int2base(int((datetime.datetime.now() - epoch).total_seconds() * 1000.0)))

if __name__ == '__main__':
    print(generate_store_code())