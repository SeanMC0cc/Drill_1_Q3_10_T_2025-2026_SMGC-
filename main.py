from pyscript import display, document

def calculate_grade(e):
    input1 = int(document.getElementById("input1").value)
    input2 = int(document.getElementById("input2").value)
    document.getElementById("output").innerHTML = ""

    if (input1 + input2) / 2 < 75:
        display("Failed", target="output")
    else:
        display("Passed", target="output")
    average = (input1 + input2) / 2
    result = f'''{input1} {input2}'s average grade is {average:.2f}. 
    Average grade: {average:.2f}
    '''
    display(result, target="output")