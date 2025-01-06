# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")
# ls = [1,2,3,4,5]
# print(ls)
# di = {"abc":10, "xyz":20, "pqr":30}
# print(di.items())
# print(di.keys())
# print(di.values())
# str = "Programming"
# letters = str.split()
# print(letters)

str = "Her name is xyz. Her name is very weird. Her brother name is pqr. His name is also weird."

# dic = {}
# for word in str.split():
#     if word in dic.keys():
#         dic[word] += 1
#     else:
#         dic[word] = 1

# print(dic)
words = str.split()
dic = {word:words.count(word) for word in words}
print(dic)


