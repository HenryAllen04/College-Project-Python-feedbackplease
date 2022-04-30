import Login as Log
import myTask4a_currency_conversion as CC
import Trends

def main():
    Log.start_choice()
    CC.CurrencyConvert()
    print("")
    Bool = True
    while Bool:
        Bool = False
        try:
            x = int(input("Enter 1 if you would like to see trends and patterns.\nIf not enter 2\n:"))
        except:
            print("Please try again. 1 OR 2!")
            Bool = True
    if x == 1:
        Trends.show_trends()
    else:
        pass


main()
