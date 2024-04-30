import pandas as pd
import ast
from collections import defaultdict

vote_df = pd.read_csv('sample_vote_dataset.csv')

#Since the votes are in tuple format, we convert them to list for consistency. This step is not necessary if the votes are already in list format.
votes = vote_df['votes'].apply(lambda x: list(ast.literal_eval(x)))

# Function to apply Approval Voting method
def approval_voting_rule(votes):
    approvals = defaultdict(int)
    
    for vote in votes:
        for option in vote:
            approvals[option] += 1  # each option in a vote gets an approval
    
    # Return only the options, not the approvals, sorted in descending order of approvals
    return [option for option, count in sorted(approvals.items(), key=lambda x: x[1], reverse=True)]

aggregation_result = approval_voting_rule(votes)
print(aggregation_result)