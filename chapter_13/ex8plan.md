Firstly, decide on data structure scheme

It's confusing because I think a given word could be a prefix of something and a suffix of something else.
My first thought is to make a dictionary where the keys are the word(s), as a tuple of strings, so I can generalize it to length n. Then the values will be perhaps lists or perhaps sets. Or perhaps lists of tuples where the tuple contains the suffix and how many times it happened. actually, do that in reverse order for easier sorting.

Actually, it's simpler than that. He doesn't say to weight the selections by whether it's more or less frequently ocurrring. Although I suppose I could use a dictionary of dictionaries, where the second dictionaries keys are... no
a dictionary of a list of tuples, with each tuple having number of occurrences and having the word.

But for now, make it a dict with prefixes for keys and lists of words for values.

anyway, first task is to get the book data into a format I can work with. What do I want? I think I want a list of words from the book, in order, with repetitions. A set would take up less space but be less useful in the general case.
