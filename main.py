import OPERATOR
def script():
    try:
        print(OPERATOR.HOW_TO_USE_THIS_PACKAGE())
        print(OPERATOR.Copyright())
    except:
        print("")
if __name__=='__main__':
    OPERATOR.LocalForm()