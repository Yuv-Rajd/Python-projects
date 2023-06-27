# def partiotion(op,res,List):
#     final=[]
#     for i in range(0,len(List)):
#         for j in range(0,len(List)):
#             if op=='+':
#                 result = List[i] + List[j]
#             if op=='-':
#                 result = List[i] - List[j]
#             if op=='*':
#                 result = List[i] * List[j]
#             if op=='/':
#                 if List[i]==0 or List[j]==0:
#                     result=False
#                 else:
#                     result = List[i] / List[j]
#             if result == res:
#                 sub=[]
#                 sub.append(List[i])
#                 sub.append(List[j])
#                 if sub  in final or sub[::-1] in final:
#                     pass
#                 else:
#                     final.append(sub)
    
#     print("[")
#     for sub in final:
#         print(sub,end=",")
#     print("]")

# partiotion('-',7,[0,2,4,9,3,6,8])
# def passCode(passcode):
#     digits=[]
#     second=[]
#     third=[]

#     for i in range(0,len(passcode)):
#         digits.append(int(passcode[i][0]))
#     digits.sort()
#     for i in range(0,len(digits)):
#         for j in range(0,len(digits)):
#             if(digits[i]==int(passcode[j][0])):
#                 second.append(passcode[j][1])
#                 third.append(passcode[j][2])
#     print(passcode)
#     print(second)
#     print(third)



# def passCode2(passcode2):
#     newPasscode=[]
#     for i in range(0,len(passcode2)):
#         for j in range(0,len(passcode2)):
#             if i==int(passcode2[j][0]):
#                 newPasscode.append(passcode2[j])
#     for code in newPasscode:
#         print(code[1],end="")
#     print()
#     for code in newPasscode:
#         print(code[2],end="")

# passcodes=["5sd","4hg","3fs","2df","1jk","6df","7cv","8jh","9ui"]
# passCode2(passcodes)


# def passcode(code):
#     code.sort()
#     print(code)
#     for i in code:
#         try:
#             print(i[1],end="")
#         except IndexError:
#             pass
#     print()
#     for i in code:
#         try:
#             print(i[2],end="")
#         except IndexError:
#             pass

# codes=['1we','6fd','2','4df']
# passcode(codes)
sum=0
a=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if 
        