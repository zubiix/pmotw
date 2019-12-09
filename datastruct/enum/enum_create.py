import enum

class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_commited = 2
    fix_released = 1

print('Member name : {}'.format(BugStatus.wont_fix.name))
print('Member name : {}'.format(BugStatus.wont_fix.value))
