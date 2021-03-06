"""
# Code Flow

actors = {
    "Kyle MacLachlan": "Dale Cooper",
    "Sheryl Lee": "Laura Palmer",
    "Lara Flynn Boyle": "Donna Hayward",
    "Sherilyn Fenn" : "Audrey Horne"
}

for each_actor in actors: 
    character = actors.get(each_actor)
    print 'name: {0}; character: {1}'.format(each_actor, character)

meet = False
distance = [0, 0, 102]
while (not meet):
    distance[0] += 2
    distance[1] += 1
    if distance[0] + distance[1] >= distance[2]:
        meet = True
print distance

phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}
try: 
    phone_book["Jamie Theakston"]
except KeyError:
    print "Jamie Theakston is not in the phone book" 

# Think Like a Coder
fizz_buzz_series = []
for i in range(1, 101): 
    if i % 3 == 0: 
        if i % 5 == 0: 
            fizz_buzz_series.append('FizzBuzz')
        else: 
            fizz_buzz_series.append('Fizz')
    elif i % 5 == 0: 
        fizz_buzz_series.append('Buzz')
    else: 
        fizz_buzz_series.append(i)
print fizz_buzz_series

# R/W Files
from collections import defaultdict
continent_wiki = defaultdict(lambda: [0, 0, 0])

with open('SQLite Data/EarthInstitute/lecz-urban-rural-population-land-area-estimates_continent-90m.csv', 'rU') as input_file:
    header = next(input_file)
    for input_line in input_file:
        each_line = input_line.rstrip().split(',')
        if each_line[1] == 'Total National Population': 
            continent = each_line[0]
            ppl_2010 = int(each_line[5])
            ppl_2100 = int(each_line[6])
            land_area = int(each_line[-1])
            continent_wiki[continent][0] += ppl_2010
            continent_wiki[continent][1] += ppl_2100
            continent_wiki[continent][2] += land_area

with open('SQLite Data/EarthInstitute/thinkful_analysis.csv', 'w') as output_file: 
    output_file.write('continent,ppl_change_2100_2010,ppl_density_2010\n')
    for continent, info in continent_wiki.iteritems():
        output_file.write(continent + ',' + str((info[1] - info[0])/float(info[0])) + ',' + str(info[0]/float(info[2])) + '\n')

# SQLite 
import sqlite3 as lite
import pandas as pd

month_list = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month = raw_input("Warmest month: ")
while month not in ('January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'):
    print  '{0} is not a valid month. Input be one of {1}'.format(month, month_list)
    month = raw_input("Warmest month: ")

con = lite.connect('SQLite Data/toy_data.sqlite')
with con: 
    cur = con.cursor()
    cur.execute("select name, state from cities join weather on name = city where warm_month = '%s'" % month)
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    df = pd.DataFrame(rows, columns = cols)
    
    if len(df) == 0: 
        message = 'No cities are warmest in %s' % month
    else: 
        message = 'The cities that are warmest in %s are: ' % month
        for index, each_row in df.iterrows():
            message += each_row['name'] + ',' + each_row['state']
            if index == len(df) - 1: 
                message += '.'
            else: 
                message += '; '
print message
"""
# Statistics Overview
import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''
data = data.splitlines()
data = [i.split(', ') for i in data]
column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

means = [df['Alcohol'].mean(), df['Tobacco'].mean()]
medians = [df['Alcohol'].median(), df['Tobacco'].median()]
modes = [stats.mode(df['Alcohol'])[0][0], stats.mode(df['Tobacco'])[0][0]]
ranges = [max(df['Alcohol']) - min(df['Alcohol']), max(df['Tobacco']) - min(df['Tobacco'])]
variances = [df['Alcohol'].var(), df['Tobacco'].var()]
deviations = [df['Alcohol'].std(), df['Tobacco'].std()]
print "For the Alcohol and Tobacco dataset, means are {0}, medians are {1}, modes are {2}, ranges are {3}, variances are {4}, and standard deviations are {5}".format(means, medians, modes, ranges, variances, deviations)