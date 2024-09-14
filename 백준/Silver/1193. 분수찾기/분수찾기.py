idx = int(input())
last_num_list = []
n = 1
biggest_num = 0
last_num = 0
while last_num < 10000000:
    last_num = int(n*(n+1)/2)
    last_num_list.append(last_num)
    n+=1

status = True
for i, current_num in enumerate(last_num_list):
    if status == True:
        if last_num_list[i-1] < idx and idx <= current_num:
            line_last_num = current_num
            status = False
if idx == 1:
    line_last_num = 1
# last_num_condition = [i for i in last_num_list if i <= idx]
# line = len(last_num_condition)

line = last_num_list.index(line_last_num)+1
start = int(line*(line-1)/2 +1)
end = int(line*(line+1)/2)
start_end_list = [i for i in range(start,end+1)]
start_end_idx = start_end_list.index(idx)

if line % 2 == 0:
    start = 1 + start_end_idx
    end = line - start_end_idx
else:
    start = line - start_end_idx
    end = 1 + start_end_idx

print(str(start)+'/'+str(end))