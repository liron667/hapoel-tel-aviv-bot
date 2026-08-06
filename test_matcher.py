"""Minimal check for the relevance filter. Run: python test_matcher.py"""
from bot import matches

KW = ["הפועל תל אביב", 'הפועל ת"א', "Hapoel Tel Aviv"]
EX = ["כדורסל"]

assert matches("הפועל תל אביב ניצחה בליגת העל", KW, EX)
assert matches("Hapoel Tel Aviv sign a new striker", KW, EX)
assert not matches("מכבי תל אביב הפסידה", KW, EX)          # different club
assert not matches("הפועל תל אביב בכדורסל גברה", KW, EX)   # basketball excluded
print("ok")
