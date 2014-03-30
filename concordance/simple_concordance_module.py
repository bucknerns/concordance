"""
Created by Nathan Buckner
"""

import re


class ConcordanceGenerator(object):
    def __init__(self):
        self.concordance = {}
        self.max_word_len = 0

    @classmethod
    def fromfile(cls, fp):
        concordance = cls()
        for line_number, line in enumerate(fp):
            line = line.strip().lower()
            for word in re.split("(\W+)", line):
                if concordance.max_word_len < len(word):
                    concordance.max_word_len = len(word)
                if re.search("^[a-z]", word):
                    concordance.add_word(word, line_number+1)
        return concordance

    def add_word(self, word, line_number):
        if not self.concordance.get(word):
            self.concordance[word] = []
        self.concordance[word].append(line_number)

    def write_line(self, word, fp):
        word = word.lower()
        data = self.concordance.get(word) or []
        format_str = "{word: <{width}}{{{count}:{data}}}\n"

        fp.write(format_str.format(
            word=word, width=self.max_word_len+1, count=len(data),
            data=",".join(map(str, data))))

    def write(self, fp):
        for word in sorted(self.concordance.keys()):
            self.write_line(word, fp)
