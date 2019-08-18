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

def prod(L):
    getNumber = reduce(lambda x,y:x*y,L)
    return getNumber

    
if __name__ == "__main__":
    names=['Abcd','asdlAhs','aliBABA']
    afterNormalize = list(map(normalize,names))
    print("nametype:%s" % afterNormalize)

    print('3 * 5 * 7 * 9 =',prod([3,5,7,9]))
    if prod([3,5,7,9]) == 945:
        print("测试成功")
    else:
        print("测试失败")