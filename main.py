# main.py
import sys

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

if __name__ == "__main__":
    print(mapping(sys.argv[1], sys.argv[2]));
