with open('words.txt', 'r') as file:
    text = file.read()
    
text_list = text.lower().split(" ")

text_dict = {}

for word in text_list:
    if word in text_dict:
        text_dict[word] += 1
    else:
        text_dict[word] = 1
            
for key,value in text_dict.items():
    print(f"{key}:{value}")       
