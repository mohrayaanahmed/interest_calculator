# Program to calculate equal total payments
import pandas as pd
import tkinter as tk
import webbrowser

root = tk.Tk()

# setting the windows size
root.geometry("2100x2100")
root.title("Equal Total Payments Method")
root.configure(bg = "lavender blush")
Total_Loan_Amount = 0
Annual_Interest_Rate = 0
Number_of_Months = 0
months = []

# declaring string variable
loan_amount = tk.StringVar()
interest_rate = tk.StringVar()
num_mon = tk.StringVar()


# defining a submit button function that will
# print the table on the screen
def submit():

	Total_Loan_Amount = float(loan_amount.get())
	Annual_Interest_Rate = float(interest_rate.get())
	Number_of_Months = int(num_mon.get())
    
	loan_amount.set("")
	interest_rate.set("")
	num_mon.set("")

	for i in range(1, Number_of_Months + 1):
		months.append(i)
	outstanding_balance = []
	payment = []
	principal_paid = []
	interest_paid = []
	Annual_Interest_Rate = Annual_Interest_Rate/100
	Rn = Annual_Interest_Rate/12
	n = 1
	for i in months:
		denominator = (1 - (1 + (Rn))**-(Number_of_Months))
		if denominator != 0:
			Paymnt = round((((Rn) * (Total_Loan_Amount)) / denominator), 2)
		else:
			Paymnt = 0
		payment.append(Paymnt)
    
		PP = round(Paymnt * (1 + Rn)**-(1 + Number_of_Months - n), 2)    
		principal_paid.append(PP)
		n += 1
    
		interest = round(Paymnt - PP, 2)
		interest_paid.append(interest)
    
		OB = round((interest/Rn) - PP, 2)
		outstanding_balance.append(OB)


# add in a dataframe for easier
# visualization in a table format
	df = pd.DataFrame(months, columns = ["Number of Payment"])
	df["Payment Amount"] = payment
	df["Principal Amount Paid"] = principal_paid
	df["Interest Amount Paid"] = interest_paid
	df["Loan Outstanding Balance"] = outstanding_balance
	df.set_index("Number of Payment")
	df.to_html("Output.html")
	webbrowser.open("Output.html")

title_label = tk.Label(root, text = 'Please Enter the following details', font=('times new roman',26, 'bold'), fg = "navy blue", justify = "center", bg = "lavender blush")
# creating a label for 
# total loan amount
loan_label = tk.Label(root, text = 'Total Loan Amount', font=('times new roman',22, 'bold'), fg = "purple", bg = "lavender blush")

# creating a entry for input
loan_entry = tk.Entry(root,textvariable = loan_amount, font=('times new roman',22,'normal'), bd = 1, width = 12, bg = "white", fg = "navy blue")

# creating a label for
# annual interest rate
interest_label = tk.Label(root, text = 'Annual Interest Rate', font = ('times new roman',22,'bold'), fg = "purple", bg = "lavender blush")

# creating a entry for input
interest_entry = tk.Entry(root, textvariable = interest_rate, font = ('times new roman',22,'normal'), bd = 1, width = 12, bg = "white", fg = "navy blue")

# creating a label for
# number of months
mon_label = tk.Label(root, text = 'Number of months', font = ('times new roman',22,'bold'), fg = "purple", bg = "lavender blush")

# creating a entry for input
mon_entry = tk.Entry(root, textvariable = num_mon, font = ('times new roman',22,'normal'), bd = 1, width = 12, bg = "white", fg = "navy blue")


# creating a button using the widget 
# Button that will call the submit function 
sub_btn = tk.Button(root,text = 'Submit', command = submit, height = 1, width = 12)


# placing the label and entry in the
# required position using grid method
title_label.grid(row = 0, column = 0)

loan_label.grid(row = 2, column = 0)
loan_entry.grid(row = 2, column = 1)

interest_label.grid(row = 3, column = 0)
interest_entry.grid(row = 3, column = 1)

mon_label.grid(row = 4, column = 0)
mon_entry.grid(row = 4, column = 1)

sub_btn.grid(row = 5,column = 1)


# performing an infinite loop 
# for the window to display
root.mainloop()