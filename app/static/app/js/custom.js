setTimeout(function focusMe() {
    const elem = document.getElementById("focus-here");
    if (elem) {
        elem.scrollIntoView();
    }
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
	if (input.value === "" || input.value === null) {
		return false;
	}
	else {
		return true;
	}
}
