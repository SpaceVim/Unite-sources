from .base import Base
import re


class Source(Base):

    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'unicode'
        self.kind = 'unicode'

    def gather_candidates(self, context):
        candidates = []
        for [ugroup, path] in self.vim.call("unicode#groups"):
            candidates.append({
                'kind': 'unicode',
                'word': ugroup
                })
        return candidates
