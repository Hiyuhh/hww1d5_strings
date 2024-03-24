# 1. Product Review Analysis
# Task 1: Keyword Highlighter
reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

result = [ ]

def change_word():
    for words in reviews:
        changed_word = words.replace("good", "GOOD") .replace("excellent", "EXCELLENT")\
        .replace("bad", "BAD") .replace("Poor", "POOR") .replace("average", "AVERAGE")
        result.append(changed_word)
        print(changed_word)

change_word()

# Task 2: Sentiment Tally
reviews = [
    "Omen is a great smokes player.",
    "Valorant is a fantastic game! But it's bad because it can become additive.",
    "You will get terrible and disappointing teammates most of the time.",
    "Despite having awful teammates you will still have an amazing time playing it!",
    "I main Cypher because he is an excellent sentinels character."
]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

def word_count(reviews):
    positive_count = 0
    negative_count = 0
    splitted_review = review.split()
    for word in splitted_review:
        if word in positive_words:
            positive_count +=1
        elif word in negative_words:
            negative_count +=1
    return negative_count, positive_count

for review in reviews:
    negative_count, positive_count = word_count(review)
    print(f"Reviews: {review}")
    print(f"Positive words: {positive_count}\nNegatitive words: {negative_count}")

word_count(reviews)

# Task 3: Review Summary
# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

valorant = ["The day after IGNITION, the world is in shock. VALORANT PROTOCOL— a covert operation \
set up to prevent just such disasters— scrambles to make sense of the unfolding events. \
Analysis of Venice and the remnants of the package suggests the detonation of a device \
harnessing the power of Radianite, previously thought to be a clean and safe source of energy."]
update = []
def script():
    word_count = 0
    for word in valorant:
        splitted_script = word.split()
    for word in splitted_script:
        if word_count < 30:
            update.append(word)
            word_count += 1
        elif word_count == 30:
            break
    print(" ".join(update) + "...")
script()