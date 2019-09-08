from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
import pymongo
from bs4 import BeautifulSoup as bs
from PIL import Image
import time


EMAIL = 'test@test.com'
PASSWORD = '123456'


class CrackGeetest():
    # 初始化
    def __init__(self):
        self.url = 'https://account.geetest.com/login'
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 20)
        self.email = EMAIL
        self.password = PASSWORD

    def get_geetest_button(self):
        """
        获取初始验证按钮
        :return: 按钮对象
        """
        button = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'geetest_radar_tip')))
        return button

    def get_screenshot(self):
        """
        获取网页截图
        :return: 截图对象
        """
        screenshot = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        return screenshot

    def get_position(self):
        """
        获取验证码位置
        :return: 验证码位置元组
        """
        img = self.wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, 'geetest_cavas_img')))
        time.sleep(2)
        location = img.location
        size = img.size
        top, bottom, left, right = location['y'], location['y'] + \
            size['height'], location['x'], location['x']+size['width']
        return (top, bottom, left, right)

    def get_geetest_image(self, name='captcha.png'):
        """
        获取验证码图片
        :return: 图片对象
        """
        top, bottom, left, right = self.get_position()
        print('验证码位置:', top, bottom, left, right)
        screenshot = self.get_screenshot()
        captcha = screenshot.crop((left, top, right, bottom))
        return captcha

    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        slider = self.wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, 'geetest_slider_button')))
        return slider

    def is_pixel_equal(self, image1, image2, x, y):
        """
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x :位置X
        :param y :位置y
        """
        # 取两个图片的像素点
        pixel1 = image1.load()[x, y]
        pixel2 = image2.load()[x, y]
        threshold = 80
        if abs(pixel1[0]-pixel2[0]) < threshold and abs(pixel1[1]-pixel2[1]) < threshold and abs(pixel1[2]-pixel2[2]) < threshold:
            return True
        else:
            return False

    def get_gap(self, image1, image2):
        """
        获取缺口偏移量
        :param image1:不带缺口图片
        :param image2:带缺口图片
        :return:
        """
        left = 60
        for i in range(left, image1.size[0]):
            for j in range(image1.size[1]):
                if not self.is_pixel_equal(image1, image2, i, j):
                    left = i
                    return left
        return left

    # 模拟拖动
    # 公式:a为加速度 v为当前速度 v0为初速度 x为位移量 t为所需时间
    #x = v0 * t + 0.5 * a * t * t
    #v = v0 + a * t

    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance:偏移量
        :return:移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                a = -3
            # 初速度为v0
            v0 = v
            # 当前速度 v = v0 + at
            v = v0 + a * t
            #移动距离x = v0 * t + 0.5 * a * t * t
            move = v0 * t + 0.5 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹 rount()浮点数四舍五入
            track.append(round(move))

    # 按照运动轨迹拖动滑块
    def move_to_gap(self, slider, track):
        """
        滑动滑块到缺口处
        :param slider:滑块
        :param tracks:轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        for x in track:
            ActionChains(self.browser).move_by_offset(
                xoffset=x, yoffsef=0).perform()
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()
    button = get_geetest_button()
    button.click()
    # 点按呼出缺口
    slider = self.get_slider()
    slider.click()
