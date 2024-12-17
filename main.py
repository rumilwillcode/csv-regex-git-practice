import csv
import re


def unhappy_customer():
  """Takes in feedback.txt to identify unhappy customers (that rated us lower than 4 out of 5) and returns
     the customer ID, text of feedback and customer's phone #."""
  with open("feedback.txt", "r") as file:
    customer_id = []
    feedback = []
    phone_num = []
    rating = []
    
    for line in file:
      pattern = r"^([\d]+) +([A-Za-z\., ]+) +(\d) +([\d\-() ]*)"
      match = re.search(pattern, line)
      if match and int(match.group(3)) < 4:
        customer_id.append(match.group(1).strip())
        feedback.append(match.group(2).strip())
        rating.append(match.group(3).strip())
        phone_num.append(match.group(4).strip())
  return customer_id, feedback, rating, phone_num

unhappy_customer()
