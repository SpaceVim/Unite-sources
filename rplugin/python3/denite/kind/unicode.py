from denite.base.kind import Base
from denite.util import Nvim, UserContext


class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'unicode'
        self.default_action = 'start'

    def _get_session_name(self, context):
        session_name = context['targets'][0]['word']
        return session_name

    def action_open(self, context):
        session_name = self._get_session_name(context)
        self.vim.command('echom %s' % session_name)

    def action_start(self, context: UserContext) -> None:
        context['sources_queue'].append([{
            'name': 'unicode_select',
            'args': x['action__source'][1:]
        } for x in context['targets']])
