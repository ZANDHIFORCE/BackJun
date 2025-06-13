def solution(expressions):
    #정규화
    e_list = normalize(expressions)
    print(e_list)
    
    #가능 진수 찾기
    # n1_set = set(
    #     int(e_list[i][j])%10, int(e_list[i][j]//10)%10
    #     for i in range(len(e_list)) 
    #     for j in range(len(e_list[0])) 
    #     if e_list[i][j].isdigit()
    # )
    
    n1_set = set()
    for i in range(len(e_list)):
        for j in range(len(e_list[0])):
            if e_list[i][j].isdigit():
                n1, n10 = int(e_list[i][j])%10, int(e_list[i][j])//10
                n1_set.add(n1)
                n1_set.add(n10)
    
    
    max_n1 = max(n1_set)
    jinsu = [i>max_n1 for i in range(10)]
    
    #확정 검사
    prime_jinsu = 0
    for e in e_list:
        first_n1, second_n1 = int(e[0])%10, int(e[2])%10
        first_n10, second_n10 = int(e[0])//10, int(e[2])//10
        #-일때 확정
        if e[1]== "-" and  first_n1 < second_n1  and e[4]!="X":
            result_n1 = int(e[4])%10
            prime_jinsu = second_n1 + result_n1 - first_n1
            jinsu = [i==prime_jinsu for i in range(10)]
            break
        #+일떄 확정 
        elif e[1]== "+"  and e[4]!="X" and  ((first_n1+second_n1)%10 != int(e[4])%10 or (first_n10+second_n10)%10 != int(e[4])//10):
            result_n1 = int(e[4])%10
            result_n10 = int(e[4])//10
            if first_n1 + second_n1 != result_n1:
                prime_jinsu = (10-(result_n1 - (first_n1+second_n1)%10))%10
            else:
                prime_jinsu = (10 - (result_n10 - (first_n10+second_n10)%10))%10
                print("프진",prime_jinsu , first_n10, second_n10, result_n10)
            jinsu = [i==prime_jinsu for i in range(10)]
            break
            
    print(jinsu)
    #확정일 떄
    a_list = []
    if prime_jinsu!=0:
        print(prime_jinsu)
        for e in e_list:
            if e[4]=="X":
                e[4] = cal_jinsu(e[0],e[1],e[2],prime_jinsu)
                a_list.append(e)
    elif max_n1==8:
        print(max_n1+1)
        for e in e_list:
            if e[4]=="X":
                e[4] = cal_jinsu(e[0],e[1],e[2],9)
                a_list.append(e)
    #확정 아닐 때
    else:
        for e in e_list:
            first_n1, second_n1 = int(e[0])%10, int(e[2])%10
            if e[4]=="X":
                if e[1] == "+":
                    if first_n1 + second_n1< 9 and not jinsu[first_n1+second_n1]:
                        e[4] = str(int(e[0]) + int(e[2]))
                        a_list.append(e)
                    else:
                        e[4] = "?"
                        a_list.append(e)
                elif e[1] == "-":
                    if first_n1>=second_n1:
                        e[4] = str(int(e[0]) - int(e[2]))
                        a_list.append(e)
                    else:
                        e[4] = "?"
                        a_list.append(e)
    
    answer = [ " ".join(a) for a in a_list ]
    print(answer)
    return answer

def normalize(expressions):
    list1 =  []
    for e in expressions:
        list1.append(e.split())
    return list1

def cal_jinsu(n1, method , n2, jinsu):
    n1, n2 = int(n1), int(n2)
    if method=="+" and (n1%10+n2%10>=jinsu or ((n1//10)%10+(n2//10))%10>=jinsu):
        if n1%10+n2%10>=jinsu:
            n3 = n1+n2 + (10-jinsu)
            if ((n1//10)%10+(n2//10))%10>=jinsu:
               n3 +=  (10-jinsu)*10
            return str(n3)
    elif method=="-" and n1%10 < n2%10:
        return str(n1-n2 - (10-jinsu))
    else:
        if method=="+":
            return str(n1+n2)
        elif method=="-":
            return str(n1-n2)
        else:
            return False
    return False


            
    
