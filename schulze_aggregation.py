import pandas as pd
import ast
from collections import defaultdict
from itertools import combinations
import numpy as np

vote_df = pd.read_csv('sample_vote_dataset.csv')

#Since the votes are in tuple format, we convert them to list for consistency. This step is not necessary if the votes are already in list format.
votes = vote_df['votes'].apply(lambda x: list(ast.literal_eval(x)))

# Function to apply Schulze Voting method
def schulze_voting_rule(votes):
    # Create set of all alternatives
    alternatives_set = set()
    for vote in votes:
        alternatives_set.update(vote)

    # Create mapping from alternatives to indices
    alternatives = list(alternatives_set)
    alternatives_to_indices = {alternative: i for i, alternative in enumerate(alternatives)}

    # Initialize pairwise preference matrix and strongest paths matrix
    num_alternatives = len(alternatives)
    pairwise_pref = np.zeros((num_alternatives, num_alternatives))
    strongest_paths = np.zeros((num_alternatives, num_alternatives))

    # Compute pairwise preference matrix
    for vote in votes:
        for i, j in combinations(vote, 2):
            if vote.index(i) < vote.index(j):
                pairwise_pref[alternatives_to_indices[i]][alternatives_to_indices[j]] += 1
            else:
                pairwise_pref[alternatives_to_indices[j]][alternatives_to_indices[i]] += 1

    # Initialize strongest paths matrix with pairwise preferences
    for i in range(num_alternatives):
        for j in range(num_alternatives):
            if i != j:
                strongest_paths[i][j] = pairwise_pref[i][j]

    # Compute strongest paths matrix
    for i in range(num_alternatives):
        for j in range(num_alternatives):
            if i != j:
                for k in range(num_alternatives):
                    if k != i and k != j:
                        strongest_paths[j][k] = max(strongest_paths[j][k], min(strongest_paths[j][i], strongest_paths[i][k]))

    # Compute ranking
    ranking = []
    for i in range(num_alternatives):
        rank = sum(1 for j in range(num_alternatives) if strongest_paths[i][j] > strongest_paths[j][i])
        ranking.append((alternatives[i], rank))

    # Sort alternatives by rank in descending order
    ranking.sort(key=lambda x: -x[1])

    return [alternative for alternative, rank in ranking]

aggregation_result = schulze_voting_rule(votes)
print(aggregation_result)