

def encrypt(filename,key):
    file=open(filename,'rb')
    cfile=open(filename+'c','wb')
    plain=str(file.read())
    str_list=[]
    key_list=[]
    c1=[]
    c2=[]
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X" "Y","Z"," ","@","*","%","1","2","3","4","5","6","7","8","9","0","$","\n"]
    key_len=len(key)
    text_len=len(plain)
    
    overLap= text_len % key_len
    leftover= key[:overLap]
    random= text_len-overLap
    random = text_len/key_len
    key = (int(random)*key)+leftover
    
    for i in key:
        n=alphabet.index(i.upper())
        key_list.append(n)
    for i in plain:
        n=alphabet.index(i.upper())
        str_list.append(n)
    i=0
    while i<text_len:
        c1.append((str_list[i]+key_list[i])%41)
        i+=1
    for i in c1:
        c2.append(alphabet[i])
    cypher=''.join(c2)
    print cypher
    cfile.write(cypher)

def decrypt(filename,key):
    file=open(filename+'c','rb')
    plain=str(file.read())
    str_list=[]
    key_list=[]
    c1=[]
    c2=[]
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X" "Y","Z"," ","@","*","%","1","2","3","4","5","6","7","8","9","0","$","\n"]
    key_len=len(key)
    text_len=len(plain)
    
    overLap= text_len % key_len
    leftover= key[:overLap]
    random= text_len-overLap
    random = text_len/key_len
    key = (int(random)*key)+leftover
    
    for i in key:
        n=alphabet.index(i.upper())
        key_list.append(n)
    for i in plain:
        n=alphabet.index(i.upper())
        str_list.append(n)
    i=0
    while i<text_len:
        c1.append((str_list[i]-key_list[i])%41)
        i+=1
    for i in c1:
        c2.append(alphabet[i])
    cypher=''.join(c2)
    print cypher
encrypt('b','into')
decrypt('b','into')