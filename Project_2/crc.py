
def xor(a,c,n): 
    result=""
    a=remove_starting_zero(a,n)
    a_len=len(a)
    if a_len<n:
        return a
    for i in range(n):
        if(a[i]==c[i]):
            res='0'
        else:
            res='1'
        result+=res
    here=n-1
    j=0
    count_zero=0
    for j in range(n):
        if(result[j]=='0'):
            count_zero+=1
            continue
        else:
            here=j
            break
    if(count_zero==n):
        result=''
    else:
        result=result[here:n]
    return result


def create_t_from_m(m,c):
    k=len(c)-1
    app=""
    for i in range(k):
        app+='0'
    t=m+app
    return t

def create_p_from_t(t,r):
    t_len=len(t)
    r_len=len(r)
    zero_apnd=count_zeros(t,t_len)
    t=remove_starting_zero(t,t_len)
    new_t=len(t)
    apnd=new_t-r_len
    for i in range(apnd):
        r='0'+r
    p=xor(t,r,new_t)
    for i in range(zero_apnd):
        p='0'+p
    return p

def remove_starting_zero(a,n):
    here_1=0
    for j in range(n):
        if(a[j]=='0'):
            continue
        else:
            here_1=j
            break
    a=a[here_1:n]
    return a

def modulo_2_div(t,c):
    check=len(c)
    lent=len(t)
    t=remove_starting_zero(t,lent)
    len_t=len(t)
    i=0
    while len_t>=check :
        if i==0:
            dividend=t[i:i+check]
        else:
            to_add=t[i+res:i+res+x]
            dividend=result+to_add
        result=xor(dividend,c,check)
        res=len(result)
        x=check-res
        len_t-=x
        i+=x
    r=result
    return r

def correct_or_not(p,c):
    remainder=modulo_2_div(p,c)
    if(remainder==''):
        return 0 #OK Acknowledgement 0
    else:
        return 1 #NAK acknowledgement 1

def message_retrieval(pt,c): #client side message from pt
    chop=len(c)
    where=len(pt)
    upto=where-chop+1
    m=pt[0:upto]
    return m

def count_zeros(a,n):
    i=0
    for j in range(n):
        if(a[j]=='0'):
            i+=1
        else:
            break
    return i

c='100000111'
m='0001011001001001011'
print(m)
tx=create_t_from_m(m,c)
print(f"T(x)={tx}")

remainder=modulo_2_div(tx,c)
print(f"Remainder={remainder}")

pt=create_p_from_t(tx,remainder) #t='11010000'
print(f"P(x)={pt}")

ok_or_nak=correct_or_not('101100100100101110010011',c)
print(f"ok_or_nak={ok_or_nak}")

m=message_retrieval(pt,c)
print(f"M(x)={m}")
