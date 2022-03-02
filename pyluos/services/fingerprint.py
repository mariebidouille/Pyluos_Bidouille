from .service import Service

import time

class Fingerprint(Service):
    def __init__(self, id, alias, device):
        Service.__init__(self, 'Fingerprint', id, alias, device)
        self._check = False
        self._enroll = False
        self._delete = False

    def reinit(self):
        self._push_value('reinit', None)
        time.sleep(0.01)

    def enroll(self):
        self._push_value('enroll', 1)
        time.sleep(0.01)

    def delete(self):
        self._push_value('delete',1)
    
    def check(self):
        self._check = False
        self._push_value('check', 1)
    
    def _update(self, new_state):
        Service._update(self, new_state)
        if 'check' in new_state:
            self._check = new_state['check']
        if 'enroll' in new_state:
            self._enroll = new_state['enroll']
        if 'delete' in new_state:
            self._delete = new_state['delete']