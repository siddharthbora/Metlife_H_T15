from http.client import responses

import requests
from robot.api.deco import keyword
from robot.api import logger
import json


class APILibrary:
    
    def __init__(self):
        self.base_url = "https://automationexercise.com/api"
        self.last_response = None
        self.stored_data = {}
        
    @keyword
    def get_all_products_list(self):
        url = f"{self.base_url}/productsList"
        logger.info(f"GET Request to: {url}")
        self.last_response = requests.get(url)
        logger.info(f"Response Status: {self.last_response.status_code}")
        logger.info(f"Response Time: {self.last_response.elapsed.total_seconds()}s")
        try:
            response_json = self.last_response.json()
            expected_data={
                          "id": 1,
                          "name": "Blue Top",
                          "price": "Rs. 500",
                          "brand": "Polo",
                          "category": {
                            "usertype": {
                              "usertype": "Women"
                            },
                            "category": "Tops"
                          }
            }
            actual_data = response_json["products"][0]
            assert expected_data==actual_data
            logger.info("Expected_Data = "+str(expected_data))
            logger.info("Actual_Data = "+str(actual_data))
            logger.info(f"Response JSON: {json.dumps(response_json)}")
            return response_json["products"]
        except:
            logger.info(f"Response Text: {self.last_response.text[:500]}")
        return self.last_response
        
    @keyword
    def get_all_brands_list(self):
        url = f"{self.base_url}/brandsList"
        logger.info(f"GET Request to: {url}")
        self.last_response = requests.get(url)
        logger.info(f"Response Status: {self.last_response.status_code}")
        logger.info(f"Response Time: {self.last_response.elapsed.total_seconds()}s")
        try:
            response_json = self.last_response.json()
            logger.info(f"Response JSON: {json.dumps(response_json, indent=2)[:500]}...")
        except:
            logger.info(f"Response Text: {self.last_response.text[:500]}")
        return self.last_response
        
    @keyword
    def search_product(self, product_name):
        url = f"{self.base_url}/searchProduct"
        data = {"search_product": product_name}
        logger.info(f"POST Request to: {url}")
        logger.info(f"Request Data: {data}")
        self.last_response = requests.post(url, data=data)
        logger.info(f"Response Status: {self.last_response.status_code}")
        logger.info(f"Response Time: {self.last_response.elapsed.total_seconds()}s")
        try:
            response_json = self.last_response.json()
            logger.info(f"Response JSON: {json.dumps(response_json)}")
            return response_json["products"]
        except:
            logger.info(f"Response Text: {self.last_response.text[:500]}")

        
    @keyword
    def verify_login_api(self, email, password):
        url = f"{self.base_url}/verifyLogin"
        data = {
            "email": email,
            "password": password
        }
        logger.info(f"POST Request to: {url}")
        logger.info(f"Request Data: email={email}, password=***")
        self.last_response = requests.post(url, data=data)
        logger.info(f"Response Status: {self.last_response.status_code}")
        logger.info(f"Response Time: {self.last_response.elapsed.total_seconds()}s")
        logger.info(f"Response Text: {self.last_response.text}")
        return self.last_response
        
    @keyword
    def create_user_account(self, name, email, password, title, birth_date, birth_month, 
                           birth_year, firstname, lastname, company, address1, address2, 
                           country, state, city, zipcode, mobile_number):
        url = f"{self.base_url}/createAccount"
        data = {
            "name": name,
            "email": email,
            "password": password,
            "title": title,
            "birth_date": birth_date,
            "birth_month": birth_month,
            "birth_year": birth_year,
            "firstname": firstname,
            "lastname": lastname,
            "company": company,
            "address1": address1,
            "address2": address2,
            "country": country,
            "state": state,
            "city": city,
            "zipcode": zipcode,
            "mobile_number": mobile_number
        }
        logger.info(f"POST Request to: {url}")
        logger.info(f"Creating account for: {email}")
        self.last_response = requests.post(url, data=data)
        logger.info(f"Response Status: {self.last_response.status_code}")
        logger.info(f"Response Time: {self.last_response.elapsed.total_seconds()}s")
        logger.info(f"Response Text: {self.last_response.text}")
        return self.last_response
        
    @keyword
    def update_user_account(self, name, email, password, title, birth_date, birth_month, 
                           birth_year, firstname, lastname, company, address1, address2, 
                           country, state, city, zipcode, mobile_number):
        url = f"{self.base_url}/updateAccount"
        data = {
            "name": name,
            "email": email,
            "password": password,
            "title": title,
            "birth_date": birth_date,
            "birth_month": birth_month,
            "birth_year": birth_year,
            "firstname": firstname,
            "lastname": lastname,
            "company": company,
            "address1": address1,
            "address2": address2,
            "country": country,
            "state": state,
            "city": city,
            "zipcode": zipcode,
            "mobile_number": mobile_number
        }
        self.last_response = requests.put(url, data=data)
        return self.last_response
        
    @keyword
    def delete_user_account(self, email, password):
        url = f"{self.base_url}/deleteAccount"
        data = {
            "email": email,
            "password": password
        }
        self.last_response = requests.delete(url, data=data)
        return self.last_response
        
    @keyword
    def get_user_account_detail_by_email(self, email):
        url = f"{self.base_url}/getUserDetailByEmail"
        data = {"email": email}
        self.last_response = requests.get(url, params=data)
        return self.last_response
        
    @keyword
    def post_to_products_list(self):
        url = f"{self.base_url}/productsList"
        self.last_response = requests.post(url)
        return self.last_response
        
    @keyword
    def put_to_brands_list(self):
        url = f"{self.base_url}/brandsList"
        self.last_response = requests.put(url)
        return self.last_response
        
    @keyword
    def search_product_without_parameter(self):
        url = f"{self.base_url}/searchProduct"
        self.last_response = requests.post(url, data={})
        return self.last_response
        
    @keyword
    def verify_login_without_email(self, password):
        url = f"{self.base_url}/verifyLogin"
        data = {"password": password}
        self.last_response = requests.post(url, data=data)
        return self.last_response
        
    @keyword
    def verify_login_without_password(self, email):
        url = f"{self.base_url}/verifyLogin"
        data = {"email": email}
        self.last_response = requests.post(url, data=data)
        return self.last_response
        
    @keyword
    def delete_verify_login(self):
        url = f"{self.base_url}/verifyLogin"
        self.last_response = requests.delete(url)
        return self.last_response
        
    @keyword
    def verify_response_status_code(self, expected_status_code):
        actual_status = self.last_response.status_code
        if actual_status != int(expected_status_code):
            raise AssertionError(f"Expected status code {expected_status_code}, but got {actual_status}")
        return True
        
    @keyword
    def verify_response_contains_text(self, expected_text):
        response_text = self.last_response.text
        if expected_text not in response_text:
            raise AssertionError(f"Response does not contain '{expected_text}'. Response: {response_text}")
        return True
        
    @keyword
    def get_response_json(self):
        try:
            return self.last_response.json()
        except:
            return self.last_response.text
            
    @keyword
    def get_response_status_code(self):
        return self.last_response.status_code
        
    @keyword
    def get_response_text(self):
        return self.last_response.text
        
    @keyword
    def get_response_time(self):
        return self.last_response.elapsed.total_seconds()
        
    @keyword
    def verify_response_time_less_than(self, max_seconds):
        elapsed = self.last_response.elapsed.total_seconds()
        if elapsed >= float(max_seconds):
            raise AssertionError(f"Response time {elapsed}s exceeds maximum {max_seconds}s")
        return True
        
    @keyword
    def log_response_details(self):
        logger.info(f"Status Code: {self.last_response.status_code}")
        logger.info(f"Response Time: {self.last_response.elapsed.total_seconds()}s")
        logger.info(f"Response Headers: {dict(self.last_response.headers)}")
        try:
            response_json = self.last_response.json()
            logger.info(f"Response JSON: {json.dumps(response_json, indent=2)}")
        except:
            logger.info(f"Response Body: {self.last_response.text}")
            
    @keyword
    def store_json_value(self, json_path, var_name):
        try:
            response_json = self.last_response.json()
            keys = json_path.split('.')
            value = response_json
            for key in keys:
                if '[' in key:
                    key_name = key.split('[')[0]
                    index = int(key.split('[')[1].split(']')[0])
                    value = value[key_name][index]
                else:
                    value = value[key]
            self.stored_data[var_name] = value
            logger.info(f"Stored '{json_path}' as '{var_name}': {value}")
            return value
        except Exception as e:
            logger.error(f"Failed to store JSON value: {str(e)}")
            raise
            
    @keyword
    def get_stored_value(self, var_name):
        value = self.stored_data.get(var_name)
        logger.info(f"Retrieved stored value '{var_name}': {value}")
        return value
        
    @keyword
    def store_response_json(self, var_name):
        try:
            response_json = self.last_response.json()
            self.stored_data[var_name] = response_json
            logger.info(f"Stored entire response as '{var_name}'")
            return response_json
        except Exception as e:
            logger.error(f"Failed to store response JSON: {str(e)}")
            raise
    @keyword
    def Validate_Search_Products(self,products):
        try:
            logger.info(len(products))
            for product in products:
                searched_product_data = self.search_product(product["name"])
                expected_matched_data = [p for p in products if p["name"] in product["name"]]
                logger.info("Searched Name : " + product["name"])
                logger.info("Response from search api"+ str(searched_product_data))
                assert sorted(searched_product_data)==sorted(expected_matched_data)
        except Exception as e:
            logger.error(f"Failed to store response JSON: {str(e)}")
            raise
