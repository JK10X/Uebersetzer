# Uebersetzer

This is a little repository that aims to build a solit Latin-translator.
We saw a lack in something that knows all grammar-rules and such and has a solit vocab base.

The documentation is mostly in german, because we are from germany (duh).

Using it in your own projects is easy: You need to import uebersetzer.py and can then use the bestimmmen() function to identify and translate stuff to german.
bestimmen() needs an the stuff you want to run it on as a LIST with every word as a string. For terminal input in this format you can use inputf().

# bestimmen()
bestimmen() has no dependencies on other libaries, but it needs the folder structur to be the same as in the repo, because it uses files.
bestimmen() returns a tupil of lists. The lists contain an object for each string in your input list with it identified or translated, 
where the first list contains the identification and the second the translation. This is in order to your input.
