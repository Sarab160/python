#tupples
# is ma data modify nhi hota baqi same as list
num= int(input("G"))
namelist = ("sarab","umer","cheema")
for name in namelist:
    print(name)
    
#set
#ya bi list ki taara hi ha pr is ma data duplicate nhi aata 
#agr data duplicate enter hoga bi to ya show nhi kaara ga

namaset = {"sarab","umer","sarab"}
namaset.add("jutt")
#namaset.update("jutt","cheema")
for i in namaset:
    print(i)
