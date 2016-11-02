#def sum(a,b):
    #c=a%b
    #return c
#print (sum(1.0,123.))

#a= len("sai")
##print (a)


#a= "bhavana"
#print(a[7:10])


#danton = "De l'audace, encore de l'audace, toujours de l'audace"
#a= danton.find("audace")
#b= danton.find("'audace",a)
#print (b)

#a="sai"
#print a[1:]

# #def print_number(n):
#  #   i=0
#  #   while i<n:
#         i=i+1
#         print i
# print (print_number(3))


# x="aaaaa"
# z="aa"
# y= x.find(z)
# i=x.find(z,y-1)
# # e=x.find(z,i+1)
# # w=x.find(z,e+1)
# # f=x.find(z,w+1)
# # #i=x[y+1:]
# print (i)

# def last(a,b):
#     last_pos= -1
#     while True:
#         pos=a.find(b,last_pos+1)
#         if pos== -1:
#             return last_pos
#         last_pos=pos
#
# print last("aaaaa","b")

def no_of_days(date_of_birth,current_date):
    days=0
    n=date_of_birth
    x=current_date
    if n != x:
        days= days+1
    else:
        return days

print no_of_days()

