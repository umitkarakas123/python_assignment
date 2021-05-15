sentence = input("Enter is a sentence: ")
sentence_list = list(sentence)
sentence_set = set(sentence)
my_dict = {}
for i in sentence_set :
    say = sentence_list.count(i)
    my_dict.update({i:say})
print(my_dict)