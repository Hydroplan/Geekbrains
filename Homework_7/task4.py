import os

stat_of_sizes = {
    0: 0,
    10: 0,
    100: 0
}
# print(os.stat(os.path.join('task1.py')))
for i in os.walk('my_project'):
    for file in i[2]:
        print(file)
        size_of_file = os.stat(os.path.join(i[0], file))[6]

        if size_of_file == 0:
            stat_of_sizes[0] = stat_of_sizes[0]+1
        if 10 <= size_of_file > 0:
            stat_of_sizes[10] = stat_of_sizes[10] + 1
        if 100 <= size_of_file > 10:
            stat_of_sizes[100] = stat_of_sizes[100] + 1

print(stat_of_sizes)
