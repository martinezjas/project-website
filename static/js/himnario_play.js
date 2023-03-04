document.getElementById("audio").addEventListener("ended", function () {
  window.location.href = "/himnario";
});
var audio = document.getElementById("audio");
const res = JSON.parse(lyrics);
const end_card_time = Math.floor(audio.duration) - 4;
var i = 0;
const firstTime = res[0].timestamp - 1;
var hasBreak = false;
audio.addEventListener(
  "timeupdate",
  function () {
    var currentTime = Math.floor(audio.currentTime);
    if (currentTime == firstTime) {
      document.getElementById("title").hidden = true;
      document.getElementById("themes").hidden = true;
      document.getElementById("title-div").style.position = "fixed";
      document.getElementById("lyrics-div").style.position = "relative";
      document.getElementById("lyrics").hidden = false;
    }
    var curInterval = setInterval(function () {
      if (i < res.length && !hasBreak) {
        if (currentTime == res[i].timestamp - 1) {
          document.getElementById("lyrics").innerHTML = res[
            i
          ].verse.content.replace(/(\.\s+|;\s+|!\s+|\?\s+)/g, "$1<br>");
          verse_number = res[i].verse.number;
          if (verse_number == 0) {
            verse_number = "Coro";
          }
          document.getElementById("verseno").innerHTML = verse_number;
          i = i + 1;
          if (i == res.length) {
            document.getElementById("end_icon").hidden = false;
          }
        }
      } else {
        clearInterval(curInterval);
      }
    }, 500);
  },
  false
);
var myDocument = document.documentElement;
var myButton = document.getElementById("fullscreen-btn");

myButton.addEventListener("click", toggleFullscreen)
myDocument.addEventListener("keydown", function (e) {
  if (e.key == "f" || e.key == "F") {
    toggleFullscreen();
  }
});

function toggleFullscreen() {
  if (
    (document.fullScreenElement && document.fullScreenElement !== null) ||
    (!document.mozFullScreen && !document.webkitIsFullScreen)
  ) {
    if (document.documentElement.requestFullScreen) {
      document.documentElement.requestFullScreen();
    } else if (document.documentElement.mozRequestFullScreen) {
      document.documentElement.mozRequestFullScreen();
    } else if (document.documentElement.webkitRequestFullScreen) {
      document.documentElement.webkitRequestFullScreen(
        Element.ALLOW_KEYBOARD_INPUT
      );
    }
  } else {
    if (document.cancelFullScreen) {
      document.cancelFullScreen();
    } else if (document.mozCancelFullScreen) {
      document.mozCancelFullScreen();
    } else if (document.webkitCancelFullScreen) {
      document.webkitCancelFullScreen();
    }
  }
}

var leftButton = document.getElementById("go-back");
var rightButton = document.getElementById("go-forward");

leftButton.addEventListener("click", function () {
  hasBreak = true;
  document.getElementById("title").hidden = true;
  document.getElementById("themes").hidden = true;
  document.getElementById("title-div").style.position = "fixed";
  document.getElementById("lyrics-div").style.position = "relative";
  document.getElementById("lyrics").hidden = false;
  if (i > 0) {
    i = i - 1;
  }
  document.getElementById("lyrics").innerHTML = res[i].verse.content.replace(
    /(\.\s+|;\s+|!\s+|\?\s+)/g,
    "$1<br>"
  );
  verse_number = res[i].verse.number;
  if (verse_number == 0) {
    verse_number = "Coro";
  }
  document.getElementById("verseno").innerHTML = verse_number;
  if (i + 1 == res.length) {
    document.getElementById("end_icon").hidden = false;
  }
});

var firstClick = false;
rightButton.addEventListener("click", function () {
  hasBreak = true;
  document.getElementById("title").hidden = true;
  document.getElementById("themes").hidden = true;
  document.getElementById("title-div").style.position = "fixed";
  document.getElementById("lyrics-div").style.position = "relative";
  document.getElementById("lyrics").hidden = false;
  if (i < res.length && firstClick) {
    i = i + 1;
  } else if (i < res.length && !firstClick) {
    i = 0;
    firstClick = true;
  }
  document.getElementById("lyrics").innerHTML = res[i].verse.content.replace(
    /(\.\s+|;\s+|!\s+|\?\s+)/g,
    "$1<br>"
  );
  verse_number = res[i].verse.number;
  if (verse_number == 0) {
    verse_number = "Coro";
  }
  document.getElementById("verseno").innerHTML = verse_number;
  if (i + 1 == res.length) {
    document.getElementById("end_icon").hidden = false;
  }
});
