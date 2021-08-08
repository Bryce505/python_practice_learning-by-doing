#!python3
# read_census_excel.py - tabulates population and number of census tracts for each country

import openpyxl,pprint
print('opening workbook....')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
country_data = {}

# TODO: fill in country_data with each country's population and tracts.
print('reading rows...')

for row in range(2,sheet.max_row+1):
    state = sheet['B'+str(row)].value
    country = sheet['C'+str(row)].value
    pop = sheet['D'+str(row)].value

# TODO: open w new text file nad write the contents of country_data to it.
    """data structure-dict
    {'AK:{'Aleutians East':{'pop':3141,'tracts':1},
      'Aleutians West':{'pop':5561,'tracts':2},
      --snip--   
    country_data[state abbrev][country]['tract']
    country_data[state abbrev][country]['pop']   
    """
    # make sure the key for this state exists
    country_data.setdefault(state,{})
    # make sure the key for this country in this state exists
    country_data[state].setdefault(country,{'tracts':0,'pop':0})

    # each row represent one census tract,so increment by one
    country_data[state][country]['tracts'] += 1
    # increase the country pop by the pop in this census tartct
    country_data[state][country]['pop'] += int(pop)
# TODO: open w nea text file and write the contents of country_data to it

print('writing results...')
result_file =open('CENSUS2010.PY','w')
result_file.write('all_data='+pprint.pformat(country_data))
result_file.close()
print('done')


