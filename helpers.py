from data import *


def receipt():
    receipt = [f'(==== {BUN_NAME} ====)']
    receipt.append(f'= {str(FILLING_TYPE).lower()} {FILLING_NAME} =')
    receipt.append(f'(==== {BUN_NAME} ====)\n')
    receipt.append(f'Price: {300.}')
    return '\n'.join(receipt)
