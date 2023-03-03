document.getElementById("audio").addEventListener("ended", function () {
  window.location.href = "/himnario";
});
const res = JSON.parse(lyrics);
var audio = document.getElementById("audio");
var i = 0;
var firstTime = res[0].timestamp - 1;
audio.addEventListener(
  "timeupdate",
  function () {
    var currentTime = Math.floor(audio.currentTime);
    if (currentTime == firstTime) {
      document.getElementById("title").hidden = true;
      document.getElementById("title-div").style.position = "fixed";
      document.getElementById("lyrics-div").style.position = "relative";
      document.getElementById("lyrics").hidden = false;
    }
    var curInterval = setInterval(function () {
      if (i < res.length) {
        if (currentTime == res[i].timestamp - 1) {
          document.getElementById("lyrics").innerHTML = res[i].verse.content;
          i = i + 1;
        }
      } else {
        clearInterval(curInterval);
      }
    }, 500);
  },
  false
);
