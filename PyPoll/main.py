import os
import csv
#open csv file and read
poll_csv = os.path.join('Resources','election_data.csv')

with open(poll_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')

    next(csvreader)
    #convert columns in csv file to lists
    voter_ids = []
    counties = []
    candidates = []

    for row in csvreader:

        voter = row[0]
        county = row[1]
        candidate = row[2]

        voter_ids.append(voter)
        counties.append(county)
        candidates.append(candidate)
    # define function to find out the candidate names
    def unique(candidates):
    
        candidate_names = []

        for x in candidates:
            if x not in candidate_names:
                    candidate_names.append(x)

        for x in candidate_names:
            print(x)

    #print(unique(candidates))
    #define function to count the number of votes for candidates
    def counts(candidates, y):
        return candidates.count(y)

    khan_votes = counts(candidates,'Khan')
    correy_votes = counts(candidates,'Correy')
    li_votes = counts(candidates,'Li')
    otooley_votes = counts(candidates,"O'Tooley")
    #input formulas for analysis
    total_votes = khan_votes + correy_votes + li_votes + otooley_votes

    khan_percentage = round(khan_votes / total_votes * 100,5)
    correy_percentage = round(correy_votes / total_votes * 100,5)
    li_percentage = round(li_votes / total_votes * 100,5)
    otooley_percentage = round(otooley_votes / total_votes * 100,5)
    #Khan is seen with the highest votal total
    #print result to terminal window
    print('Election Results')
    print('---------------------')
    print(f'Khan: {khan_percentage}% ({khan_votes})')
    print(f'Correy: {correy_percentage}% ({correy_votes})')
    print(f'Li: {li_percentage}% ({li_votes})')
    print(f"O'Tooley: {otooley_percentage}% ({otooley_votes})")
    print('---------------------')
    print('Winner: Khan')
    print('---------------------')
    #write to text file
    output_path = os.path.join('analysis','new.csv')

    with open(output_path,'w') as newfile:

        csvwriter = csv.writer(newfile,delimiter=',')

        csvwriter.writerow(['Election Results'])
        csvwriter.writerow(['---------------------'])
        csvwriter.writerow([f'Khan: {khan_percentage}% ({khan_votes})'])
        csvwriter.writerow([f'Correy: {correy_percentage}% ({correy_votes})'])
        csvwriter.writerow([f'Li: {li_percentage}% ({li_votes})'])
        csvwriter.writerow([f"O'Tooley: {otooley_percentage}% ({otooley_votes})"])
        csvwriter.writerow(['---------------------'])
        csvwriter.writerow(['Winner: Khan'])
        csvwriter.writerow(['---------------------'])
