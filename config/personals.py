'''
Author:    Sujay Babu Thota
'''

###################################################### CONFIGURE YOUR TOOLS HERE ######################################################

# >>>>>>>>>>> Easy Apply Questions & Inputs <<<<<<<<<<<

# Your legal name
first_name = "Sujay"
middle_name = "Babu"
last_name = "Thota"

# Phone number (required)
phone_number = "9346491221"  # Enter your actual 10-digit mobile number

# What is your current city?
current_city = "Hyderabad"

# Address
street = "Madhapur"
state = "Telangana"
zipcode = "500081"
country = "India"

## Equal Opportunity Questions

ethnicity = ""
gender = "Male"
disability_status = "No"
veteran_status = "No"

############################################################################################################

# --- Load user settings saved by the local control panel
from config import _overrides as _o
_o.apply(__name__, globals())