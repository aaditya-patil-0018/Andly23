### UP to the matching ### line, you might paste these lines near the top of each of your programs (after any imports)
# Which test case are we running?
# Change this line to switch to running a different test case
# (which is exactly what the grader will do and nothing more)
test_case = 1

# Following are the test case files given
annuity_terms_filename = 'p4_test%d_terms.csv' % test_case
sparse_cf_filename = 'p4_test%d_cash_flows.csv' % test_case
sparse_rates_filename = 'p4_test%d_interest_rates.csv' % test_case

# Following are the output files created by this program. These have one line for every month
dense_cf_filename = 'p4_test%d_dense_cf.txt' % test_case
dense_rates_filename = 'p4_test%d_dense_rates.txt' % test_case

# Get the annuity terms
terms_file = open(annuity_terms_filename, 'r')
terms_file.readline()  # skip the first line of column titles
line = terms_file.readline()  # this is the line with the numbers, e.g., '120,3.0'
annuity_term, inflation = line.split(',')  # split into our two values (as strings), e.g., '120', '3.0'
annuity_term = int(annuity_term)  # convert to an integer from a string
inflation = float(inflation) / 100.0  # convert to a float and ratio from a string with percent number
terms_file.close()

# File for writing the cash_flow.txt file
sparse_file = open(sparse_cf_filename, 'r')
dense_file = open(dense_cf_filename, 'w')
month = 1
for line in sparse_file:
    cf_month, cf_amount = line.split(',')
    cf_month = int(cf_month)  # convert the string cf_month into an integer
    cf_amount = float(cf_amount)  # convert the string cf_amount into a float
    while month < cf_month:
        dense_file.write(str(0.0) + '\n')  # no cash flows for this month
        month += 1
    dense_file.write(str(cf_amount) + '\n') # here's the cash flow month
    month += 1
while month <= annuity_term:  # any later months until the end of the annuity term after last cash flow
    dense_file.write(str(0.0) + '\n')
    month += 1
sparse_file.close()
dense_file.close()

# File for writing the rates.txt file
sp_rates_file = open(sparse_rates_filename, 'r')
de_rates_file = open(dense_rates_filename, 'w')
# This is for keeping track of the month and the last rate
mo = 1
last_rate = 0
# Loop for writing and reading from one file to writing the data into another
for line in sp_rates_file:
    rate_mo, rate = line.split(',')
    rate_mo = int(rate_mo)
    rate = float(rate)
    while mo < rate_mo:
        de_rates_file.write(str(last_rate) + '\n')
        mo += 1
    last_rate = rate
    de_rates_file.write(str(rate) + '\n')
    mo += 1
while mo <= annuity_term:
    de_rates_file.write(str(rate) + '\n')
    mo +=1
sp_rates_file.close()
de_rates_file.close()

