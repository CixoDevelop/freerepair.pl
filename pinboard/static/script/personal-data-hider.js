/*
 * Ten skrypt jest uzywany
 * do ukrywania i pokazywania 
 * danych kontaktowych uzytkownikow
 */

const show_data = "Pokaż dane kontaktowe!"
const hide_data = "Ukryj dane kontaktowe!"

var actual_show = false;

document.getElementsByTagName("body")[0].onload = function (){
	document.querySelectorAll(".service-box").forEach(
		function (element){
			element.querySelector("#show").onclick = showData;	
		}
	);
}

function showData(){
	if(actual_show != false)
		actual_show.click()
	actual_show = this;
	
	this.value = hide_data;
	this.onclick = hideData;
	
	this.parentElement.querySelector("ul").style.opacity = "1";
}

function hideData(){
	actual_show = false;
	
	this.value = show_data;
	this.onclick = showData;
	
	this.parentElement.querySelector("ul").style.opacity = "0";
}