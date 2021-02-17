import sys 


def readfile_comb():
    file_comb= open('password_komb.txt','r')
    compare_list=[]
    pass_comb= file_comb.readline().strip()
    while pass_comb!='':
        compare_list.append(pass_comb)
        pass_comb= file_comb.readline().strip()

    file_comb.close()
    return compare_list

print(readfile_comb())

def compare_password():

    password_list= readfile_comb()

    if len(sys.argv)>1:
        for i in password_list:
            if sys.argv[1]==i:
                print('inappropriate password')       
    else:
        print('No input provided')

#compare_password()
    
    

