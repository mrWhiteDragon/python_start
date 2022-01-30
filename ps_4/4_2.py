# 1 способ без генератора:
# num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = []
# for n in range(len(num_list) - 1):
#     if num_list[n] < num_list[n + 1]:
#         result.append(num_list[n + 1])
# print(result)

# 2 способ c генератором:
num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [num_list[n + 1] for n in range(len(num_list) - 1) if num_list[n] < num_list[n + 1]]
print(result)