
const promoText = document.querySelectorAll('.promo-text')
const promotionImg = document.querySelectorAll('.promotion-img')
const titleText = document.querySelectorAll('.title-text')
const titleImg = document.querySelectorAll('.title-img')

// 新增一個陣列存放所有旅遊景點的資料
const touristSpot = []

// 新增會修改promotion資料的函數
function renderPromoList(data) {
  // promotion只有兩筆，所以迴圈只跑兩次
  for (let i = 0; i < 2; i++) {
    // 新增一個元素
    let promoP = document.createElement('p')
    // 修改元素的結構
    promoP.innerText = data[i].stitle
    //將元素放入dom結構
    promoText[i].appendChild(promoP)
    // 第一個圖片的位置
    let firstPic = 'https://' + data[i].file.split('https://')[1]
    // 變更背景圖片的位置
    promotionImg[i].style["background-image"] = `url(${firstPic})`
  }
}

// 新增會修改title資料的函數
function renderTitleList(data) {
  // promotion有八筆，所以迴圈跑八次
  for (let i = 0; i < 8; i++) {
    let titleP = document.createElement('p')
    titleP.innerText = data[i + 2].stitle
    titleText[i].appendChild(titleP)
    let firstPic = 'https://' + data[i + 2].file.split('https://')[1]
    titleImg[i].style["background-image"] = `url(${firstPic})`
  }
}




fetch(
  "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
).then(function (response) {
  return response.json();
}).then(function (data) {
  // 展開運算子... ，展開陣列元素
  touristSpot.push(...data.result.results)
  renderPromoList(touristSpot)
  renderTitleList(touristSpot)
})
