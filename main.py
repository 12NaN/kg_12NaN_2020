# main.py

def mapping(a, b):
    if(len(a) != len(b)):
        return False
    dicts = {}
    for i in range(len(a)):
        if(a[i] not in dicts):
            dicts[a[i]] = b[i];
        else:
            return False

    return True

def main():
    a = input("Enter the first word: ")
    b = input("Enter the second word: ")
    print(mapping(a,b))

if __name__ == "__main__":
    main();
