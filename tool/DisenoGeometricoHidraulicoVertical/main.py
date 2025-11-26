import arrr
from pyscript import document

def run(event):
    input_a = document.querySelector("#a")
    input_b = document.querySelector("#b")
    a = float(input_a.value)
    b = float(input_b.value)
    c = (a + b)
    output_div = document.querySelector("#output")
    output_div.innerText = c

