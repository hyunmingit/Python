
#[시작점:끝점:증강값]

oneLine ="this is one line string"
print(oneLine)
print("길이 : ", len(oneLine))
print(oneLine[0:4])
print(oneLine[:4])
print(oneLine[:])
print(oneLine[::2]) #짝수자리만

print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])

subString = oneLine[-11:]
print(subString)