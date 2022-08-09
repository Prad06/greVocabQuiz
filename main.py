import csv
from email.header import Header
from time import sleep
import pandas as pd
from learn import *
from test import *
from print import *


def callFunc(arg, df):
    if arg == 1:
        return learnSet(df)
    elif arg == 2:
        return testSet(df)
    elif arg == 3:
        return printSet(df)
    
    return

def main():
    df = pd.read_csv("Final_Words.csv", header=None)
    df.rename(columns={0:"Word", 1:"Meaning"}, inplace=True)
    df = df[["Word", "Meaning"]]
    case = 0

    while(case!=4):
        print("Options:\n 1. Learn  2. Test  3. Print Set  4. Exit")
        case = int(input())
        callFunc(case, df)
        print("\n")
        sleep(1)

if __name__ == "__main__":
    main()