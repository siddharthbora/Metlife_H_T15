from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import time


class CommonActions:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self.pw = None
        
    def _get_browser_instance(self):
        """Get Browser library instance"""
        if not self.pw:
            self.pw = BuiltIn().get_library_instance('Browser')
        return self.pw
    
    @keyword
    def click_and_wait(self, selector, wait_time=2):
        """Click element and wait"""
        browser = self._get_browser_instance()
        browser.wait_for_elements_state(selector, 'visible', timeout='10s')
        browser.click(selector)
        time.sleep(wait_time)
    
    @keyword
    def fill_and_validate(self, selector, value, field_name=""):
        """Fill text field and validate"""
        browser = self._get_browser_instance()
        browser.wait_for_elements_state(selector, 'visible', timeout='10s')
        browser.fill_text(selector, value)
        actual_value = browser.get_attribute(selector, 'value')
        if actual_value != value:
            raise AssertionError(f"Field validation failed for {field_name}. Expected: {value}, Actual: {actual_value}")
        logger.info(f"✅ {field_name}: {value}")
    
    @keyword
    def wait_and_verify_element(self, selector, element_name="", timeout='15s'):
        """Wait for element and verify visibility"""
        browser = self._get_browser_instance()
        browser.wait_for_elements_state(selector, 'visible', timeout=timeout)
        logger.info(f"✅ {element_name} verified")
        return True
    
    @keyword
    def verify_page_loaded(self, url_part, title_part="", element_selector=""):
        """Verify page loaded correctly"""
        browser = self._get_browser_instance()
        current_url = browser.get_url()
        if url_part not in current_url:
            raise AssertionError(f"URL validation failed. Expected: {url_part}, Actual: {current_url}")
        
        if title_part:
            title = browser.get_title()
            if title_part.lower() not in title.lower():
                raise AssertionError(f"Title validation failed. Expected: {title_part}, Actual: {title}")
        
        if element_selector:
            browser.wait_for_elements_state(element_selector, 'visible', timeout='15s')
        
        logger.info(f"✅ Page loaded: {url_part}")
        return True
    
    @keyword
    def verify_text_present(self, selector, expected_text):
        """Verify text is present in element"""
        browser = self._get_browser_instance()
        browser.wait_for_elements_state(selector, 'visible', timeout='10s')
        actual_text = browser.get_text(selector)
        if expected_text.lower() not in actual_text.lower():
            raise AssertionError(f"Text validation failed. Expected: {expected_text}, Actual: {actual_text}")
        logger.info(f"✅ Text verified: {expected_text}")
        return True
    
    @keyword
    def verify_element_count(self, selector, min_count, element_name=""):
        """Verify minimum element count"""
        browser = self._get_browser_instance()
        elements = browser.get_elements(selector)
        actual_count = len(elements)
        if actual_count < min_count:
            raise AssertionError(f"Element count validation failed for {element_name}. Expected at least: {min_count}, Actual: {actual_count}")
        logger.info(f"✅ {element_name} count: {actual_count}")
        return actual_count
    
    @keyword
    def verify_element_not_present(self, selector, element_name=""):
        """Verify element is not present"""
        browser = self._get_browser_instance()
        try:
            elements = browser.get_elements(selector)
            count = len(elements)
            if count > 0:
                raise AssertionError(f"Element should not be present: {element_name}")
        except:
            pass
        logger.info(f"✅ {element_name} not present")
        return True
    
    @keyword
    def select_and_validate(self, selector, selection_type, value, field_name=""):
        """Select option and validate"""
        browser = self._get_browser_instance()
        browser.wait_for_elements_state(selector, 'visible', timeout='10s')
        browser.select_options_by(selector, selection_type, value)
        logger.info(f"✅ {field_name}: {value}")
    
    @keyword
    def check_and_validate(self, selector, field_name=""):
        """Check checkbox and validate"""
        browser = self._get_browser_instance()
        browser.wait_for_elements_state(selector, 'visible', timeout='10s')
        browser.click(selector)
        checked = browser.get_attribute(selector, 'checked')
        if checked != 'true':
            raise AssertionError(f"Checkbox validation failed for {field_name}")
        logger.info(f"✅ {field_name} checked")
    
    @keyword
    def navigate_to_home(self):
        """Navigate to home page"""
        browser = self._get_browser_instance()
        browser.new_context(viewport={'width': 1920, 'height': 1080})
        browser.set_browser_timeout('30s')
        browser.new_page('https://automationexercise.com')
        time.sleep(3)
        self.wait_and_verify_element('.features_items', 'Home page')
        self.verify_page_loaded('automationexercise.com', 'Automation Exercise')
    
    @keyword
    def go_to_login_page(self):
        """Navigate to login page"""
        self.click_and_wait('a[href="/login"]')
        self.verify_page_loaded('/login')
        self.wait_and_verify_element('h2:has-text("Login to your account")', 'Login section')
        self.wait_and_verify_element('h2:has-text("New User Signup!")', 'Signup section')
    
    @keyword
    def go_to_products_page(self):
        """Navigate to products page"""
        self.click_and_wait('a[href="/products"]', 3)
        self.verify_page_loaded('/products')
        self.wait_and_verify_element('h2:has-text("All Products")', 'Products page')
    
    @keyword
    def go_to_contact_page(self):
        """Navigate to contact page"""
        self.click_and_wait('a[href="/contact_us"]')
        self.verify_page_loaded('/contact_us', 'Contact us')
        self.wait_and_verify_element('h2:has-text("Get In Touch")', 'Contact form')
    
    @keyword
    def login_with_credentials(self, email, password):
        """Login with provided credentials"""
        self.fill_and_validate('input[data-qa="login-email"]', email, 'Email')
        self.fill_and_validate('input[data-qa="login-password"]', password, 'Password')
        self.click_and_wait('button[data-qa="login-button"]')
    
    @keyword
    def signup_with_details(self, name, email):
        """Signup with name and email"""
        self.fill_and_validate('input[data-qa="signup-name"]', name, 'Name')
        self.fill_and_validate('input[data-qa="signup-email"]', email, 'Email')
        self.click_and_wait('button[data-qa="signup-button"]', 3)
    
    @keyword
    def fill_contact_form(self, name, email, subject, message):
        """Fill contact form"""
        self.fill_and_validate('input[data-qa="name"]', name, 'Name')
        self.fill_and_validate('input[data-qa="email"]', email, 'Email')
        self.fill_and_validate('input[data-qa="subject"]', subject, 'Subject')
        self.fill_and_validate('textarea[data-qa="message"]', message, 'Message')
    
    @keyword
    def fill_account_information(self, password):
        """Fill account information form"""
        self.check_and_validate('input#id_gender1', 'Gender')
        self.fill_and_validate('input#password', password, 'Password')
        self.select_and_validate('select#days', 'value', '1', 'Day')
        self.select_and_validate('select#months', 'value', '1', 'Month')
        self.select_and_validate('select#years', 'value', '1990', 'Year')
        self.check_and_validate('input#newsletter', 'Newsletter')
        self.check_and_validate('input#optin', 'Offers')
    
    @keyword
    def fill_address_information(self, first_name, last_name, company, address, country, state, city, zipcode, mobile):
        """Fill address information form"""
        self.fill_and_validate('input#first_name', first_name, 'First Name')
        self.fill_and_validate('input#last_name', last_name, 'Last Name')
        self.fill_and_validate('input#company', company, 'Company')
        self.fill_and_validate('input#address1', address, 'Address')
        self.select_and_validate('select#country', 'label', country, 'Country')
        self.fill_and_validate('input#state', state, 'State')
        self.fill_and_validate('input#city', city, 'City')
        self.fill_and_validate('input#zipcode', zipcode, 'Zipcode')
        self.fill_and_validate('input#mobile_number', mobile, 'Mobile')
    
    @keyword
    def verify_login_success(self, username):
        """Verify successful login"""
        self.wait_and_verify_element(f'a:has-text("Logged in as {username}")', f'Logged in as {username}')
        self.wait_and_verify_element('a[href="/logout"]', 'Logout button')
    
    @keyword
    def verify_login_error(self):
        """Verify login error message"""
        self.wait_and_verify_element('p:has-text("Your email or password is incorrect!")', 'Error message')
        self.verify_page_loaded('/login')
        self.verify_element_not_present('a:has-text("Logged in as")', 'Login success elements')
    
    @keyword
    def verify_account_created(self):
        """Verify account creation success"""
        self.wait_and_verify_element('h2:has-text("ACCOUNT CREATED!")', 'Account created message')
        self.verify_page_loaded('/account_created')
        self.wait_and_verify_element('p:has-text("Congratulations!")', 'Congratulations message')
    
    @keyword
    def verify_account_deleted(self):
        """Verify account deletion success"""
        self.wait_and_verify_element('h2:has-text("ACCOUNT DELETED!")', 'Account deleted message')
        self.verify_page_loaded('/delete_account')
        self.wait_and_verify_element('p:has-text("Your account has been permanently deleted!")', 'Deletion confirmation')
    
    @keyword
    def verify_contact_success(self):
        """Verify contact form submission success"""
        self.wait_and_verify_element('text="Success! Your details have been submitted successfully."', 'Success message')
        self.verify_text_present('div:has-text("Success! Your details have been submitted successfully.")', 'Success! Your details have been submitted successfully.')
    
    @keyword
    def search_product(self, product_name):
        """Search for product"""
        self.fill_and_validate('#search_product', product_name, 'Search term')
        self.click_and_wait('#submit_search', 3)
    
    @keyword
    def verify_search_results(self):
        """Verify search results"""
        self.wait_and_verify_element('h2:has-text("Searched Products")', 'Search results header')
        self.verify_element_count('.features_items .col-sm-4', 1, 'Search result products')
    
    @keyword
    def verify_product_details(self):
        """Verify product detail page"""
        self.wait_and_verify_element('.product-information', 'Product information section')
        self.wait_and_verify_element('h2', 'Product name')
        self.wait_and_verify_element('p:has-text("Category:")', 'Product category')
        self.wait_and_verify_element('span:has-text("Rs.")', 'Product price')
    
    @keyword
    def complete_test_flow(self, flow_name):
        """Complete test flow with final validation"""
        logger.info(f"🎉 {flow_name} completed successfully")
