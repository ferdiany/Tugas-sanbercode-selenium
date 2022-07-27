import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterandLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    # test case 1
    def test_a_success_direct_to_registration_page(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/div/p/a").click() # klik link daftar disini 
        time.sleep(1)

        # validasi
        card_txt = browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[1]/h1").text
        btn_txt = browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[5]/button").text

        self.assertIn('daftar', card_txt)
        self.assertEqual(btn_txt, 'Daftar sekarang')

    # test case 2
    def test_b_failed_register_because_registered_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/div/p/a").click() # klik link daftar disini 
        time.sleep(1)
        browser.find_element(By.NAME,"username").send_keys("aew") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("aewtlefigebszykhwb@nthrl.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("aewtle") # isi kata sandi
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[5]/button").click() # klik tombol daftar sekarang
        time.sleep(5)

        # validasi
        response_message = browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[1]/div[1]/p").text

        self.assertEqual(response_message, 'Email atau username sudah terdaftar')

    # test case 3
    def test_c_success_register(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/div/p/a").click() # klik link daftar disini 
        time.sleep(1)
        browser.find_element(By.NAME,"username").send_keys("urg") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("urgwzwemitpeqpskum@kvhrw.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("urgwzwemi") # isi kata sandi
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[5]/button").click() # klik tombol daftar sekarang
        time.sleep(5)

        # validasi
        response_message = browser.find_element(By.XPATH,"/html/body/div/main/div/div[2]/p").text

        self.assertEqual(response_message, 'Selamat! Akun anda berhasil dibuat')

    # test case 4
    def test_d_failed_login_because_empty_email_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") # isi kata sandi
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol masuk
        time.sleep(3)

        # validasi
        response_email = browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[2]/div").text
        response_password = browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[3]/div").text
        
        self.assertIn('diperlukan', response_email)
        self.assertIn('diperlukan', response_password)

    # test case 5
    def test_e_failed_login_with_wrong_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("aewtlefigebszykhwb@nthrl.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("aewtle123456") # isi kata sandi
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol masuk
        time.sleep(5)

        # validasi
        response_message = browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[2]/p").text

        self.assertEqual(response_message, 'Kata Sandi Salah')

    # test case 6
    def test_f_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("wou71338@jeoce.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("wou71338") # isi kata sandi
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/main/div/div/form/div[4]/button").click() # klik tombol masuk
        time.sleep(10)

        # validasi
        validation = browser.find_element(By.XPATH,"/html/body/div/nav/div/div[2]/div").text

        self.assertIn('Hai!', validation)

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()
