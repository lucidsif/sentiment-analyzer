import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        # read positive list and store each word into a set
        positive_file = open(positives, 'r')
        self.positive_set = set()
        for line in positive_file:
            self.positive_set.add(line.rstrip())
        # read negative list and store each word into a set
        negative_file = open(negatives, 'r')
        self.negative_set = set()
        for line in negative_file:
            self.negative_set.add(line.rstrip())
        # initialize a score counter
        self.score = 0

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        for token in tokens:
            if (token in self.positive_set):
                self.score += 1
            elif (token in self.negative_set):
                self.score -=1
            else: 
                self.score += 0
        return self.score
