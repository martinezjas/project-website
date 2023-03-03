document.getElementById("audio").addEventListener("ended", function () {
  window.location.href = "/himnario";
});
var audio = document.getElementById("audio");
const res = JSON.parse(lyrics);
var end_card_time = Math.floor(audio.duration) - 4;
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
          document.getElementById("lyrics").innerHTML = res[i].verse.content.replace(/(\.\s+)/g,"\$1<br>")
          verse_number = res[i].verse.number;
          if (verse_number == 0) {
            verse_number = "Coro";
          }
          document.getElementById("verseno").innerHTML = verse_number;
          i = i + 1;
        }
      } else {
        clearInterval(curInterval);
      }
    }, 500);
  },
  false
);
