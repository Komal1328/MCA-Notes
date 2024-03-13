<h1>Calculater</h1>
<form>
    <button type="submit" value={submit}>Calculation</button>
</form>
function onsubmit(){
    let n1=Number(prompt("Enter first number"));
    let n2=Number(prompt("Enter Second number"));
    let op=(prompt("Enter operand"));
    if(op=='+')
        let res=a+b;
        alert("Sum is:"+res);
    else if(op=='-')
        let res=a-b;
        alert("Subtraction is:"+res);
    else if(op=='*')
        let res=a*b;
        alert("Multiplication is:"+res);
    else if(op=='/')
        let res=a/b;
        alert("Division is:"+res);
}

