
class Screen(object):
    @property
    def width(self):
        return self._weight
    
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError("height must be an integer")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError("height must be an integer")
        self._height = value
    
    @property
    def resolution(self):
        return self._height*self._width

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')