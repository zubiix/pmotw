import textwrap
from textwrap_example import sample_text

dedented_text = textwrap.dedent(sample_text)
original = textwrap.fill(dedented_text, width = 50)

print('Original:\n')
print(original)

# shorten the original text
shortened = textwrap.shorten(original, 100)
# make the shortened text same width with original
shortened_wrapped = textwrap.fill(shortened, width = 50)

print('\Shortened\n')
print(shortened_wrapped)
