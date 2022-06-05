#This is just example
import OPERATOR
#this must be exist
def script():
    try:
        #your script here
        def p():
            t = OPERATOR.Copyright()
            return t
        print(p())
    except:
        #your except script here
        print("")
if __name__=='__main__':
    #this must be exist
    OPERATOR.LocalForm()
