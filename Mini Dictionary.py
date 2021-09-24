#My mini dictionary

dictionary={"mutable":"liable to change", "immutable":"unable to be changed",
            "expenditure":"the amount of money that is spent","anxious":"worried or afraid",
            "intercept":"to stop or catch somebody", "queue":"to form a line while waiting",
            "asset":"any resource owned by a business", "pathetic":"causing you to feel pity or sadness",
            "entrepreneur":"a person who makes money by starting or running businesses, especially when this involves taking financial risks",
            "repository":"a place or container in which something is stored in large quantities"}
l1=["mutable","immutable","expenditure","anxious","intercept","queue","asset","pathetic","entrepreneur","repository"]
print(l1)
word=input("enter the word from the given list \n")
print("meaning:-",dictionary[word])
