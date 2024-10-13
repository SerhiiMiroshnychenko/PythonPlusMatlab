from oct2py import octave

octave.eval("""
x = [1:2:20];
y = [0:9];
size(x)
size(y)
""")
