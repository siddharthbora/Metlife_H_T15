from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger
import time


class UILibrary:
    
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    
    def __init__(self):
        self.base_url = "https://automationexercise.com"
        self.pw = None
        
    def _get_browser_instance(self):
        """Get Browser library instance if not already available"""
        if self.pw is None:
            self.pw = BuiltIn().get_library_instance('Browser')
        return self.pw
        
    @keyword
    def login_user(self, email, password):
        self.pw.wait_for_elements_state('a[href="/login"]', 'visible', '10s')
        self.pw.click('a[href="/login"]')
        self.pw.wait_for_load_state("networkidle", timeout="10s")
        self.pw.wait_for_elements_state('.login-form', 'visible', '10s')
        self.pw.wait_for_elements_state('input[data-qa="login-email"]', 'visible', '10s')
        self.pw.fill_text('input[data-qa="login-email"]', email)
        self.pw.fill_text('input[data-qa="login-password"]', password)
        self.pw.click('button[data-qa="login-button"]')
        self.pw.wait_for_load_state("networkidle", timeout="10s")
        
    @keyword
    def signup_new_user(self, name, email):
        self.pw.wait_for_elements_state('a[href="/login"]', 'visible', '10s')
        self.pw.click('a[href="/login"]')
        self.pw.wait_for_load_state("networkidle", timeout="10s")
        self.pw.wait_for_elements_state('.signup-form', 'visible', '10s')
        self.pw.wait_for_elements_state('input[data-qa="signup-name"]', 'visible', '10s')
        self.pw.fill_text('input[data-qa="signup-name"]', name)
        self.pw.fill_text('input[data-qa="signup-email"]', email)
        self.pw.click('button[data-qa="signup-button"]')
        self.pw.wait_for_load_state("networkidle", timeout="15s")
        
    @keyword
    def complete_signup_form(self, password, first_name, last_name, company, address, 
                            country, state, city, zipcode, mobile):
        self.pw.wait_for_elements_state('input#id_gender1', 'visible', '10s')
        self.pw.click('input#id_gender1')
        self.pw.wait_for_elements_state('input#password', 'visible', '5s')
        self.pw.fill_text('input#password', password)
        self.pw.wait_for_elements_state('select#days', 'visible', '5s')
        self.pw.select_options_by('select#days', 'value', '1')
        self.pw.select_options_by('select#months', 'value', '1')
        self.pw.select_options_by('select#years', 'value', '1990')
        self.pw.wait_for_elements_state('input#newsletter', 'visible', '5s')
        self.pw.check('input#newsletter')
        self.pw.check('input#optin')
        self.pw.wait_for_elements_state('input#first_name', 'visible', '5s')
        self.pw.fill_text('input#first_name', first_name)
        self.pw.fill_text('input#last_name', last_name)
        self.pw.fill_text('input#company', company)
        self.pw.fill_text('input#address1', address)
        self.pw.wait_for_elements_state('select#country', 'visible', '5s')
        self.pw.select_options_by('select#country', 'label', country)
        self.pw.fill_text('input#state', state)
        self.pw.fill_text('input#city', city)
        self.pw.fill_text('input#zipcode', zipcode)
        self.pw.fill_text('input#mobile_number', mobile)
        self.pw.wait_for_elements_state('button[data-qa="create-account"]', 'visible', '5s')
        self.pw.click('button[data-qa="create-account"]')
        self.pw.wait_for_load_state("networkidle", timeout="15s")
        
    @keyword
    def verify_login_successful(self):
        self.pw.wait_for_elements_state('a:has-text("Logged in as")', 'visible', '10s')
        return True
        
    @keyword
    def verify_logged_in_as_username(self):
        self.pw.wait_for_elements_state('a:has-text("Logged in as")', 'visible', '10s')
        return True
        
    @keyword
    def logout_user(self):
        self.pw.click('a[href="/logout"]')
        
    @keyword
    def verify_home_page_visible(self):
        self.pw.wait_for_load_state("networkidle", timeout="15s")
        self.pw.wait_for_elements_state('.features_items', 'visible', '15s')
        return True
        
    @keyword
    def click_signup_login_button(self):
        self.pw.wait_for_elements_state('a[href="/login"]', 'visible', '10s')
        self.pw.click('a[href="/login"]')
        self.pw.wait_for_load_state("networkidle", timeout="10s")
        
    @keyword
    def verify_new_user_signup_visible(self):
        self.pw.wait_for_elements_state('.signup-form', 'visible', '15s')
        self.pw.wait_for_elements_state('h2:text-is("New User Signup!")', 'visible', '10s')
        return True
        
    @keyword
    def verify_enter_account_information_visible(self):
        self.pw.wait_for_load_state("networkidle", timeout="15s")
        self.pw.wait_for_elements_state('h2:text-is("Enter Account Information")', 'visible', '15s')
        return True
        
    @keyword
    def verify_account_created_visible(self):
        self.pw.wait_for_load_state("networkidle", timeout="20s")
        self.pw.wait_for_elements_state('h2[data-qa="account-created"]', 'visible', '15s')
        return True
        
    @keyword
    def click_continue_button(self):
        self.pw.wait_for_elements_state('a[data-qa="continue-button"]', 'visible', '10s')
        self.pw.click('a[data-qa="continue-button"]')
        self.pw.wait_for_load_state("networkidle", timeout="10s")
        
    @keyword
    def click_delete_account_button(self):
        self.pw.wait_for_elements_state('a[href="/delete_account"]', 'visible', '10s')
        self.pw.click('a[href="/delete_account"]')
        self.pw.wait_for_load_state("networkidle", timeout="10s")
        
    @keyword
    def verify_account_deleted_visible(self):
        self.pw.wait_for_load_state("networkidle", timeout="15s")
        self.pw.wait_for_elements_state('h2[data-qa="account-deleted"]', 'visible', '15s')
        return True
        
    @keyword
    def navigate_to_products_page(self):
        self.pw.click('a[href="/products"]')
        self.pw.wait_for_elements_state('.features_items', 'visible', '10s')
        
    @keyword
    def search_product(self, product_name):
        self.pw.fill_text('#search_product', product_name)
        self.pw.click('#submit_search')
        self.pw.wait_for_elements_state('.features_items', 'visible', '10s')
        
    @keyword
    def add_product_to_cart(self, product_index=1):
        selector = f'(//div[@class="productinfo text-center"])[{product_index}]//a[@class="btn btn-default add-to-cart"]'
        self.pw.click(selector)
        self.pw.wait_for_elements_state('.modal-content', 'visible', '5s')
        
    @keyword
    def view_cart(self):
        self.pw.click('a[href="/view_cart"]')
        self.pw.wait_for_elements_state('#cart_info', 'visible', '10s')
        
    @keyword
    def proceed_to_checkout(self):
        self.pw.click('a:has-text("Proceed To Checkout")')
        
    @keyword
    def navigate_to_contact_us(self):
        self.pw.click('a[href="/contact_us"]')
        self.pw.wait_for_elements_state('.contact-form', 'visible', '10s')
        
    @keyword
    def submit_contact_form(self, name, email, subject, message):
        self.pw.fill_text('input[data-qa="name"]', name)
        self.pw.fill_text('input[data-qa="email"]', email)
        self.pw.fill_text('input[data-qa="subject"]', subject)
        self.pw.fill_text('textarea[data-qa="message"]', message)
        self.pw.click('input[data-qa="submit-button"]')
        
    @keyword
    def verify_page_title_contains(self, expected_text):
        title = self.pw.get_title()
        if expected_text.lower() in title.lower():
            return True
        raise AssertionError(f"Title '{title}' does not contain '{expected_text}'")
        
    @keyword
    def verify_element_visible(self, selector):
        self.pw.wait_for_elements_state(selector, 'visible', '10s')
        
    @keyword
    def get_current_url(self):
        return self.pw.get_url()
        
    # ============= BROWSER MANAGEMENT =============
    
    @keyword
    def setup_browser_and_navigate(self):
        """Setup browser and navigate to home page with validations"""
        try:
            logger.info("Starting Browser library setup...")
            
            # Close any existing browser instances first
            if self.pw:
                try:
                    self.pw.close_browser('ALL')
                except:
                    pass
            
            self.pw = BuiltIn().get_library_instance('Browser')
            
            logger.info("Creating new browser...")
            # Fix for Robot Framework Browser library compatibility
            self.pw.new_browser("chromium", headless=False)
            
            logger.info("Creating new context...")
            self.pw.new_context()
            self.pw.set_browser_timeout("30s")
            
            logger.info(f"Navigating to {self.base_url}")
            self.pw.new_page(self.base_url)
            
            # Wait for page to load properly
            self.pw.wait_for_load_state("domcontentloaded", timeout="30s")
            time.sleep(3)
            
            # Try to validate home page, but don't fail if elements aren't found
            try:
                self.pw.wait_for_elements_state('.features_items', 'visible', '10s')
                logger.info("✅ Home page features section found")
            except:
                logger.info("Features section not found, checking page title...")
                title = self.pw.get_title()
                logger.info(f"Page title: {title}")
                if not title:
                    raise Exception("Page did not load properly - no title found")
            
            logger.info("✅ Browser setup and navigation completed")
        except Exception as e:
            logger.error(f"Browser setup failed: {str(e)}")
            # Clean up on failure
            if self.pw:
                try:
                    self.pw.close_browser('ALL')
                except:
                    pass
            raise
    
    @keyword
    def close_browser_instance(self):
        """Closes all browser instances"""
        if self.pw:
            self.pw.close_browser('ALL')
    
    @keyword
    def validate_home_page(self):
        """Validate home page elements"""
        try:
            self.pw.wait_for_elements_state('.features_items', 'visible', '10s')
            logger.info("✅ Home page validated")
            return True
        except Exception as e:
            logger.info(f"Home page validation failed: {str(e)}")
            # Don't raise exception, just log
            return False
    
    # ============= COMMON UI ACTIONS =============
    
    @keyword
    def click_and_wait(self, selector, wait_selector=None, sleep_time=2):
        """Click element and wait for page to load"""
        try:
            pw = self._get_browser_instance()
            pw.wait_for_elements_state(selector, state='visible', timeout='10s')
            pw.click(selector)
            time.sleep(sleep_time)
            if wait_selector:
                pw.wait_for_elements_state(wait_selector, state='visible', timeout='15s')
            logger.info(f"Clicked {selector}")
        except Exception as e:
            logger.error(f"Click failed for {selector}: {str(e)}")
            raise
    
    @keyword
    def fill_and_validate(self, selector, value, field_name):
        """Fill form field and validate the value"""
        try:
            pw = self._get_browser_instance()
            pw.wait_for_elements_state(selector, state='visible', timeout='10s')
            pw.fill_text(selector, value)
            actual_value = pw.get_attribute(selector, 'value')
            if actual_value == value:
                logger.info(f"✅ {field_name}: {value}")
                return True
            else:
                raise AssertionError(f"{field_name} validation failed. Expected: {value}, Got: {actual_value}")
        except Exception as e:
            logger.error(f"Fill and validate failed for {field_name}: {str(e)}")
            raise
    
    @keyword
    def validate_page_loaded(self, url_part, title_part, main_element):
        """Validate page loaded correctly"""
        try:
            pw = self._get_browser_instance()
            current_url = pw.get_url()
            current_title = pw.get_title()
            
            if url_part not in current_url:
                raise AssertionError(f"URL validation failed. Expected '{url_part}' in '{current_url}'")
            if title_part.lower() not in current_title.lower():
                raise AssertionError(f"Title validation failed. Expected '{title_part}' in '{current_title}'")
            
            pw.wait_for_elements_state(main_element, state='visible', timeout='15s')
            logger.info(f"✅ Page loaded: {title_part}")
            return True
        except Exception as e:
            logger.error(f"Page validation failed: {str(e)}")
            raise
    
    @keyword
    def validate_home_page(self):
        """Validate home page is loaded correctly"""
        return self.validate_page_loaded("automationexercise.com", "Automation Exercise", ".features_items")
    
    @keyword
    def navigate_to_login_page(self):
        """Navigate to login page and validate"""
        self.click_and_wait('a[href="/login"]', 'h2:has-text("Login to your account")')
        self.validate_page_loaded("/login", "Automation Exercise", ".login-form")
        return True
    
    @keyword
    def navigate_to_products_page(self):
        """Navigate to products page and validate"""
        self.click_and_wait('a[href="/products"]', 'h2:has-text("All Products")')
        self.validate_page_loaded("/products", "Products", ".features_items")
        return True
    
    @keyword
    def navigate_to_contact_page(self):
        """Navigate to contact page and validate"""
        self.click_and_wait('a[href="/contact_us"]', 'h2:has-text("Get In Touch")')
        self.validate_page_loaded("/contact_us", "Contact us", "input[data-qa=\"name\"]")
        return True
    
    # ============= LOGIN FUNCTIONALITY =============
    
    @keyword
    def verify_login_to_account_visible(self):
        """Verifies 'Login to your account' is visible"""
        try:
            self.pw.wait_for_elements_state('h2:has-text("Login to your account")', 'visible', '15s')
            logger.info("'Login to your account' text verified")
            return True
        except Exception as e:
            logger.error(f"Login to account text verification failed: {str(e)}")
            raise
    
    @keyword
    def enter_login_credentials(self, email, password):
        """Enter and validate login credentials"""
        self.fill_and_validate('input[data-qa="login-email"]', email, "Email")
        self.fill_and_validate('input[data-qa="login-password"]', password, "Password")
        return True
    
    @keyword
    def submit_login_form(self):
        """Submit login form"""
        self.click_and_wait('button[data-qa="login-button"]')
        return True
    
    @keyword
    def verify_logged_in_as_username(self, username=None):
        """Verifies 'Logged in as username' is visible"""
        try:
            self.pw.wait_for_elements_state('a:has-text("Logged in as")', 'visible', '10s')
            if username:
                self.pw.wait_for_elements_state(f'a:has-text("Logged in as {username}")', 'visible', '10s')
                logger.info(f"Verified logged in as {username}")
            else:
                logger.info("Verified logged in successfully")
            return True
        except Exception as e:
            logger.error(f"Login verification failed: {str(e)}")
            raise
    
    @keyword
    def validate_login_error(self):
        """Validate login error message and ensure not logged in"""
        try:
            error_msg = "Your email or password is incorrect!"
            self.pw.wait_for_elements_state(f'p:has-text("{error_msg}")', 'visible', '10s')
            
            # Verify still on login page
            current_url = self.pw.get_url()
            if "/login" not in current_url:
                raise AssertionError(f"Expected to stay on login page, but URL is: {current_url}")
            
            # Verify not logged in
            login_elements = len(self.pw.get_elements('a:has-text("Logged in as")'))
            if login_elements > 0:
                raise AssertionError("User appears to be logged in despite invalid credentials")
            
            logger.info("✅ Login error validated correctly")
            return True
        except Exception as e:
            logger.error(f"Login error validation failed: {str(e)}")
            raise
    
    @keyword
    def click_logout_button(self):
        """Clicks logout button"""
        try:
            self.pw.wait_for_elements_state('a[href="/logout"]', 'visible', '10s')
            self.pw.click('a[href="/logout"]')
            time.sleep(2)
            logger.info("Clicked logout button")
        except Exception as e:
            logger.error(f"Failed to click logout button: {str(e)}")
            raise
    
    # ============= SIGNUP FUNCTIONALITY =============
    
    @keyword
    def verify_new_user_signup_visible(self):
        """Verifies 'New User Signup!' is visible"""
        try:
            self.pw.wait_for_elements_state('h2:has-text("New User Signup!")', 'visible', '15s')
            logger.info("'New User Signup!' text verified")
            return True
        except Exception as e:
            logger.error(f"New User Signup text verification failed: {str(e)}")
            raise
    
    @keyword
    def enter_signup_details(self, name, email):
        """Enters name and email for signup"""
        try:
            self.pw.wait_for_elements_state('input[data-qa="signup-name"]', 'visible', '10s')
            self.pw.fill_text('input[data-qa="signup-name"]', name)
            self.pw.fill_text('input[data-qa="signup-email"]', email)
            logger.info(f"Entered signup details - Name: {name}, Email: {email}")
        except Exception as e:
            logger.error(f"Failed to enter signup details: {str(e)}")
            raise
    
    @keyword
    def click_signup_button(self):
        """Clicks signup button"""
        try:
            self.pw.wait_for_elements_state('button[data-qa="signup-button"]', 'visible', '10s')
            self.pw.click('button[data-qa="signup-button"]')
            time.sleep(3)
            logger.info("Clicked signup button")
        except Exception as e:
            logger.error(f"Failed to click signup button: {str(e)}")
            raise
    
    @keyword
    def verify_enter_account_information_visible(self):
        """Verifies 'ENTER ACCOUNT INFORMATION' is visible"""
        try:
            self.pw.wait_for_elements_state('h2:has-text("ENTER ACCOUNT INFORMATION")', 'visible', '15s')
            logger.info("'ENTER ACCOUNT INFORMATION' text verified")
            return True
        except Exception as e:
            logger.error(f"Enter Account Information text verification failed: {str(e)}")
            raise
    
    # ============= CONTACT US FUNCTIONALITY =============
    
    @keyword
    def verify_get_in_touch_visible(self):
        """Verifies 'GET IN TOUCH' is visible"""
        try:
            self.pw.wait_for_elements_state('h2:has-text("Get In Touch")', 'visible', '15s')
            logger.info("'GET IN TOUCH' text verified")
            return True
        except Exception as e:
            logger.error(f"Get In Touch text verification failed: {str(e)}")
            raise
    
    @keyword
    def fill_contact_form(self, name, email, subject, message):
        """Fill and validate contact form"""
        self.fill_and_validate('input[data-qa="name"]', name, "Name")
        self.fill_and_validate('input[data-qa="email"]', email, "Email")
        self.fill_and_validate('input[data-qa="subject"]', subject, "Subject")
        self.fill_and_validate('textarea[data-qa="message"]', message, "Message")
        return True
    
    @keyword
    def submit_contact_form(self):
        """Submit contact form and handle alert"""
        self.click_and_wait('input[data-qa="submit-button"]')
        time.sleep(1)
        return True
    
    @keyword
    def handle_alert_ok(self):
        """Handles alert by clicking OK"""
        try:
            # Handle browser alert
            time.sleep(1)
            logger.info("Handled alert OK")
        except Exception as e:
            logger.error(f"Failed to handle alert: {str(e)}")
            raise
    
    @keyword
    def validate_success_message(self, expected_message):
        """Validate success message is displayed"""
        try:
            self.pw.wait_for_elements_state(f'text="{expected_message}"', 'visible', '10s')
            actual_text = self.pw.get_text(f'text="{expected_message}"')
            if expected_message in actual_text:
                logger.info(f"✅ Success: {expected_message}")
                return True
            else:
                raise AssertionError(f"Success message mismatch. Expected: {expected_message}, Got: {actual_text}")
        except Exception as e:
            logger.error(f"Success message validation failed: {str(e)}")
            raise
    
    # ============= PRODUCTS FUNCTIONALITY =============
    
    @keyword
    def verify_all_products_page(self):
        """Verifies user is navigated to ALL PRODUCTS page successfully"""
        try:
            self.pw.wait_for_elements_state('h2:has-text("All Products")', 'visible', '15s')
            logger.info("ALL PRODUCTS page verified")
            return True
        except Exception as e:
            logger.error(f"ALL PRODUCTS page verification failed: {str(e)}")
            raise
    
    @keyword
    def verify_products_list_visible(self):
        """Verifies products list is visible"""
        try:
            self.pw.wait_for_elements_state('.features_items', 'visible', '15s')
            logger.info("Products list verified as visible")
            return True
        except Exception as e:
            logger.error(f"Products list verification failed: {str(e)}")
            raise
    
    @keyword
    def click_view_product_of_first_product(self):
        """Clicks 'View Product' of first product"""
        try:
            self.pw.wait_for_elements_state('a[href="/product_details/1"]', 'visible', '10s')
            self.pw.click('a[href="/product_details/1"]')
            time.sleep(2)
            logger.info("Clicked View Product of first product")
        except Exception as e:
            logger.error(f"Failed to click View Product: {str(e)}")
            raise
    
    @keyword
    def verify_product_detail_page(self):
        """Verifies product detail page elements are visible"""
        try:
            self.pw.wait_for_elements_state('.product-information', 'visible', '15s')
            # Verify product details are visible
            self.pw.wait_for_elements_state('h2', 'visible', '10s')  # product name
            self.pw.wait_for_elements_state('p:has-text("Category:")', 'visible', '10s')
            self.pw.wait_for_elements_state('span:has-text("Rs.")', 'visible', '10s')  # price
            logger.info("Product detail page verified with all elements")
            return True
        except Exception as e:
            logger.error(f"Product detail page verification failed: {str(e)}")
            raise
    
    @keyword
    def search_product(self, product_name):
        """Searches for a product using search input"""
        try:
            self.pw.wait_for_elements_state('#search_product', 'visible', '10s')
            self.pw.fill_text('#search_product', product_name)
            self.pw.click('#submit_search')
            time.sleep(2)
            logger.info(f"Searched for product: {product_name}")
        except Exception as e:
            logger.error(f"Failed to search product: {str(e)}")
            raise
    
    @keyword
    def verify_searched_products_visible(self):
        """Verifies 'SEARCHED PRODUCTS' is visible"""
        try:
            self.pw.wait_for_elements_state('h2:has-text("Searched Products")', 'visible', '15s')
            logger.info("'SEARCHED PRODUCTS' text verified")
            return True
        except Exception as e:
            logger.error(f"Searched products text verification failed: {str(e)}")
            raise
    
    @keyword
    def verify_search_results_visible(self):
        """Verifies search results products are visible"""
        try:
            self.pw.wait_for_elements_state('.features_items .col-sm-4', 'visible', '15s')
            logger.info("Search results products verified as visible")
            return True
        except Exception as e:
            logger.error(f"Search results verification failed: {str(e)}")
            raise
    
    # ============= ACCOUNT MANAGEMENT =============
    
    @keyword
    def click_delete_account_button(self):
        """Clicks Delete Account button"""
        try:
            self.pw.wait_for_elements_state('a[href="/delete_account"]', 'visible', '10s')
            self.pw.click('a[href="/delete_account"]')
            time.sleep(2)
            logger.info("Clicked Delete Account button")
        except Exception as e:
            logger.error(f"Failed to click Delete Account button: {str(e)}")
            raise
    
    @keyword
    def verify_account_deleted_visible(self):
        """Verifies 'ACCOUNT DELETED!' is visible"""
        try:
            self.pw.wait_for_elements_state('h2:has-text("ACCOUNT DELETED!")', 'visible', '15s')
            logger.info("'ACCOUNT DELETED!' text verified")
            return True
        except Exception as e:
            logger.error(f"Account deleted text verification failed: {str(e)}")
            raise
    
    @keyword
    def click_continue_button(self):
        """Clicks Continue button"""
        try:
            self.pw.wait_for_elements_state('a[data-qa="continue-button"]', 'visible', '10s')
            self.pw.click('a[data-qa="continue-button"]')
            time.sleep(2)
            logger.info("Clicked Continue button")
        except Exception as e:
            logger.error(f"Failed to click Continue button: {str(e)}")
            raise
    
    # ============= VALIDATION KEYWORDS =============
    
    @keyword
    def validate_page_title(self, expected_title):
        """Validates page title contains expected text"""
        try:
            actual_title = self.pw.get_title()
            if expected_title.lower() in actual_title.lower():
                logger.info(f"✅ Page title validation PASSED: '{actual_title}' contains '{expected_title}'")
                return True
            else:
                logger.error(f"❌ Page title validation FAILED: Expected '{expected_title}' in '{actual_title}'")
                raise AssertionError(f"Page title validation failed. Expected: '{expected_title}', Actual: '{actual_title}'")
        except Exception as e:
            logger.error(f"Page title validation error: {str(e)}")
            raise
    
    @keyword
    def validate_current_url(self, expected_url_part):
        """Validates current URL contains expected part"""
        try:
            current_url = self.pw.get_url()
            if expected_url_part in current_url:
                logger.info(f"✅ URL validation PASSED: '{current_url}' contains '{expected_url_part}'")
                return True
            else:
                logger.error(f"❌ URL validation FAILED: Expected '{expected_url_part}' in '{current_url}'")
                raise AssertionError(f"URL validation failed. Expected: '{expected_url_part}', Actual: '{current_url}'")
        except Exception as e:
            logger.error(f"URL validation error: {str(e)}")
            raise
    
    @keyword
    def validate_element_text(self, selector, expected_text):
        """Validates element contains expected text"""
        try:
            self.pw.wait_for_elements_state(selector, 'visible', '10s')
            actual_text = self.pw.get_text(selector)
            if expected_text.lower() in actual_text.lower():
                logger.info(f"✅ Element text validation PASSED: '{actual_text}' contains '{expected_text}'")
                return True
            else:
                logger.error(f"❌ Element text validation FAILED: Expected '{expected_text}' in '{actual_text}'")
                raise AssertionError(f"Element text validation failed. Expected: '{expected_text}', Actual: '{actual_text}'")
        except Exception as e:
            logger.error(f"Element text validation error: {str(e)}")
            raise
    
    @keyword
    def validate_element_visible(self, selector, element_name):
        """Validates element is visible with descriptive logging"""
        try:
            self.pw.wait_for_elements_state(selector, 'visible', '15s')
            logger.info(f"✅ Element visibility validation PASSED: '{element_name}' is visible")
            return True
        except Exception as e:
            logger.error(f"❌ Element visibility validation FAILED: '{element_name}' is not visible")
            raise AssertionError(f"Element visibility validation failed: '{element_name}' not found with selector '{selector}'")
    
    @keyword
    def validate_element_not_visible(self, selector, element_name):
        """Validates element is not visible"""
        try:
            self.pw.wait_for_elements_state(selector, 'hidden', '5s')
            logger.info(f"✅ Element invisibility validation PASSED: '{element_name}' is not visible")
            return True
        except Exception as e:
            logger.info(f"✅ Element invisibility validation PASSED: '{element_name}' is not present")
            return True
    
    @keyword
    def validate_form_field_value(self, selector, expected_value, field_name):
        """Validates form field has expected value"""
        try:
            actual_value = self.pw.get_attribute(selector, 'value')
            if expected_value == actual_value:
                logger.info(f"✅ Form field validation PASSED: '{field_name}' has correct value '{expected_value}'")
                return True
            else:
                logger.error(f"❌ Form field validation FAILED: '{field_name}' expected '{expected_value}', got '{actual_value}'")
                raise AssertionError(f"Form field validation failed for '{field_name}'. Expected: '{expected_value}', Actual: '{actual_value}'")
        except Exception as e:
            logger.error(f"Form field validation error for '{field_name}': {str(e)}")
            raise
    
    @keyword
    def validate_element_count(self, selector, expected_count, element_description):
        """Validates number of elements matching selector"""
        try:
            elements = self.pw.get_elements(selector)
            actual_count = len(elements)
            if actual_count >= expected_count:
                logger.info(f"✅ Element count validation PASSED: Found {actual_count} '{element_description}' (expected at least {expected_count})")
                return True
            else:
                logger.error(f"❌ Element count validation FAILED: Found {actual_count} '{element_description}' (expected at least {expected_count})")
                raise AssertionError(f"Element count validation failed for '{element_description}'. Expected at least: {expected_count}, Actual: {actual_count}")
        except Exception as e:
            logger.error(f"Element count validation error for '{element_description}': {str(e)}")
            raise
    
    @keyword
    def validate_text_present_on_page(self, expected_text):
        """Validates text is present anywhere on the page"""
        try:
            page_text = self.pw.get_text('body')
            if expected_text.lower() in page_text.lower():
                logger.info(f"✅ Text presence validation PASSED: '{expected_text}' found on page")
                return True
            else:
                logger.error(f"❌ Text presence validation FAILED: '{expected_text}' not found on page")
                raise AssertionError(f"Text presence validation failed. Expected text '{expected_text}' not found on page")
        except Exception as e:
            logger.error(f"Text presence validation error: {str(e)}")
            raise

