import os
import csv
election_csv = os.path.join("Resources", "election_data.csv")
with open("election_data.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
votes = 0
vote_count = []
candidates = []
for row in csv_reader
votes = votes + 1
candidate = row [1]
if candidate in candidates
candidate_index = candidates.index(candidate)
           vote_count[candidate_index] = vote_count[candidate_index] + 1
