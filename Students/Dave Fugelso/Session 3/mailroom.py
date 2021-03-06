"""

Dave Fugelso, UW Python Course (Developing on WIndows so didn't make this an executable script.)


Mail Room

You work in the mail room at a local charity. Part of your job is to write incredibly boring, repetitive emails thanking your donors for their generous gifts. 
You are tired of doing this over an over again, so yo've decided to let Python help you out of a jam.

Write a small command-line script called mailroom.py. As with Task 1, This script should be executable. The script should accomplish the following goals:

It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at 
first with at least five donors, with between 1 and 3 donations each
The script should prompt the user (you) to choose from a menu of 2 actions: 'Send a Thank You' or 'Create a Report'.
If the user (you) selects 'Send a Thank You', prompt for a Full Name.
If the user types 'list', show them a list of the donor names and re-prompt
If the user types a name not in the list, add that name to the data structure and use it.
If the user types a name in the list, use it.
Once a name has been selected, prompt for a donation amount.
Verify that the amount is in fact a number, and re-prompt if it isn't.
Once an amount has been given, add that amount to the donation history of the selected user.
Finally, use string formatting to compose an email thanking the donor for their generous donation. Print the email to the terminal and return to the original prompt.
It is fine to forget new donors once the script quits running.

If the user (you) selected 'Create a Report' Print a list of your donors, sorted by total historical donation amount.
Include Donor Name, total donated, number of donations and average donation amount as values in each row.
Using string formatting, format the output rows as nicely as possible. The end result should be tabular (values in each column should align with those above and below)
After printing this report, return to the original prompt.
At any point, the user should be able to quit their current task and return to the original prompt.
From the original prompt, the user should be able to quit the script cleanly
First, factor your script into separate functions. Each of the above tasks can be accomplished by a series of steps. Write discreet functions that accomplish individual steps and call them.

Second, use loops to control the logical flow of your program. Interactive programs are a classic use-case for the while loop.

Put the functions you write into the script at the top.

Put your main interaction into an if __name__ == '__main__' block.

Finally, use only functions and the basic Python data types you've learned about so far. There is no need to go any farther than that for this assignment.

As always, put the new file in your student directory in a session03 directory, and add it to your clone early. Make frequent commits with good, clear messages about what you are doing and why.

When you are done, push your changes and make a pull request.
"""

import operator
import datetime

#Donor list

donors = [  ['Dave Fugelso', [3000, 6000, 4000]],\
            ['Barb Grecco', [5000]],\
            ['Ken Johnson', [500, 250, 50, 80]],\
            ['Jack Bell', [55, 55, 55, 55, 55]],\
            ['Alejandro Escobar', [25, 25]]\
         ]
    
def listDonors ():
    ''' 
    List donors.
    '''
    for contributors in donors:
        print contributors[0]

def report ():
    ''' 
    Create a report with Name, Total DOnation, Number of Donation and average donation size. Print largest donor first.
    '''
    
    # go through list and calculate donor metrics
    for donor in donors:
        total = 0
        print donor
        print donor[0]
        print donor[1]
        for amount in donor[1]:
            total += amount
        donor.append (total)
        print donor
        #if total > 0:
        #    sortedDonors[total] = [ donor[0], total, len(donors[1]), total/len(donor[1]) ]

    #print it out
    print '\n\nDonor\t\t\t\tAmount\t\tNumber of Donations\t\tAverage Donation'
    print     '-----\t\t\t\t------\t\t-------------------\t\t----------------'
    for donor in sorted(donors, key=lambda individual: individual[2], reverse=True):
        print donor[0],
        if len(donor[0]) < 15:
            print '\t\t\t',
        else:
            print '\t\t',
        print donor[2],
        print '\t\t\t',
        if len(donor[1]) > 0:
            print len(donor[1]),
            print '\t\t\t',
            print donor[2] / len(donor[1])
        else:
            print '0\t\tNA'
    print '\n\n\n\n'
        
def thankYou (donor):
    ''' 
    Send off a thank you note to a single donor.
    '''
    print '\n\n\n\n\t\t\t\t\t',datetime.date.today()
    print '\nOur Charity Name\nAddress\nEtc\n\n\n'
    name = donor[0].split()
    print 'Dear '+name[0]+':\n'
    if len(donor[1]) <= 1:
        print 'Thank you for your donation of ',
        print donor[1][0] ,
        print '.'
    else:
        print 'Thank you for your donations of ',
        for i in range (0, len(donor[1])-1):
            print donor[1][i],
            print ',',    
        print ' and ',
        print donor[1][len(donor[1])-1],
        print '.'                
    print '\nWe look forward to serving our community blah blah blah.\n\nSincerely, \n\nOur Charity.\n\n\n\n'
  
def addDonor (name):
    '''
    Add <name> to the list of donors and get the amounts of donation.
    '''
    donations = []
    amount = 0
    while amount >= 0:
        inp = raw_input ('Add amount of donation one at a time. Enter \'-1\' to finish: ')
        try:
            amount = int(inp)
            if amount > 0:
                donations.append(amount)
        except:
            print ('Input must be a number.')
            amount = 0
    donors.append ( [name, donations] )
        
        
    

def processDonors ():
    '''
    Interact with administrator to manage donor list.
    '''
    processing = True
    while processing:
        action = raw_input ("Select 'Send a Thank You(S)', 'Create a report (C)', or 'Quit(Q)': ")
        if action.upper() == 'S' or action.upper() == 'SEND A THANK YOU':
            thankYouProcessing = True
            while thankYouProcessing:
                name = raw_input ("Enter name of donor, add a donor ('A') or ('Add'), or list all donors ('L') or ('List') or 'E' or 'End' to go to main menu: ")
                if name.upper() == 'L' or name.upper() == 'LIST':
                    listDonors()
                elif name.upper() == 'E' or name.upper() == 'END':
                    thankYouProcessing = False
                else:
                    haveDonor = False
                    for donor in donors:
                        if name in donor:
                            thankYou (donor)
                            haveDonor = True
                            break
                    if not haveDonor:
                        addDonor(name)
        elif action.upper() == 'Q' or action.upper == 'QUIT':
            processing = False
        elif action.upper() == 'C' or action.upper == 'Create a report'.upper():
            report()
        else:
            print 'Unrecognized input.'
        

if __name__ == "__main__":
    processDonors ()