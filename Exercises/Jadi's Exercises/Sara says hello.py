
message = input()

h_index = message.find('h')
if h_index == -1:
    print("No")
else:
    e_index = message.find('e', h_index+1)
    if e_index == -1:
        print('No')
    else:
        l1_index = message.find('l', e_index+1)
        if l1_index == -1:
            print('No')
        else:
            l2_index = message.find('l', l1_index+1)
            if l2_index == -1:
                print('No')
            else:
                o_index = message.find('o', l2_index +1)
                if o_index ==-1:
                    print('No')
                else:
                    print('Yes')