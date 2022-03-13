from solution import *

try:
    try:
        N = int(input("Enter N:"))
        K = int(input("Enter K:"))
    except ValueError:
        print("Incorrect input")
        sys.exit()
        
    s = ReadFile(path)

    CheckVariables(N, K)
    print(FrequencyList(s))
    print("Amount of words: ", WordsCounts(s))
    print("Average amount of words in sentence: ", Average(WordsCounts(s)))
    print("Median amount of words in sentence: ", Median(WordsCounts(s)))
    dct = Ngramms(s, K)
    print(f"Top-{N} {K}-gramms: ")
    print([dct[i] for i in range(min(N, len(dct)))])

except EOFError as exception:
    print(exception)

except ValueError as ex:
    print(ex)
