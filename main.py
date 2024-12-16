import csv
import re


def unhapy_customer():
  """Takes in feedback.txt to identify unhappy customers (that rated us lower than 4 out of 5) and reaturns
     the customer ID, text of feedback and customer's phone #."""
  with open("feedback.txt", "r") as file:

    #Initialize customer_id, feedback, and phone_num lists to be populated with data.
    customer_id = []
    feedback = []
    phone_num = []
    
    reader = csv.reader(file) 
