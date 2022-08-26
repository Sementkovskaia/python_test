# python_test


This repository stores solutions to two tasks that were done using Python:


1. Please create a tiny C# utility to monitor Windows processes and kill the processes that work longer than the threshold specified: 

This command line utility expects three arguments: a process name, its maximum lifetime (in minutes) and a monitoring frequency (in minutes, as well). When you run the program, it starts monitoring processes with the frequency specified. If a process of interest lives longer than the allowed duration, the utility kills the process and adds the corresponding record to the log. When no process exists at any given moment, the utility continues monitoring (new processes might appear later). The utility stops when a special keyboard button is pressed (say, q).

Here is the example: monitor.exe notepad 5 1 – every other minute, the program verifies if a notepad process lives longer than 5 minutes, and if it does, the program kills the process.

2. Using Selenium WebDriver, please do the following:

Open https://cz.careers.veeam.com/vacancies and maximize the browser window. 
Then, choose Research & Development and English from the lists of departments and languages, respectively.
Please, count the number of jobs found and compare this value with the expected result.

Notes:

It would be a good idea to parameterize the values of input parameters and the expected job number so that the code could be used with various parameter sets.
You can use a browser of your choice.
Keywords: Webdriver C# best practices, Page Object, implicit/explicit waits, reliable/fragile locators, NUnit



