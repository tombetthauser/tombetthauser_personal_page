const things = {
  stuff: [
    { tag: `a`, target: `new`,
      href: `images/image-02.jpg`,
      babies: [{ tag: `img`,
          src: `images/image-02-thumb.png`
        }]
    },{ tag: `p`,
      className: `image-text`,
      innerText: `Sacramento Collage, 8.5 x 11 in. original drawings and paintings on photocopies of original drawings and paintings, 2021`
    },{ tag: `h1`,
      innerText: `Tom Betthauser`
    },{ tag: `h2`,
      innerText: `Visual Artist / Software Engineer`
    },{ tag: `hr`,
    },{ tag: `p`,
      innerText: `Hello, I'm a multimedia artist and software developer currently working as an educator and maintaining my studio practice as an ongoing resident at the Verge Center for the Arts in Sacramento, CA. I'm making a futile effort to get off social media by focusing my efforts on an old-school email newsletter, a blog, art zines and pop-up exhibitions with other artists.`
    },{ tag: `p`,
      innerText: `I'm always up for studio visits and collaboration oppourtunities with other artists, tech people, and artists masquerading as tech people (like me) so please don't hesitate to drop me a regular old email any time.`
    },{ tag: `p`,
      innerText: `tombetthauser@gmail.com`
    },{ tag: `ul`,
      babies: [{ tag: `li`, babies: [{ tag: `a`,
              innerText: `my email newsletter thing`,
              target: `new`, href: `https://docs.google.com/forms/d/e/1FAIpQLSeUSTIFKk7IitfyXX7EeCuyEGOX8n1FqZ5SMbLVNXDAtTQ8yQ/viewform?usp=sf_link`
            }]},{ tag: `li`, babies: [{ tag: `a`,
              innerText: `my random bandcamp page`,
              target: `new`, href: `https://tombetthauser.bandcamp.com/`
            }]},{ tag: `li`, babies: [{ tag: `a`,
              innerText: `my art merch shop for buying stuff`,
              target: `new`, href: `https://www.etsy.com/shop/tombetthauser`
            }]},{ tag: `li`, babies: [{ tag: `a`,
              innerText: `my github page for computer people`,
              target: `new`, href: `https://github.com/tombetthauser`
            }]},{ tag: `li`, babies: [{ tag: `a`,
              innerText: `my linkedin page for whatever`,
              target: `new`, href: `https://www.linkedin.com/in/tombetthauser/`
            }]}]
    // },{ tag: `ul`,
    //   babies: [{ tag: `li`, babies: [{ tag: `a`,
    //           innerText: `my software development portfolio`,
    //           target: `new`, href: `https://docs.google.com/forms/d/e/1FAIpQLSeUSTIFKk7IitfyXX7EeCuyEGOX8n1FqZ5SMbLVNXDAtTQ8yQ/viewform?usp=sf_link`
    //         }]},{ tag: `li`, babies: [{ tag: `a`,
    //           innerText: `my visual arts portfolio`,
    //           target: `new`, href: `https://github.com/tombetthauser`
    //         }]},{ tag: `li`, babies: [{ tag: `a`,
    //           innerText: `my arts / tech blog`,
    //           target: `new`, href: `https://github.com/tombetthauser`
    //         }]}]
    }
  ]
}

const main = document.querySelector("#main-thing");
const body = document.querySelector("body");
const title = document.querySelector("title");

setTimeout(() => {
  body.style.opacity = "1";
}, 500)

title.innerText = "🌱 Tom Betthauser"

const turtler = (thing, mama = main) => {
  thing = Array.isArray(thing) ? thing : thing.stuff;
  thing.forEach(thing => {
    let baby = document.createElement(thing.tag);
    Object.keys(thing).forEach(key => {
      if (key !== `tag`) baby[key] = thing[key];
      if (baby.babies) turtler(baby.babies, baby);
    })
    mama.appendChild(baby);
  })
}

turtler(things);