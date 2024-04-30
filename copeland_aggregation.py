import pandas as pd
import ast
from collections import defaultdict
from itertools import combinations

vote_df = pd.read_csv('sample_vote_dataset.csv')

#Since the votes are in tuple format, we convert them to list for consistency. This step is not necessary if the votes are already in list format.
votes = vote_df['votes'].apply(lambda x: list(ast.literal_eval(x)))

# Function to apply Copeland Voting method
def copeland_voting_rule(votes):
    scores = defaultdict(int)
    alternatives_compared = defaultdict(list)
    
    for vote in votes:
        for i, j in combinations(vote, 2):
            if vote.index(i) < vote.index(j):
                scores[i] += 1
                scores[j] += 0
                alternatives_compared[i].append(j)  # store the alternative compared with 'i'
            elif vote.index(j) < vote.index(i):
                scores[j] += 1
                scores[i] += 0
                alternatives_compared[j].append(i)  # store the alternative compared with 'j'
            else:
                scores[i] += 0.5
                scores[j] += 0.5
                # In case of a tie, both alternatives are compared with each other
                alternatives_compared[i].append(j)
                alternatives_compared[j].append(i)
    
    # Return only the keys (alternatives), not the values (scores)
    return [key for key, value in sorted(scores.items(), key=lambda x: x[1], reverse=True)]

aggregation_result = copeland_voting_rule(votes)
print(aggregation_result)