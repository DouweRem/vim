import sympy as sym
import re

# x, y, z = sym.symbols('x y z')
# expr = sym.exp(x*y*z)
# print(sym.diff(expr, x, y, y, z, z, z, z))
#

FUNCTIONS = ['ln', 'log_', 'log', 'exp', 'sin', 'cos', 'tan', 'sinh', 'cosh', 'tanh',
             'arcsin', 'arccos', 'arctan', 'left', 'right', 'sqrt', 'frac', 'sum']

CONSTANTS = ['pi', 'hbar']

EULER_CHAR = 'e'
IMAGINARY_CHAR = 'i'


def is_number(s):
    """Checks if a string is a number
    :param: s: string to check
    :return: True if s is a number, False otherwise
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def subscript_symbol(substring):
    """Creates a sympy symbol from a subscripted LaTeX string
    :param: substring: LaTeX string
    :return: the key, the symbol and the LaTeX string with the subscripted symbol removed
    """
    sub_index = substring.index('_')
    command_bool = False
    if '\\' in substring[:sub_index]:
        command_bool = True
        start_index = substring.rfind('\\') + 1
    else:
        start_index = sub_index - 1
    symbol = substring[start_index:sub_index]
    subscript = substring[sub_index + 1:]

    snippet = symbol + '_' + subscript
    symbol = sym.symbols(symbol + '_' + subscript)

    if command_bool:
        substring = substring.replace('\\' + snippet, '')
    else:
        substring = substring.replace(snippet, '')
    return snippet, symbol, substring


def bracket_symbol(substring):
    pass


def substring_symbol(substring):
    """Creates sympy symbols from a substring of LaTeX
    :param: substring: LaTeX substring
    :return: (keys, symbols) where keys is a list of the keys of the symbols
    """
    print(substring)


    keys, symbols = [], []
    if '_' in substring:
        pass

    substring = substring.replace('(', ' ').replace(')', ' ')
    substring = substring.replace('{', '').replace('}', '')

    if '\\' in substring:
        # If the substring contains a \, split it at each occurrence of
        subsubstrings = substring.split('\\')
        for subsubstring in subsubstrings[1:]:
            # All new subsubstrings except for the first one must be symbols
            # add these to the dictionary and remove them from the substring
            keys.append(subsubstring)
            symbols.append(sym.symbols(subsubstring))
            substring = substring.replace('\\' + subsubstring, '')

    for char in substring:
        # All remaining characters must be symbols, add them to the dictionary
        if char.isalpha() and char != IMAGINARY_CHAR and char != EULER_CHAR:
            keys.append(char)
            symbols.append(sym.symbols(char))
    return keys, symbols


def remove_nonvariables(latex_string):
    """Removes functions and constants from a substring
    :param: latex_string: string to remove functions from
    :return: substring with functions removed
    """
    for func in FUNCTIONS:
        latex_string = latex_string.replace('\\' + func, '')
    for const in CONSTANTS:
        latex_string = latex_string.replace('\\' + const, '')
    return latex_string


def create_symbols(latex_string):
    """Creates sympy symbols from a string of LaTeX
    :param: latex_string: LaTeX string
    :return: list of sympy symbols
    """

    # Remove the functions and constants from the string
    if any(func in latex_string for func in FUNCTIONS) or any(const in latex_string for const in CONSTANTS):
        latex_string = remove_nonvariables(latex_string)

    symbol_dict = {}

    # Split the string into substrings at definite symbol ends
    substrings = re.split('[ +-]', latex_string)

    for substring in substrings:
        if is_number(substring) or substring == '':
            # If the substring is a rational number or empty: ignore
            continue
        else:
            # Else: execute substring_symbol
            keys, symbols = substring_symbol(substring)
            for i in range(len(keys)):
                if keys[i] not in symbol_dict:
                    symbol_dict[keys[i]] = symbols[i]

    return symbol_dict


if __name__ == '__main__':
    latex_string = r'x_ix_j + z_{a_1} + \rho_a + \ln(a + cd \omega)'
    print(create_symbols(latex_string))
