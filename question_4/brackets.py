def check_brackets(brackets):
    checked = []
    open_list = ["[","{","("]
    close_list = ["]","}",")"]
  
    for i in brackets:
        if i in open_list:
            checked.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(checked) > 0) and (open_list[pos] == checked[len(checked)-1])):
                checked.pop()
            else:
                return False

    if len(checked) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    brackets = input()
    print(check_brackets(brackets))

# { [ (  ) ] }

# { [ ] ( { } { } ) [ ] }
