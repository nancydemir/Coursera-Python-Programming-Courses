# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

def date(month, day):
    """
    Given numbers month and day, returns a string of the form '2/12',
    with the month followed by the day.
    """
    return str(month) + "/" + str(day)

print date(2, 12)