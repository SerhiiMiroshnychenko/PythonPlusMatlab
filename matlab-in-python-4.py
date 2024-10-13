from oct2py import Oct2Py

oc = Oct2Py()

script = """
function y = firstTest()
    x = [1 2 3];
    y = x.*10;
    disp(y)
end
"""

with open("firstTest.m", "w+") as f:
    f.write(script)

oc.firstTest()
