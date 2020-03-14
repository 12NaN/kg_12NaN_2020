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
    a, b = input("").split()
    print(mapping(a,b))

if __name__ == "__main__":
    main();
