let images = [
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/54.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/56.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/62.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/70.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/11.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/17.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/18.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/26.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/27.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/28.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/29.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/30.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/32.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/38.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/43.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/44.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/51.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/49.jpg",
  "http://www.tombetthauser.com/studio/assets/images/portfolio/thumb/46.jpg"
];
let count = Math.floor(Math.random() * images.length);

document.querySelector(".studio-images-div").style.backgroundImage = `url(${images[count]})`;
count = (count + 1) % images.length;

const loader = (imageArr) => {
  imageArr.forEach(imgPath => {
    const newNode = document.createElement('div')
    const body = document.querySelector('body')
    
    newNode.style.setProperty('background-image', `url(${imgPath})`)
    body.appendChild(newNode);
  });
}

loader(images);

setInterval(() => {
  document.querySelector(".studio-images-div").style.backgroundImage = `url(${images[count]})`;
  count = (count + 1) % images.length;
}, 3000)