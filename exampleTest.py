''' Going to use pync to make notifications on Mac OS X , before that you need to do this: brew install terminal-notifier and then: pip install pync '''
from pync import Notifier
import os
Notifier.notify('This is how it looks')
Notifier.notify('Hello World', title='Python')
Notifier.notify('Hello World', group=os.getpid())
Notifier.notify('Hello World', activate='com.apple.Safari')
Notifier.notify('Hello World', open='http://github.com/')
Notifier.notify('Hello World', execute='say "OMG"')

Notifier.remove(os.getpid())

Notifier.list(os.getpid())
