import csv
import json

f = open('final.csv', 'rU')

reader = csv.DictReader(f, fieldnames=("Feature col 1", "Feature col 2"))

# Parse the CSV into JSON
out = json.dumps([row for row in reader])

f = open('Finaldataset.json', 'w')

f.write(out)

print("JSON saved!")

#to json to csv
#mongoimport --db dbName --collection collectionName --file parsed.json --jsonArray



# reader = csv.DictReader(f, fieldnames=("Customer_id", "Customer_name", "Birth_date", "C_gender", "Profession",
#                                        "Exp_point", "Last_purchase", "Brand_choice", "Product_id", "Product_name",
#                                        "Product_quantity", "Tax_amount", "Profit", "Suitable_season",
#                                        "Product_active_for_sale", "Product_refund/Replace", "Category_id",
#                                        "Category_name", "SubCategory_id", "SubCategory_name", "Invoice_id",
#                                        "Invoice_date", "Payment_id", "Payment_method", "Amount", "Card_type",
#                                        "Gift_coupen_id", "Coupen_value", "Employee_id", "Employee_name", "E_gender",
#                                        "Birth_date", "Hire_date", "Qualification", "Salary", "Bonus",
#                                        "Customer_reference_id", "Reference_type", "Customer_review_id",
#                                        "Customer_review_description", "Customer_rating", "In_time", "Out_time",
#                                        "Current_selling_price"))
#mongoimport --db supermarket --collection main --file Finaldataset.json --jsonArray
