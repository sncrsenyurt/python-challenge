# import the csv module
import csv

# set the file path for the data
file_path = "election_data.csv"

# open the file and create a csv reader object
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip the header row
    next(csvreader)

    # initialize variables
    total_votes = 0
    candidate_votes = {}
    winner_votes = 0
    winner_name = ""

    # count the total number of votes and the votes for each candidate
    for row in csvreader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

    # find the winner of the election based on popular vote
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        if votes > winner_votes:
            winner_votes = votes
            winner_name = candidate

    # calculate the percentage of votes and format the output
    output_lines = []
    output_lines.append("Election Results")
    output_lines.append("-------------------------")
    output_lines.append(f"Total Votes: {total_votes}")
    output_lines.append("-------------------------")
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percent = votes / total_votes * 100
        output_lines.append(f"{candidate}: {percent:.3f}% ({votes})")
    output_lines.append("-------------------------")
    output_lines.append(f"Winner: {winner_name}")
    output_lines.append("-------------------------")

    # print the output to the terminal
    for line in output_lines:
        print(line)

    # export the output to a text file
    with open("output.txt", "w") as txtfile:
        for line in output_lines:
            txtfile.write(line + "\n")    
