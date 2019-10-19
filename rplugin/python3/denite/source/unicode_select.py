from .base import Base
import re


class Source(Base):

    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'unicode_select'
        self.kind = 'word'

    def gather_candidates(self, context):
        candidates = []
        for line in self.vim.call("unicode#words", context.args):
            candidates.append({
                'word': line
                })
        return candidates

