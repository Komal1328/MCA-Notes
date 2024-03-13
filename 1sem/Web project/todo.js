const inputBox=document.getElementById("input-box");
const list=document.getElementById("list");
const edate=document.getElementById("edate");
function addtask() 
{
	if(inputBox.value==='')
		alert("Enter something");
	else if(edate.value==='')
		alert("Enter end date");
	else
	{
		let li=document.createElement("li");
		li.innerHTML=inputBox.value;
		list.appendChild(li);
		let ed=document.createElement("ed");
		ed.innerHTML=edate.value;
		li.appendChild(ed);
		let span=document.createElement("span");
		span.innerHTML="\u00d7";
		li.appendChild(span);
	}
	inputBox.value="";
	edate.value="";
	saveData();
}

list.addEventListener("click",function(e)
{
	if(e.target.tagName==='LI')
	{
		e.target.classList.toggle("checked");
		saveData();
	}
	else if(e.target.tagName==="SPAN")
	{
		e.target.parentElement.remove();	
		saveData();
	}
},false);

function saveData()
{
	localStorage.setItem("data",list.innerHTML);
}

function showlist()
{
	list.innerHTML= localStorage.getItem("data");
}
showlist();