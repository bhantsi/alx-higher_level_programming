#!/usr/bin/python3

def hidden():
    import hidden_4

    methods = dir(hidden_4)
    for method in methods:
        if method[0].isalnum():
            print("{}".format(method))

if __name__ == "__main__":
    hidden()
