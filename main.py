# input -> "aabcd"
# output -> a-2 b-1 c-1 d-1



# #N**2
# N = len(data)
# def strcounter(data):
#     for sym in data: # len(data)
#         counter = 0 
#         for sym2 in data:# len(data)
#             if sym == sym2:
#                 counter += 1 
#         print(sym, counter)


# strcounter("aabcd")




# #N*M
# # N = len(data)   M = set(data)
# def strcounter(data):
#     for sym in set(data): #set(data)
#         counter = 0 
#         for sym2 in data:# len(data)
#             if sym == sym2:
#                 counter += 1 
#         print(sym, counter)


# strcounter("aabcd")



# N
#  N = len(data) 
# def strcounter(data):
#     str_count = {}
#     for sym in data: 
#         str_count[sym] = str_count.get(sym,0) + 1 # add or update
    
#     # print(str_count.items()) # dict -> tuple
#     for s, c in str_count.items():
#         print(s,c)

# strcounter("aabcdgrasedgsdfgseryety")


# 1 - зарегистрироваться на github  https://github.com/
# 2 - скачать gitbash https://gitforwindows.org/
# 3 скачать https://desktop.github.com/



# 1 способ через терминал

# - создать удаленный репозиторий 
# - выполнить команды в терминале: 
# git init 
# git add .
# git commit -m "first commit"
# git branch -M main
# git remote add origin https://github.com/RyT32/test_test.git
# git push -u origin main












# famaly = {}
# print()
# famaly["dad"] = 1
# print(famaly)
# famaly["mom"] = 1
# print(famaly)
# # famaly["child"] = 1 #add
# # print(famaly)
# famaly["child"] = famaly.get("child",0) + 1 # update
# print(famaly)











# # set - множество, неупорядоченный тип данных, который хранит уникальный значения
# x = set()

# v = {1,1,2,3}
# print(v)

# r = {} #dict
# print(type(r))

# u = {1} # set
# print(type(u))

# l = [1,1,2,2,3,4,5]
# print(l)
# # s_l = set(l)
# # l = list(s_l)

# l = list(set(l))
# print(l)




