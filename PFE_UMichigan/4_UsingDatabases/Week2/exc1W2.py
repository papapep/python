# -*- coding: utf-8 -*-

import sqlite3, re, sys

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = '../mbox.txt'
fh = open(fname)
rows = 0
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    org = str(re.findall('@(.*)',pieces[1])).strip("['']")
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, 1 )''', ( org, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))
    
    #"\033[K" clears to the end of the line
    #the \r, returns to the beginning of the line
    #the flush statement makes sure it shows up immediately 
    # so you get real-time output.

    print "\033[K","Rows I've read so far:", rows, "\r",
    sys.stdout.flush()
    
    rows += 1

    # This statement commits outstanding changes to disk each 
    # time through the loop - the program can be made faster 
    # by moving the commit so it runs only after the loop completes
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print
print "Counts:"
for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()
