from OPERATOR_PACK import OPERATOR
def script():
    try:
        from OPERATOR_PACK import OPERATOR as op
        import random as rd
        rdnLIST = ['{}'.format(op.HOW_TO_USE_THIS_PACKAGE()),'{}'.format(op.Copyright())]
        rdn = rd.choice(rdnLIST)
        def helloworldTEXT():
            TxT = '{}'.format("hello world")
            return TxT
        def z():
            C = 0
            return C
        if z()>=0:
            print(helloworldTEXT())
    finally:
        print(rdn)
if __name__=='__main__':
    OPERATOR.LocalForm()