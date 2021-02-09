const things = {
  stuff: [
    {
      tag: `img`,
      src: `https://whitneymedia.org/assets/image/823189/large_CallaLilyVendor.jpg`
    },{
      tag: `p`,
      innerText: `I'm a multimedia artist and software engineer currently working as an educator and maintaining my studio practice as an ongoing resident at the Verge Center for the Arts in Sacramento, CA. I am making a futile effort to join the migration off of social media by focusing my efforts towards an email newsletter, blog, art zines and pop-up exhibitions. I'm actively seeking out studio visits and collaboration oppourtunities so please don't hesitate to drop me a regular old email any time.`
    },{
      tag: `h1`,
      innerText: `Tom Betthauser`
    },{
      tag: `p`,
      innerText: `I'm a multimedia artist and software engineer currently working as an educator and maintaining my studio practice as an ongoing resident at the Verge Center for the Arts in Sacramento, CA. I am making a futile effort to join the migration off of social media by focusing my efforts towards an email newsletter, blog, art zines and pop-up exhibitions. I'm actively seeking out studio visits and collaboration oppourtunities so please don't hesitate to drop me a regular old email any time.`
    },{
      tag: `a`,
      innerText: `github`,
      target: `new`,
      href: `https://github.com/tombetthauser`
    },{
      tag: `ul`,
      babies: [
        {
          tag: `li`,
          innerText: `testing!`
        },{
          tag: `li`,
          innerText: `testing again!`
        }
      ]
    },
  ]
}

const main = document.querySelector("#main-thing");
const body = document.querySelector("body");
const title = document.querySelector("title");

const turtler = thing => {
  thing = Array.isArray(thing) ? thing : thing.stuff;
  thing.forEach(thing => {
    let baby = document.createElement(thing.tag);
    Object.keys(thing).forEach(key => {
      if (key !== `tag`) baby[key] = thing[key];
      if (baby.babies) turtler(baby.babies);
    })
    main.appendChild(baby);
  })
}

turtler(things);