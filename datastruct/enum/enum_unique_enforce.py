# to force an enum to have only unique values
# we apply the @unique decorator

import enum

@enum.unique
class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    # this will trigger an error with the unique applied
    by_design = 4
    closed = 1

