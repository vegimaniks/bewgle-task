### Prerequisites to run the script
Python Version: 3.8+
Third party python packages required are listed in the requirements.txt file
Create a virtulenv using the command `python -m venv venv` and actiavte the virtual environment.
Run `pip install -r requirements.txt` command to install required packages to run the test scripts

### Testscript

Test script(task_bewgle.py) contains two automated test cases
1. Search a laptop in amazon with filters. Sort the isted latops by Low to High. Validate whether the laptops are listed in price low to high
2. This is a partial test case that requests a Free Demo from Bewgle. The Request wasn't submit due to captcha. This test case is to demonstrate that I can automate the Form submission.