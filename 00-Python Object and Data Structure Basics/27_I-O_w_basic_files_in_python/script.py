# open (and close) file and save on variable
# mode = 'r' (read, default), 'w' ((over)write), 'a' (append)
with open("test.txt", mode = 'a') as myfile:
  myfile.write('\nfive (added in python)')

with open("test.txt") as myfile:
  content = myfile.read()

print(content)

