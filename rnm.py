ddzWords = ["rnm()","调用日你妈的函数","准备日你妈"]
class  people:#定义一个人员类
    def __init__(self, name):
        self.name = name
        self.mum = True
    def display(self):
        print(f"Name: {self.name}")
def fuck(person):
    if person.mum == False:
        print("不能日不存在的东西（")
        return False
    else:
        print("验证通过！")
        return True
        
def rnm():#ddz说要有rnm(),于是便有了rnm()(
    name = input("请输入名字：")
    person = people(name)
    person.display()
    if fuck(person) == True:
        for words in ddzWords:
            print("ddz:"+words)
    else:
        pass
if __name__ == "__main__":
    rnm()