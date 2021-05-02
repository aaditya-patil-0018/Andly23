from math import e
### UP to the matching ### line, you might paste these lines near the top of each of your programs (after any imports)
# Which test case are we running?
# Change this line to switch to running a different test case
# (which is exactly what the grader will do and nothing more)
test_case = 1

# Following are instructor-provided files:
#   p4_testN_terms.csv:
#     line 1 column titles: term,inflation
#     line 2 values: term is number of months of annuity payments, inflation is annual inflation adjustment
#   p4_testN_cash_flows.csv:
#     column 1: number of months in the future
#     column 2: cash flow (US dollars) or interest rate (annual percentage simple rate)
#   p4_testN_interest_rates.csv:
#     column 1: number of months in the future
#     column 2: cash flow (US dollars) or interest rate (annual percentage simple rate)
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
### End of section you want to paste into your programs

## Highlights of my p4_search_annuity.py
# First figure out the bracket: low can be $0, high can be total which we know is too high
#     While we're at it we can calculate the npv of the cash flows, since this won't change during the search
#     Here's the code in its entirety for this section!  (up to ###)
total = 0.0
cf_npv = 0.0
cf_file = open(dense_cf_filename, 'r')
rates_file = open(dense_rates_filename, 'r')
months = 1
for cf_line, rate_line in zip(cf_file, rates_file):
    rate = float(rate_line) / 12.0 / 100.0
    cash_flow = float(cf_line)
    total += cash_flow
    discount = e ** (-rate * months)
    cf_npv += cash_flow * e ** (-rate * months)
    npv = cash_flow * discount
    if cash_flow != 0.0:
        print(f'months: {months} cashflow: {cash_flow} discount: {discount} npv: {npv}')
    months += 1
cf_file.close()
print(cf_npv)
print('NPV of customer-provided cash flows: $%.2f' % cf_npv)
print('Total customer-provided cash flows: $%.2f' % total)


lo, hi = 0.0, total
# Now we have a low that is too low and a high that is too high, so we can use bisection search
print('\nSearching for correct beginning monthly annuity payment:')
last_guess = lo
guess = hi  # which we will change to (lo + hi) / 2 in the loop
iter_count = 1  ### End of verbatim code
# the bisection search -- while the current guess is different than the last guess, keep narrowing it down
    #...
    # note that the guess is always rounded to decimal places since we want dollars and cents in USD
while guess != last_guess:
    guess = round(guess, 2)
    npv = cf_npv  # start npv at what we are getting from the customer-provided cash flows
    print(f'With annuity of ({lo}+{hi})/2 = ${(lo+hi)/2}')
    
    # then loop through the months figuring out how our annuity payments pv's deduct from the net present value
    #...
        # don't forget to zadjust the payment every 12 months (when months % 12 == 0, right)
            #payment += round(payment * inflation, 2)
    #...
    # after figuring out the npv at this payment guess, narrow the search range for the next time through the loop body
    #if npv < 0.0:
        # too high a monthly payment
        #hi = guess
    #else:
        # too low a monthly payment
        #lo = guess
# Finally, print out the details of the payments every year

# !!!
# Remember to look at p4_test1_results.txt -- that is the expected output from running the search program on test case 1
