from appium import webdriver

# aapt dumps
# com.mysteel.android.steelphone
# com.mysteel.android.steelphone.ui.activity.IntroActivity
# 1 准备参数：告诉appium，你要打开哪个设备上的哪个app
desired_caps = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "huawei",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": True,
}

# 2 启动appium server程序
# 3 连接appium server。 把启动参数发送
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# 3