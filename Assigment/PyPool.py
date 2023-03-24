import os
import csv


csvpath = r"Resources\election_data.csv"


with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
   
    totalVotes = 0
    
    candidateDict = {}

    
    for row in csvreader:        
             
        totalVotes +=1

    
        
        candidate = row[2]
        if candidate in candidateDict.keys():
            candidateDict[candidate] +=1
        else:
            candidateDict[candidate] = 1

  
winner = max(candidateDict, key=candidateDict.get)


percentDict = {}
for key in candidateDict.keys():
    percentage = candidateDict[key] / totalVotes
    percentDict[key] = percentage


listOfStrings = []
for key in percentDict.keys():
    myString = key + ": " + str(round(percentDict[key]*100,3)) + "% (" + str(candidateDict[key]) + ")"
    listOfStrings.append(myString)

finalString = "\n".join(listOfStrings)


summaryTable = f"""Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
{finalString}
-------------------------
Winner: {winner}
-------------------------"""
print(summaryTable)

with open("poll_results.txt", "w") as file1:
    file1.write(summaryTable)