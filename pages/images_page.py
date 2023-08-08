from pages.base_page import BasePage


class ImageSearchPage(BasePage):

    def switch_to_window(self, win_number):
        return self.driver.switch_to.window(
            self.driver.window_handles[win_number]
            )
