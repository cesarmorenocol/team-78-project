$(document).ready(function(){
   $(document).on("click",".fullscreen",function(event){
       let btnId = event.target.id.substring(event.target.id.lastIndexOf('-') + 1);
       let elem = document.getElementById(`graph-map-${btnId}`);
       elem.webkitRequestFullscreen();
  })
});

function openFullscreen() {
  if (elem.requestFullscreen) {
    elem.requestFullscreen();
  } else if (elem.mozRequestFullScreen) { /* Firefox */
    elem.mozRequestFullScreen();
  } else if (elem.webkitRequestFullscreen) { /* Chrome, Safari and Opera */
    elem.webkitRequestFullscreen();
  } else if (elem.msRequestFullscreen) { /* IE/Edge */
    elem.msRequestFullscreen();
  }
}