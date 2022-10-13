// 直接更改url
function myFunction() {
  var e = document.getElementById("input").value;
  var theUrl = "http://127.0.0.1:3000/square/".concat(e);
  window.location.replace(theUrl);
}
