from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 创建一个带代理的浏览器实例
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=http://127.0.0.1:4780')
# chrome_options.add_argument('--headless')  # 使用无头模式运行，不显示浏览器窗口

# 创建一个浏览器实例
driver = webdriver.Chrome(options=chrome_options)

# 打开登录页面
driver.get('http://libzwyy.jlu.edu.cn/#/ic/home')

# 创建一个WebDriverWait对象，等待最多3秒
wait = WebDriverWait(driver, 3)

# 填写用户名和密码
# 使用XPath和placeholder属性来定位输入框
# username_input = driver.find_element_by_xpath('//input[@placeholder="请输入统一账号"]')
# password_input = driver.find_element_by_xpath('//input[@placeholder="请输入一卡通系统密码"]')

# 等待输入框出现（根据placeholder属性定位）
username_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="请输入统一账号"]')))
password_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="请输入一卡通系统密码"]')))

username_input.send_keys('20200100700')
password_input.send_keys('133375')
 
# 使用XPath定位按钮并点击登录按钮
login_button = driver.find_element_by_xpath('//button[@class="el-button el-button--primary" and @style="width: 100%;"]')
login_button.click()

# 等待页面加载完成
# wait.until(EC.url_changes(driver.current_url))

# 检查HTTP状态码
# if "#/" in driver.current_url:
#     print("登录成功！")
# else:
#     print("登录失败！")

time.sleep(1)

# 修改当前页面的URL（模拟页面跳转）
new_url = 'http://libzwyy.jlu.edu.cn/#/ic/seatPredetermine/100652805'
driver.execute_script(f'window.history.replaceState("", "", "{new_url}")')
driver.refresh()

# 定位并点击选择日期
# input_element = driver.find_element_by_xpath('//input[@placeholder="选择日期"]')
date_input = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="选择日期"]')))
date_input.send_keys('2023-09-03')


time.sleep(3)

# 关闭浏览器
# driver.quit()

