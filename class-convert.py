good = ""
with open('input.txt', 'r') as file:
    content = file.read()
    good = content.replace("className", "class")
with open('output.txt', 'w') as f:
    f.write(good)
