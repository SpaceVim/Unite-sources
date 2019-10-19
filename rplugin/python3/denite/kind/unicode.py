from ..kind.base import Base


class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        self.name = 'unicode'
        self.default_action = 'open'

    def _get_session_name(self, context):
        session_name = context['targets'][0]['word']
        return session_name

    def action_open(self, context):
        session_name = self._get_session_name(context)
        self.vim.command('echom %s' % session_name)
