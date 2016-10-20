from githook import HookInstaller

class GitTalk(object):
    def __init__(self, *args, **kwargs):
        pass

    def enable(self):
        HookInstaller.addHook()

    def disable(self):
        HookInstaller.rmHook()

    def trigger(self):
        pass
