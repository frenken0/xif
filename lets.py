print("""
Shell Chooser, Coded By Gilz.
Indonesian Hacker Rulez
""")
list = []
zz = input("List Shell: ")
ch = input("Choose File Shell: ")
choose = [x.strip() for x in open(ch, mode="r").readlines()]
target = [i.strip() for i in open(zz, mode="r").readlines()]
for t in target:
    for choosee in choose:
        if t not in list:
           if choosee in t:
              print(t)
              list.append(t)
              open('result.txt', 'a').write(t+"\n")
        else:
           continue
