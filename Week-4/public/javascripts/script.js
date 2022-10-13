// 直接更改url
function myFunction() {
  var e = document.getElementById("input").value;
  var theUrl = "http://127.0.0.1:3000/square/".concat(e);
  window.location.replace(theUrl);
}

let seconds = 10;

function countdown() {
  seconds = seconds - 1;
  if (seconds < 0) {
    window.location = "/";
  } else {
    // 更新剩餘秒數
    document.getElementById("countdown").innerHTML = seconds;
    // 倒數
    window.setTimeout("countdown()", 1000);
  }
}

countdown();
