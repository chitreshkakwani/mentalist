from __future__ import division
from collections import defaultdict

class NaiveBayesClassifier:
	# Initialize the index.
	# The index is a 2-D array implemented using nested dictionaries
	index = defaultdict(lambda: defaultdict(int))
	# Two categories in which tweets are to be classified,
	# positive and negative
	categories = ["pos", "neg"]
	# Initial token count for each category
	categoryTokenCounts = {"pos":0, "neg":0}
	tokenCount = 0
	categoryTweetCounts = {"pos":0, "neg":0}
	tweetCount = 0
	prior = {"pos":0.5, "neg":0.5}
	
	def addToIndex(self, tweet, tweetCategory, limit = 0):
		if not tweetCategory in self.categories:
			raise Exception("Category not found")
		# Increment tweet count
		self.tweetCount += 1
		# Increment tweet count for the category
		self.categoryTweetCounts[tweetCategory] += 1
		tokens = tweet.split()
		#print tokens
		for token in tokens:
				self.index[token][tweetCategory] += 1
				self.categoryTokenCounts[tweetCategory] += 1
				self.tokenCount += 1

		#print self.index

	def classify(self, tweet):
		
		#Set the prior probability, which is assumed to be 0.5 for each category
		self.prior["pos"] = self.categoryTweetCounts["pos"]/self.tweetCount
		self.prior["neg"] = self.categoryTweetCounts["neg"]/self.tweetCount
		tokens = tweet.split()
		#print tokens
		#Removing noise words from the list of tokens
		lines = [line.strip() for line in open("noise_words")]
		lines.sort()
		print lines
		tokens = set(tokens)-set(lines)
		
			

			
		categoryScores = {"pos":1, "neg":1}
		print tokens	
		#print self.index	
		for category in self.categories:
			#print category
			for token in tokens:
				# Get the count of token in the category
				count = self.index[token][category]
				# For each token calculate category scores
			categoryScores[category] *= (count + 1)/(self.categoryTokenCounts[category] + self.tokenCount)
			
			categoryScores[category] = self.prior[category] * categoryScores[category]

		#print categoryScores
		# Return the category with a bigger score
		return max(categoryScores, key = categoryScores.get)

# Examples
# Train the classifier
classifier = NaiveBayesClassifier()
classifier.addToIndex("this is a happy tweet", "pos")	
classifier.addToIndex("this is a sad tweet", "neg")	
classifier.addToIndex("some random statement", "pos")	
classifier.addToIndex("this is wrong", "neg")
classifier.addToIndex("what the hell", "neg")

# Classify tweets	
print classifier.classify("what went wrong with this tweet")
print classifier.classify("who the hell are you")
print classifier.classify("I'm happy today")
