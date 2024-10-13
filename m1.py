from oct2py import Oct2Py

oc = Oct2Py()

script = """
function ans = VariablesExpressions()
    % Variables & Expressions
    myVariable = 4  % Notice Workspace pane shows newly created variable
    myVariable = 4; % Semi colon suppresses output to the Command Window
    4 + 6       % ans = 10
    8 * myVariable  % ans = 32
    2 ^ 3       % ans = 8
    a = 2; b = 3;
    c = exp(a)*sin(pi/2) % c = 7.3891
end
"""

with open("VariablesExpressions.m", "w+") as f:
    f.write(script)

oc.VariablesExpressions()