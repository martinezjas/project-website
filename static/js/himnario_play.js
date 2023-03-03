document.getElementById("audio").addEventListener("ended", function () {
  window.location.href = "/himnario";
});
const res = JSON.parse(lyrics);
// console.log(JSON.stringify(res));
console.log(res[0].verse.content);
var audio = document.getElementById("audio");
audio.addEventListener(
  "timeupdate",
  function () {
    var currentTime = Math.floor(audio.currentTime);
    console.log(currentTime);
    /* var last_time = res[res.length - 1].timestamp;
    console.log(last_time)
    let i = 0;
    while (i < res.length) {
      if (currentTime == res[i].timestamp) {
        document.getElementById("text").innerHTML = res[i].verse.content;
        console.log(currentTime);
        i++;
      }
    } */
  },
  false
);
