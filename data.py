# Indicate briefly how far you got on the following targets:
# 1. Constructing the data list:
# 2. Calculating Averages:
# 3. Calculating Seasons:

import csv

def analyse(inputfile, outputfile):
    data = []
    # data is to be a list of item data information to be read from the input
    # file and then used in calculating the rows to be written out to the
    # output file.
    #
    # There is one element if data for each different item in the input file.
    #
    # Each element of data is a list of length 2.
    #
    # If el is an element of the data list, then el[0] is an item: a list of
    # length 4 as described in the assignment. For example:
    #     ['Blackberries', 'All Varieties', '-', '$/kg']
    # el[1] is then a list of lists as described in the comment about allprices
    # in the function calc_averages below
    #
    # An example of data could then be:
    #  [ [item1, allprices1],
    #    [item2, allprices2],
    #    [item3, allprices3],
    #    [item4, allprices4] ]
    # where the item element are as described above and the allprices
    # elements are as described below.


    with open(inputfile, 'r', newline = '') as input_file:
        reader = csv.reader(input_file)
        header = reader.__next__()           # read the header row from the input_file
        header = header[2:18] + ["Season"]   # construct the header row for the output file
        for row in reader:
            # Replace the following "pass" statement with code
            # to populate the data list with the information
            # required from the input file
            pass          # YOUR CODE REPLACES THIS LINE

    # at this point, we have read the whole input file into our data list
    # and can therefore close the input file

    with open(outputfile, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)

        for n, el in enumerate(data):
            item = el[0]
            prices = el[1]

            # Calculate averages
            averages = calc_averages(prices)

            # calculate seasons
            season = calc_seasons(averages)

            # output the final row for this item
            writer.writerow(item + averages + [season])


def calc_averages(allprices):
    # allprices is a list of lists, each sub-list contains prices for an item
    # for each month in a single year. if the item was not available in a
    # particular month, the price will be recorded as the empty string: ''
    # An example value for allprices is:

    #    [  ['',  '',  '',  '', 1.0, 2.0, 1.2, 1.3, 1.1,  '',  '',  ''],
    #       ['',  '',  '', 1.2, 1.0, 2.0, 1.2, 1.3, 1.1,  '',  '',  ''],
    #       ['',  '',  '', 1.2,  '', 1.8, 1.3, 1.1,  '',  '',  '',  ''],
    #       ['',  '',  '',  '', 1.0, 2.0, 1.2, 1.2,  '',  '',  '',  ''],
    #       ['',  '',  '',  '', 1.0, 2.0, 1.1, 1.2, 1.4, 1.8, 1.9, 2.2]    ]
    averages = []

    # insert the code after this comment to calculate the list of average prices
    # per month over all years from allprices

    # YOUR CODE REPLACES THIS LINE

    return averages

def calc_seasons(averages):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',\
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    season = ''
    # Averages contains a list of length 12 containing average prices for an item for
    # each month (Jan to Dec) over all years, where some or all of the entries might be empty strings
    # The following are 3 different possible example values for average:
    #   ['', '', '', '', '', '',2.338, 2.175, 3.086, '', '', '']
    #   [1.00, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.10, 1.11, 1,12]
    #   ['', '', '', '', '', '', '', '', '', '', '', '']
    #
    # Insert the code after this calculate the Season string from the averages list as described in the assignment

    # YOUR CODE REPLACES THIS LINE

    return season


analyse("fruitvegcleanSmall.csv","AVERAGES.csv")

