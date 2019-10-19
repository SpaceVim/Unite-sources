# ============================================================================
# FILE: neoyank.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

from .base import Base
import re


class Source(Base):

    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'unicode'
        self.kind = 'unicode'

    def gather_candidates(self, context):
        candidates = []
        for [ugroup, path] in self.vim.eval("map(split(globpath(g:unite_unicode_data_path, '*.txt'), '\n'), '[fnamemodify(v:val, \":t:r\"), fnamemodify(v:val, \":p\")]')"):
            candidates += [ugroup]
        return candidates
