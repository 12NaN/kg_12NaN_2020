# main.py

def mapping(a, b):
    if(len(a) != len(b)):
        return "false"
    dicts = {}
    for i in range(len(a)):
        if(a[i] not in dicts):
            dicts[a[i]] = b[i];
        else:
            return "false"

    return "true"

def main():
    a = input("")
    b = input("")
    print(mapping(a,b))

if __name__ == "__main__":
    main();
