var elem = document.getElementsByName("colorpad");

for (var j = 0; j < elem.length; j++){
elem[j].style.backgroundColor = randomColor({luminosity: 'light'});
}