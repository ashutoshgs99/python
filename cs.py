def getcs():
	server=input("server: ")
	dbname=input("dbname: ")
	usr=input("usr: ")
	password=input("password: ")
	cs="Server=" + server + ";dbname="+ dbname + ";username=" + usr + ";password=" + password;
	return cs;
def cstolot1(cs):
    mylist=[]
    string1=""
    string2=""
    for i in range(len(cs)):
        pass
    return mylist

def cstolot1(cs):
    mylist=[]
    string1=str()
    string2=str()
    for i in range(len(cs)):
        while cs[i] != '=':
            string1.append(cs[i])
            i+=1
        while cs[i] != ';':
            string2.append(cs[i])
            i+=1
        mylist.append(tuple(string1,string2))
    return mylist

def cstolot(cs):
    mylist=[]
    for i in cs.split(";"):
        mylist.append(tuple(i.split("=")))
    return mylist

def cstodict(cs):
    return dict(catolot(cs))

def dicttocs(d):
    cs=""
    return cs

def main():
	cs=getcs()
	mylist=cstolot(cs)
	print(mylist)
	return
main()
