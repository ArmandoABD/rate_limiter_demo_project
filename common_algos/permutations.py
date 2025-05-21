from collections import defaultdict

card_freqs = defaultdict(lambda: -1)

input = ['a', 'a', 'b', 'c']
for card in input:
    card_freqs[card] += 1


list_answer = []
def explore_permutations(input_list, index, cur_list):
    if index == len(input_list):
        list_answer.append(cur_list[:])
        return
    for i in range(index, len(input_list)):
        cur_list.append(input_list[i])
        explore_permutations(input_list, index+1, cur_list)
        cur_list.pop()

listinput = [1, 2, 3, 4]
index = 0
curlist = []
explore_permutations(listinput, index, curlist)
print(list_answer)
