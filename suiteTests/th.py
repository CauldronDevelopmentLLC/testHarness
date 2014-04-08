class Suite:
    def __init__(self, th):
        th.Test('one', command = 'ls')
        th.Test('two', command = 'ls -R')
        th.Test('three', command = 'ls -sh')
        th.Test('four', command = 'echo %(test-four)s') # Causes KeyError
        th.Test('five', command = 'echo hello')
        th.Test('six', command = 'echo goodbye') # Fail
        th.Test('seven', command = 'echo hello')

    def build(self):
        print '***** Build ****'

    def clean(self):
        print '***** Clean ****'

    def begin(self):
        print '***** Start ****'

    def end(self):
        print '****** End *****'
