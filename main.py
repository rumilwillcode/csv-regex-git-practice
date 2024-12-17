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

def create_call_list(customer_id, feedback, rating, phone_num):
  """Using the data extracted by the unhappy_customer function, creates a call list of unhappy customers (csv file)."""
  with open("unhappy_call_list.csv", "w", newline="") as file:
    writer = csv.writer(file)
    columns = ["Customer ID", "Feedback", "Rating", "Phone #"] 
    writer.writerow(columns)
    for i in range(len(customer_id)):
      writer.writerow([customer_id[i], feedbsck[i], rating[i], phone_num[i]])
