async function getMember(inputUserame) {
  const searchMember = document.querySelector(".searchMember")
  let data = await fetch(`/api/member?username=${inputUserame}`)
  // console.log(data)
  let parsedData = await data.json()
  // console.log(parsedData.data)
  if (parsedData.data === null) {
    searchMember.innerHTML = "無此會員"
  }
  else {
    // console.log(typeof (parsedData))
    // 取得name
    name = parsedData.data["name"]
    // 取得username
    username = parsedData.data["username"]

    searchMember.innerHTML = `${name} (${username})`
  }
}

function updateUsername(updateName) {
  const newName = document.querySelector(".newName")
  let url = "/api/member"
  let newResult = {
    name: updateName
  }
  let options = {
    method: "PATCH",
    body: JSON.stringify(newResult),
    headers: {
      "Content-type": "application/json",
    }
  }
  fetch(url, options)
    .then(response => newName.innerHTML = "更新成功")
}
