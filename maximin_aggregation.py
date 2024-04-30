import pandas as pd
import ast
from collections import defaultdict
from itertools import combinations

vote_df = pd.read_csv('sample_vote_dataset.csv')

#Since the votes are in tuple format, we convert them to list for consistency. This step is not necessary if the votes are already in list format.
votes = vote_df['votes'].apply(lambda x: list(ast.literal_eval(x)))

# Function to apply Maximin method
def maximin_voting_rule(votes):
    scores = defaultdict(int)
    
    for vote in votes:
        for idx, option in enumerate(vote):
             if scores[option] > idx or option not in scores:
                scores[option] = idx  # assign the minimum position the option has ever appeared
    
    # Return only the options, not the scores, sorted in ascending order of scores
    return [option for option, score in sorted(scores.items(), key=lambda x: x[1])]

aggregation_result = maximin_voting_rule(votes)
print(aggregation_result)