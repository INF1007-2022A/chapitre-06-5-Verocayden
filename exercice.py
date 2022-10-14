#!/usr/bin/env python
# -*- coding: utf-8 -*-


def check_brackets(text, brackets): # FINISHED
	# Choisir la structure de données la plus appropriée. Essayer de le faire soi-même. Très bon exercice.
	op_brackets = list(brackets[::2]) # Ouvrants
	cl_brackets = list(brackets[1::2]) # Fermants
	trace = []

	for caracter in text:
		if caracter in op_brackets:
			trace.append(caracter)
		elif caracter in cl_brackets:
			if op_brackets[cl_brackets.index(caracter)] in trace or trace[-1] == cl_brackets[cl_brackets.index(caracter)] or len(trace) != 0:
				trace.pop() # Like a pile
			else: # Incorrect order
				return False

	if len(trace) % 2 != 0: # Missing bracket
		return False

	return True

def remove_comments(full_text, comment_start, comment_end): # FINISHED
	while True: # Iterate to delete all comments in the text.
		if comment_start not in full_text and comment_end not in full_text:
			return full_text
		elif (comment_start in full_text and comment_end not in full_text) or (comment_start not in full_text and comment_end in full_text):
			return None
		elif (full_text.find(comment_start) > full_text.find(comment_end)):
			return None
		elif comment_start in full_text and comment_end in full_text:
			full_text = full_text[:full_text.find(comment_start)] + full_text[full_text.find(comment_end)+(len(comment_end))::]


def get_tag_prefix(text, opening_tags, closing_tags): # FINISHED
	for tag in opening_tags:
		if text[:len(tag)] == tag:
			return(tag, None)
	for tag in closing_tags:
		if text[:len(tag)] == tag:
			return(None, tag)
	return (None, None)

def check_tags(full_text, tag_names, comment_tags): # DEBUG
	trace = []
	op_tags = [f"<{tag}>" for tag in tag_names]
	cl_tags = [f"</{tag}>" for tag in tag_names]

	# Remove all comments
	while comment_tags[0] in full_text and comment_tags[1] in full_text:
		op_comment = full_text.find(comment_tags[0])
		cl_comment = full_text.find(comment_tags[1])
		full_text = full_text[:op_comment] + full_text[cl_comment+len(comment_tags[1]):]

	if ((comment_tags[0] in full_text) and (comment_tags[1] not in full_text)) or ((comment_tags[0] not in full_text) and (comment_tags[1] in full_text)):
		return False

	# Check openings and endings
	for word in full_text.split():
		if word in op_tags:
			trace.append(word)
		elif word in cl_tags:
			if op_tags[cl_tags.index(word)] in trace or trace[-1] == cl_brackets[cl_brackets.index(caracter)] or len(trace) != 0:
				trace.pop()
			else: # Incorrect order
				return False

	if len(trace) % 2 != 0:
		return False

	return True


if __name__ == "__main__":
	brackets = ("(", ")", "{", "}")
	yeet = "(yeet){yeet}"
	yeeet = "({yeet})"
	yeeeet = "({yeet)}"
	yeeeeet = "(yeet"
	print(check_brackets(yeet, brackets))
	print(check_brackets(yeeet, brackets))
	print(check_brackets(yeeeet, brackets))
	print(check_brackets(yeeeeet, brackets))
	print()

	spam = "Hello, /* OOGAH BOOGAH */world!"
	eggs = "Hello, /* OOGAH BOOGAH world!"
	parrot = "Hello, OOGAH BOOGAH*/ world!"
	print(remove_comments(spam, "/*", "*/"))
	print(remove_comments(eggs, "/*", "*/"))
	print(remove_comments(parrot, "/*", "*/"))
	print()

	otags = ("<head>", "<body>", "<h1>")
	ctags = ("</head>", "</body>", "</h1>")
	print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("</h1></body>", otags, ctags))
	print(get_tag_prefix("</body>", otags, ctags))
	print()

	spam = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    </title>"
		"  </head>"
		"  <body>"
		"    <h1>Hello, world</h1>"
		"    <!-- Les tags vides sont ignorés -->"
		"    <br>"
		"    <h1/>"
		"  </body>"
		"</html>"
	)
	eggs = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    <!-- Il manque un end tag"
		"    </title>-->"
		"  </head>"
		"</html>"
	)
	parrot = (
		"<html>"
		"  <head>"
		"    <title>"
		"      Commentaire mal formé -->"
		"      Example"
		"    </title>"
		"  </head>"
		"</html>"
	)
	tags = ("html", "head", "title", "body", "h1")
	comment_tags = ("<!--", "-->")
	print(check_tags(spam, tags, comment_tags))
	print(check_tags(eggs, tags, comment_tags))
	print(check_tags(parrot, tags, comment_tags))
	print()

