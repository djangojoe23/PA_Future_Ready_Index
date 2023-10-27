import pandas as pd


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    '''
    Six graphs/csv files (Alg-Growth, Alg-Achievement, Lit-Growth, Lit-Achievement, Bio-Growth, Bio-Achievement)
    1. Go in school fast facts and IF THE SCHOOL offers 9-12...
        1. get the address and use it to get geo coords of the school
        2. Get all other data about the school in fast facts
        3. Get the growth and achievement from the other data file
        4. Save it all in a dictionary
    2. print it all out in 6 separate csv files
    '''
    df = pd.read_csv('data/csv/SchoolFastFacts_20172018.csv')
    high_schools = df.loc[(df['DataElement'] == "Grades Offered") & (df['DisplayValue'] == "9, 10, 11, 12")]
    for i in high_schools.index:
        all_rows = df.loc[df['AUN'] == high_schools['AUN'][i]]
        address = all_rows.loc[all_rows['DataElement'] == "School Address (Street)"]["DisplayValue"].iloc[0] + " "
        address += all_rows.loc[all_rows['DataElement'] == "School Address (City)"]["DisplayValue"].iloc[0] + ", "
        address += all_rows.loc[all_rows['DataElement'] == "School Address (State)"]["DisplayValue"].iloc[0] + " "
        address += all_rows.loc[all_rows['DataElement'] == "School Zip Code"]["DisplayValue"].iloc[0]
        print(address)
        break

