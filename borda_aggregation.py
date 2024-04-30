import pandas as pd
import ast
from collections import defaultdict

vote_df = pd.read_csv('sample_vote_dataset.csv')

#Since the votes are in tuple format, we convert them to list for consistency. This step is not necessary if the votes are already in list format.
votes = vote_df['votes'].apply(lambda x: list(ast.literal_eval(x)))

def borda_voting_rule(votes):
    scores = defaultdict(int)
    #We calculate the maximum score to be assigned in the borda voting rule
    num_options = len(max(votes, key=len))  

    for vote in votes:
        for idx, option in enumerate(vote):
            # assign points based on the position in the vote
            scores[option] += num_options - idx

    # Return the options sorted in descending order of scores
    return [option for option, score in sorted(scores.items(), key=lambda x: x[1], reverse=True)]

aggregation_result = borda_voting_rule(votes)
print(aggregation_result)