with open('nomes2.txt', 'w') as file:
    file.write('Ana\nCarlos\nBruno')
    file.write('\n21anos\n23anos\n25anos')

with open('nomes2.txt', 'r') as file:
    print(file.read())