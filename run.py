from abc import ABC, abstractmethod
from collections import Counter, defaultdict
import random

class VotingAlgorithm(ABC):
    @abstractmethod
    def describe(self):
        """Provides a description of the algorithm and examples."""
        pass

    @abstractmethod
    def run(self, votes):
        """Executes the voting algorithm."""
        pass

class FirstPastThePost(VotingAlgorithm):
    def describe(self):
        description = "First Past The Post (FPTP): The movie with the most top-ranked votes wins."
        example = "Example: If most people rank 'Movie A' as their top choice, 'Movie A' wins."
        return description + "\n" + example

    def run(self, votes):
        vote_counts = Counter(vote[0] for vote in votes if vote)
        return vote_counts.most_common(1)[0][0]

class BordaCount(VotingAlgorithm):
    def describe(self):
        description = "Borda Count: Points are assigned based on the position in the ranking, " \
                      "and the movie with the highest total points wins."
        example = "Example: 1st place vote gets N points, 2nd place gets N-1, etc. " \
                  "The movie with the highest total points wins."
        return description + "\n" + example

    def run(self, votes):
        candidate_scores = defaultdict(int)
        for person_votes in votes:
            for i, vote in enumerate(person_votes):
                candidate_scores[vote] += len(person_votes) - i
        return max(candidate_scores, key=candidate_scores.get)

class InstantRunoffVoting(VotingAlgorithm):
    def describe(self):
        description = "Instant Runoff Voting (IRV): If no movie has a majority of top-ranked votes, " \
                      "the movie with the fewest votes is eliminated, and votes are redistributed " \
                      "based on the next preference until one movie has a majority."
        example = "Example: If no movie gets more than 50% of the top votes, the least popular movie is " \
                  "eliminated and votes are redistributed to the next preference."
        return description + "\n" + example

    def run(self, votes):
        while True:
            first_choices = [person_votes[0] for person_votes in votes if person_votes]
            vote_counts = Counter(first_choices)

            for candidate, count in vote_counts.items():
                if count > len(votes) / 2:
                    return candidate

            lowest_candidates = eliminate_lowest(vote_counts)
            for i in range(len(votes)):
                votes[i] = [vote for vote in votes[i] if vote not in lowest_candidates]

            if not any(votes[i] for i in range(len(votes))):
                return None

# Helper function for IRV
def eliminate_lowest(candidate_counts):
    lowest = min(candidate_counts.values())
    return [candidate for candidate, count in candidate_counts.items() if count == lowest]

# Main function
def main(votes):
    algorithms = [FirstPastThePost(), BordaCount(), InstantRunoffVoting()]
    selected_algorithm = random.choice(algorithms)

    print("Selected Algorithm:", selected_algorithm.describe())
    winner = selected_algorithm.run(votes)
    print("Winner:", winner)

# Sample votes
sample_votes = [
    [1, 3, 4, 2, 5],
    [2, 3, 4, 5, 1],
    [2, 4, 3, 1, 5],
    [1, 3, 4, 2, 5]
]

# Run the main function with sample votes
main(sample_votes)
