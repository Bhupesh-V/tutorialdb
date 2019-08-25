setTimeout(function focusMe() {
	document.getElementById("focus-here").scrollIntoView();
});

function share(title, link) {
	if (navigator.share) {
		navigator.share({
		title: title,
		url: link,
		})
		.then(() => console.log('Successful Share'))
		.catch((error) => console.log('Error sharing', error));
	}
}

function checkEmpty() {
	var input = document.getElementById("search-bar");
	if (input.value == "" || input.value == null) {
		return false;
	}
	else {
		return true;
	}
}