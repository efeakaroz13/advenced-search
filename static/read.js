oldOne = ""
function checkSelect(){
	
	var thevalue =  document.getElementById("selected").value;
	console.log(thevalue)
	try{
		document.getElementById(oldOne).style.display = "none";
	}
	catch{
		console.log("start")
	}
	document.getElementById(thevalue).style.display = "";
	oldOne=thevalue;
}
checkSelect()
setInterval(checkSelect,1000)