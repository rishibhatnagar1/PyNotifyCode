''' Going to use pync to make notifications on Mac OS X , before that you need to do this: brew install terminal-notifier and then: pip install pync '''
from pync import Notifier
import os
Notifier.notify('This is how it looks')
Notifier.notify('Hello World', title='Python')
Notifier.notify('Hello World', group=os.getpid())
Notifier.notify('Browser', activate='com.apple.Safari')
Notifier.notify('Website', open='http://github.com/')
Notifier.notify('Some execution', execute='say "I am hungry!"')

Notifier.remove(os.getpid())

Notifier.list(os.getpid())
