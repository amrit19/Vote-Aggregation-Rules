import pandas as pd
import ast
from collections import defaultdict

vote_df = pd.read_csv('sample_vote_dataset.csv')

#Since the votes are in tuple format, we convert them to list for consistency. This step is not necessary if the votes are already in list format.
votes = vote_df['votes'].apply(lambda x: list(ast.literal_eval(x)))

def plurality_voting_rule(votes):
    counts = defaultdict(int)
    
    # Only the first choice is counted in plurality voting
    for vote in votes:
        if vote:  # check if vote is not empty
            counts[vote[0]] += 1  # increment the count for the top choice

    # Return the options sorted by plurality scores in descending order
    return [option for option, count in sorted(counts.items(), key=lambda x: x[1], reverse=True)]

aggregation_result = plurality_voting_rule(votes)
print(aggregation_result)