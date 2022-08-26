from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException, TimeoutException, InvalidArgumentException, ElementClickInterceptedException)

def count_vacancies(name_department, language_list, expected_number_jobs):
    
    '''
       This function counts the number of jobs found and compare this value 
       with the expected result. Сode can be used with different sets of parameters 
       (it is possible to choose any departament and one or more languages).
       The function inputs:  
           - the name of the department
           - the list of languages
           - the expected number of jobs.   
           
       The function returnes count of jobs.
           
    '''      
    
    # create driver object
    browser_setup = ChromeService(
        executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=browser_setup)
    
    # open url
    driver.get('https://cz.careers.veeam.com/vacancies')
    driver.implicitly_wait(5)

    # maximize window
    driver.maximize_window()

    # close cookie
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.ID, 'cookiescript_close'))).click()

    try:
        # choose department
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sl"]'))).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.LINK_TEXT, name_department))).click()

        # choose language
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div[1]/div/div[3]/div/div/button'))).click()

        for lan in language_list:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, f'//label[text()="{lan}"]'))).click()

        driver.implicitly_wait(5)

        # count of vacancies
        jobs_counted = driver.find_elements(By.CLASS_NAME, 'card-sm')

    except NoSuchElementException:
        pass
        jobs_counted = 0
        return jobs_counted

    except TimeoutException:
        pass
        jobs_counted = 0
        return jobs_counted

    except InvalidArgumentException:
        pass
        jobs_counted = 0
        return jobs_counted
    
    except ElementClickInterceptedException:
        pass
        jobs_counted = 0
        return jobs_counted

    else:
        jobs_counted = len(jobs_counted)
        return jobs_counted

    finally:
        # close driver
        driver.close()


def test_success(name_department, language_list, expected_number_jobs):
    
    '''
       This function determines whether the test passed or failed
       (whether the actual number of jobs coincides with the expected number 
       of jobs).
       The function returnes one of strings for each test:
           - 'Test passed successfully'
           - 'Test failed (check the entered data)'
       
    '''    
    
    jobs_counted = count_vacancies(
        name_department, language_list, expected_number_jobs)

    if expected_number_jobs == jobs_counted:
        return 'Test passed successfully'

    if expected_number_jobs != jobs_counted:
        return 'Test failed (check the entered data)'


def print_results(test_list):
    
    '''
       This function prints the result of test (tests)
       The function inputs list of tests, which include:
           - the name of the department
           - the list of languages
           - the expected number of jobs                  
       The function outputs the test number and the return string of the test_success function.       
       
    ''' 
    
    for number, test in enumerate(test_list):
        if len(test) == 3:
            number += 1
            print(number, test_success(*test))
        else:
            number += 1
            print(number, 'Test failed (check the entered data)')
            
            
# the brief list of tests that can be used to check 
# the number of vacancies in the Research & Development department
test_list = [['Research & Development', ['English'], 11],
             ['research & development', ['English'], 11],
             ['Research', ['English'], 11],
             ['Development', ['English'], 11],
             [558, ['English'], 11],
             [['Research & Development'], ['English'], 11],
             ['Research & Development', ['english'], 11],
             ['Research & Development', ['Englis'], 11],
             ['Research & Development', [31313], 11],
             ['Research & Development', ['English'], 0],            
             ['Research & Development', ['sometext'], 11],
             ['Research & Development', ['English'], 11.5],
             ['Research & Development', ['English'], 12],
             ['Research & Development', ['English'], 10.99],
             ['Research & Development', ['English'], 11.0],
             ['Research & Development', ['English'], '11'],
             ['Research & Development', ['English'], [11]],
             ['', [''], ''],
             ['', ['English'], 2],
             ['', ['English']],
             []]


# output results
print_results(test_list)

# also these functions can be used to check the number of vacancies
# in other departments by different language combinations .
test_list_1 = [['All departments', ['English', 'German'], 63],
               ['All departments', ['English', 'Russian', 'French', 'German', 'Spanish'], 65],
               ['Corporate Information Systems', ['Russian', 'German'], 8],
               ['Quality Assurance', ['French', 'Russian'], 4],
               ['Technical Customer Support', ['Spanish'], 1],
               ['IT', ['English', 'German'], 4],
               ['Other', ['English', 'Russian', 'French', 'German'], 4],
               ['HR', ['English'], 1],
               ['HR', ['English'], 1],
               ['Technical Documentation Development', ['Russian'], 1],
               ['Product Management ', ['English', 'Russian'], 1],
               ['Product Management ', ['French', 'German'], 5],
               ['Technical Documentation Development', ['Russian', 'Chinese'], 1],
               ['fgflf', ['German'], 2],
               [2325, ['English'], 1],
               ['Technical Documentation Development', [2], 1],
               ['HR', [256, 'Russian'], 1],               
               ['All departments', ['English', 'Russian', 'Trench', 'German'], 62],
               ['All departments', [25689, 'Russian', 'French', 'German'], 62],
               ['Quality Assurance', ['French', 'Russian']],
               [['English', 'German'], 3]]


print_results(test_list_1)