# main.py
import sys # Used to be able to pass CLI arguments to mapping

def mapping(a, b):          # Takes two inputs
    if(len(a) != len(b)):   # if 'a' and 'b' don't have the same length you can't map each value 1-to-1
        return "false"      # thus return false
    dicts = {}              
    for i in range(len(a)):     # Since 'a' and 'b' are the same length iterate through the length of 'a'
        if(a[i] not in dicts):  # If the value in 'a' at index 'i' is not in the dictionary, then map the value at b[i] to it
            dicts[a[i]] = b[i];
        else:                   # Otherwise, return false since it can't be 1-to-1
            return "false"

    return "true"               # If each value in 'a' is mapped to a value in 'b', then return true

if __name__ == "__main__":
    print(mapping(sys.argv[1], sys.argv[2])); # Passes CLI arguments to mapping 
