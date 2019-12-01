import string

values = {'var' : 'foo'}

t = string.Template("""
        Variable : $var
        Escape : $$
        Variable in text : ${var}iable
        """)
print('Template: ', t.substitute(values))

s = """
Variable : %(var)s
Escape : %%
Variable in text: %(var)sialbe
"""

print('Interpolation : ', s % values)

s = """
Variable : {var}
Escapte : {{}}
Variable in text : {var}iable
"""

print('Format', s.format(**values))

