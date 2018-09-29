x = 1
total = 0
GroupTotal = 0
number_of_people = int(raw_input("Enter total number of people: "))
for x in range(1, number_of_people+1):  # from 1 to number of people
    print "People "+ "# ", x
    print "Enter total number of $2 dollar coin:"
    total1 = int(raw_input())
    toonie = total1 * 2

    print "Enter total number of $1 dollar coin:"
    total2 = int(raw_input())
    loonie = total2 * 1

    print "Enter total number of 50 cent coin:"
    total3 = int(raw_input())
    half_dollar = total3 * 0.5

    print "Enter total number of 25 cent coin:"
    total4 = int(raw_input())
    quarter = total4 * 0.25

    print "Enter total number of 10 cent coin:"
    total5 = int(raw_input())
    dime = total5 * 0.10

    print "Enter total number of 5 cent coin:"
    total6 = int(raw_input())
    nickel = total6 * 0.05

    print "Enter total number of 1 cent coin:"
    total7 = int(raw_input())
    penny = total7 * 0.01

    total = toonie + loonie + half_dollar + quarter + dime + nickel + penny
    print "Total coin value from person ", x, "is $ ", total
    GroupTotal += total
print "Group total: $ ", GroupTotal
average = GroupTotal / number_of_people
print "Average: $ ", "%.2f" % average  #round the average to 2 decimals