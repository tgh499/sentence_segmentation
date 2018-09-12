# import regular expression package
import re

# open the input file, and read its content
f= open('input.txt','r')
text = f.read()


# regular expression applied
# the regex contains one disjunction
# the first one takes care of sentences with Mr./MR. etc.
# the second part takes care of the remaining sentences
sents = re.findall(r'(([\"\']?(M[rR][sS]?\.?)\s[A-Za-z]*([^\.?!]?)*((\.\s[A-Za-z])?)*([^\.?!]?)*[\"\']?[\.?!][\"\']?)|(([\"\']?[A-Z][^\.!?]*[\.!?][\"\']?)))', text)
# just in case there are some empty 
sents = [x for x in sents if x != '']



print("Total number of sentences: " + str(len(sents)))
print("Please check your folder for the \"output.txt\" file.")


f = open("output.txt", "w")
for i,j in enumerate(sents):
	temp = []

	# remove empty lists from j
	tempJ = [x for x in j if x != '']

	# this for loop is to find the maxmimum length of lists in j
	for k in j:
		temp.append(len(k))
	tempMax = max(temp)

	# while printing, only print the string with maximum length
	# This is to deal with regular expression groups.
	for m,n in enumerate(j):
		if len(n) == tempMax:
			f.write((str(i+1) + ". " + j[m])+"\n")
			# sometimes the string is stored in multiple groups
			# once the first string is found and printed, there is no point continuing
			break

		