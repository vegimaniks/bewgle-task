from seleniumbase import BaseCase

class MyTestClass(BaseCase):

    def test_1(self):
        self.open('https://www.amazon.in/')
        self.maximize_window()
        #self.click('#twotabsearchtextbox')
        self.type('#twotabsearchtextbox','Laptop')
        self.wait(1)
        self.click("//input[@id='nav-search-submit-button']")
        self.click("//span[text()='HP']")
        self.click("//span[contains(text(),'Featured')]")
        self.click_link_text('Price: Low to High')
        price_elements = self.find_elements(".a-price-whole")
        actual_prices = [ float(price_element.text.replace(",", "")) for price_element in price_elements]
        sorted_prices = sorted(actual_prices)
        self.assert_equal(actual_prices, sorted_prices, "The prices are not sorted from low to high")
        self.quit()


    def test_2(self):
        self.open('https://bewgle.com/')
        self.maximize_window()
        self.driver.execute_script("window.scrollTo(0, 9000);")
        self.wait(1)
        self.click('//a[contains(text(),"Free Demo")]')
        self.assert_element_present("//h3[contains(text(),'Request a Demo')]")
        self.type('#input_2_1','Mani')
        self.type('#input_2_4','test@gmail.com')
        self.type('#input_2_3','India')
        self.type('#input_2_6','https://bewgle.com/')
        self.wait(2)
        




