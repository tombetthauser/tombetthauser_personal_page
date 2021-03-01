const things = {
  stuff: [
    { tag: `a`, href: `images/image-02.jpg`,
      babies: [{ tag: `img`,
          src: `images/image-02-thumb.png`
        }]
    },{ tag: `p`,
      className: `image-text`,
      innerText: `Office Collage, 8.5 x 11 in. original drawings and paintings on photocopies of original drawings and paintings, 2021`
    },{ tag: `h1`,
      innerText: `Tom Betthauser`
    },{ tag: `h2`,
      innerText: `Visual Artist / Software Engineer`
    },{ tag: `hr`,
    },{ tag: `p`,
      innerText: `Hello, I'm a multimedia artist and software developer currently working as an educator and maintaining my studio practice as an ongoing resident at the Verge Center for the Arts in Sacramento, CA.`
    },{ tag: `p`,
      innerText: `I'm always up for studio visits and collaboration opportunities with other artists, tech people, and artists masquerading as tech people (like me) so please don't hesitate to drop me a regular old email any time.`
    },{ tag: `p`,
      innerText: `tombetthauser@gmail.com`
    },{ tag: `hr`
    },{ tag: `p`,
      innerText: `Some me-related links...`
    },{ tag: `ul`,
      babies: [{ tag: `li`, babies: [{ tag: `a`,
            //   innerText: `my email newsletter thing`,
            //   href: `https://docs.google.com/forms/d/e/1FAIpQLSeUSTIFKk7IitfyXX7EeCuyEGOX8n1FqZ5SMbLVNXDAtTQ8yQ/viewform?usp=sf_link`
            // }]},{ tag: `li`, babies: [{ tag: `a`,
              innerText: `my github page for computer people`,
              href: `https://github.com/tombetthauser`
            }]},{ tag: `li`, babies: [{ tag: `a`,
              innerText: `my instagram which I hate and barely use`,
              href: `https://www.instagram.com/tombetthauser/`
            }]},{ tag: `li`, babies: [{ tag: `a`,
              innerText: `my random bandcamp page`,
              href: `https://tombetthauser.bandcamp.com/`
            }]},{ tag: `li`, babies: [{ tag: `a`,
            //   innerText: `my art merch shop for buying stuff`,
            //   href: `https://www.etsy.com/shop/tombetthauser`
            // }]},{ tag: `li`, babies: [{ tag: `a`,
              innerText: `my linkedin page for whatever`,
              href: `https://www.linkedin.com/in/tombetthauser/`
            }]}]
    },{ tag: `p`,
      innerText: `Some of my recent projects...`
    },{ tag: `ul`,
      babies: [{ tag: `li`, babies: [{ tag: `a`,
              innerText: `state of the arts survey data project`,
              href: `http://www.sotasurvey.org/2019`
            }]},{ tag: `li`, babies: [{ tag: `a`,
              innerText: `unknowable symbols web meditations`,
              href: `http://unknowablesymbols.com`
            }]},{ tag: `li`, babies: [{ tag: `a`,
              innerText: `hypernormalisation ipsum generator`,
              href: `https://tombetthauser.github.io/hypernormalisipsum/`
            }]},{ tag: `li`, babies: [{ tag: `a`,
              innerText: `tomblr social media clone`,
              href: `http://tomblr.herokuapp.com/`
            }]},{ tag: `li`, babies: [{ tag: `a`,
              innerText: `more on my github`,
              href: `https://github.com/tombetthauser`
            }]}]
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