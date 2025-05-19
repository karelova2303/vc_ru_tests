from vc_ru_tests.models.pages.main_page import MainPage
from vc_ru_tests.models.pages.sidebar_components_page import SideBarComponentsPage


class Application:
    def __init__(self):
        self.main_page = MainPage()
        self.sidebar_components = SideBarComponentsPage()

app = Application()