{% load static %}

setTimeout(function focusMe(){
  document.getElementById("focus-here").scrollIntoView();
});

function share(title, link){
  if (navigator.share) {
    navigator.share({
    title: title,
    url: link,
    })
    .then(() => console.log('Successful Share'))
    .catch((error) => console.log('Error sharing', error));
  }
}

async function registerSW(){
  if('serviceWorker' in navigator) {
    try{
        await navigator.serviceWorker.register("{% static 'app/js/sw.js' %}");
    } catch(e) {
      console.log('SW Registration Failed.');
    }
  }
}