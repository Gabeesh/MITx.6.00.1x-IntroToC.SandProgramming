from itertools import groupby

def find_long_cons_sub(s):
    class Key(object):
        '''
        The Key function returns
            1: For Increasing Sequence
            0: For Decreasing Sequence
        '''
        def __init__(self):
            self.last_char = None
        def __call__(self, char):
            resp = True
            if self.last_char:
                resp = self.last_char < char
            self.last_char = char
            return resp
    def find_substring(groups):
        '''
        The Boundary Case is when an increasing sequence
        starts just after the Decresing Sequence. This causes
        the first character to be in the previous group.
        If you do not want to handle the Boundary Case
        seperately, you have to mak the Key function a bit
        complicated to flag the start of increasing sequence'''
        yield next(groups)
        try:
            while True:
                yield next(groups)[-1:] + next(groups)
        except StopIteration:
            pass
    groups = (list(g) for k, g in groupby(s, key = Key()) if k)
    #Just determine the maximum sequence based on length
    return ''.join(max(find_substring(groups), key = len))

print find_long_cons_sub('drurotsxjehlwfwgygygxz')