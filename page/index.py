from page.login import Login
from page.register import Register


class Index:
    def geto_login(self):

        return Login()

    def goto_register(self):
        return Register()