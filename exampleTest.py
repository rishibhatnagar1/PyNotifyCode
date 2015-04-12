''' Going to use pync to make notifications on Mac OS X , before that you need to do this: brew install terminal-notifier and then: pip install pync '''
from pync import Notifier

Notifier.notify('This is how it looks')
