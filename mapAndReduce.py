#python内建了map()和reduce()函数
from functools import reduce


def normalize(getTheName):
    print("参数类型：%s " % getTheName.__class__)
    if getTheName.istitle():
        return getTheName
    else:
        first = getTheName[0]
        setStr = first.upper()+getTheName[1:].lower()
        return setStr


if __name__ == "__main__":
    names=['Abcd','asdlAhs','aliBABA']
    afterNormalize = list(map(normalize,names))
    print(afterNormalize)