var displayNames = true;
var randomAnimationNumber = (Math.round(Math.random()*1)+1);

var artist = {
	name: {
		first: 'Tom',
		last: 'Betthauser'
	},
	work: [
		'<a target="_blank" href="https://tombetthauser.github.io/anchorage-museum/">Deep Sleep / Meditation Aid, Project for Anchorage Museum Performance, ES5 Script by Tom Betthauser, Images Collected with Thomas Chung, 2018 (project link)</a>',
		'<a target="_blank" href="https://tombetthauser.github.io/anchorage-museum/">Audio Performance / Digital Installation for Anchorage Museum, Thomas Chung & Tom Betthauser, 2018  (digital installation link)</a>',
		'Daruma Silhouettes / Ikea Garden, oil & acrylic on poplar, 5 x 6 in. 2018',
		'Blue Screen / Mountain Man, oil on poplar, 5 x 6.5 in. 2018',
		'Atman Netsuke, original for concrete cast, 2 x 2 in. 2018',
		'Atman Netsuke, original for concrete cast, 2 x 3 in. 2018',
		'<a target="_blank" href="https://tombetthauser.github.io/numbers/">Meditation Aid / Web Project, ES5 Script / Painting / Audio by Tom Betthauser, 2018 (project link)</a>',
		'Bay Head (Study for Large-Scale / 6 ft. Drawing), graphite on paper, 8.5 x 11 in. 2018',
		'Los Angeles / Samsara Heads, graphite on paper, graphite on paper, 6 x 9 in. 2017 / 18',
		'New App Ideas / Marin Headlands (Study), oil on panel, 6 x 6 in. 2018',
		'Eyes on Mars, photocopy of graphite original / artist\'s frame, 8.5 x 11 in. 2018',
		'Blue Screen / Daruma Grid, oil on poplar, 4.5 x 6 in. 2018',
		'Digital Loop (stills) for Installation at SFAI 3rd Street Studios, 2017',
		'Sukkah Mixed Media Installation (Exterior) at SFAI 3rd Street Studios, 2017',
		'Sukkah Audio / Digital Video Installation (Interior) at SFAI 3rd Street Studios, 2017',
		'Artist\'s Book Designed / Bound by Artist for SFAI 3rd Street Resident Artists, 2017',
		'Artist\'s Book Designed / Bound by Artist for SFAI 3rd Street Resident Artists, 2017',
		'Detail from In-Progress Lions of Judah Diptych (Large-Scale / 5 ft.), 2017',
		'Kern County Desert / Note Drawings, 3 x 3 in. (individually) 2017',
		'Kern County Desert / Note Drawings, 3 x 3 in. (individually) 2017',
		'Artist\'s Book Collaboration / Erin Kaczkowski for Exhibition at Ms. Barber\'s (LA), 2017',
		'Artist\'s Book Collaboration / Erin Kaczkowski for Exhibition at Ms. Barber\'s (LA), 2017',
		'Planet Study, acrylic on panel, 3 x 4.5 in. 2015 / 16',
		'Daruma Grid, graphite on office-paper, 5 x 7 in. 2016',
		'Bakersfield Office Installation, graphite / artist\'s frame / found material, 2016',
		'<a target="_blank" href="https://drive.google.com/file/d/0B0i92gIfB6BKcDNBLXBqSHRkaUk/view">VD03-FA16, all models / textures / sound produced by artist in collaboration Bret Ward, 2016 (video link)</a>',
		'Installation shot, San Francisco Art Institute, 3rd St. Studio Fellowship (program link), 2016',
		'Cleric_0.2[cast1], 4"x 5" concrete cast of original sculpture / hand-woven mat, 2016',
		'Cleric(s)_0.2, 4"x 5" concrete cast & original sculpture (left) / hand-woven mats, 2016',
		'Sketchbook selection (1 of 50), 8.5"x11" inkjet print scanned from ballpoint sketch, 2016',
		'Sketchbook selection (1 of 50), 8.5"x11" inkjet print scanned from ballpoint sketch, 2016',
		'157s.Cat_1[study], 4"x 5" watercolor / paper, 2016',
		'MIRc.4.5bya[study], 4"x 5" watercolor / gouache / paper, 2016',
		'Exhibition shot, Anchorage (AK), framed watercolors / sketchbook prints / digital video projection, 2016',
		'Vaab_LITE[study]-SM16, 5"x 4" watercolor / paper, 2016',
		'BK01-SM16 (book of drawings), 4.25"x 5.5" published in Oakland CA, 2016.',
		'Group exhibition curated by Christopher Ford, CB1 Gallery, Los Angeles, 2016 (exhibition link)',
		'KEEN-SP16, 7"x 7.25" oil / poplar, 2015/16',
		'ALEO-1314 (Bird in Space), 6"x 6.5" oil / acrylic / birch ply, 2014',
		'DIOT-FA15, 7.75"x 7.5"  oil / poplar panel, 2015',
		'HION-1314, 5.75"x 4.5" oil / birch panel, 2014',
		'Group exhibition curated by Brett Reichman, CB1 Gallery, Los Angeles, 2016 (exhibition link)',
		'GTS1-SP16 (Gates), 45"x 77"  graphite / paper, 2015/16',
		'AMR1-1314 (Amar I), 12"x 19" graphite / paper, 2014',
		'AMR2-1314 (Amar II), 12"x 19" graphite / paper, 2014',
		'Rkm2-SP15 (Stones II), 9"x 11"  graphite / mixed media frame, 2015',
		'SRF1-SP15 (Surface), 7"x 8.5"  graphite / paper, 2015',
		'CLER-SP15 (Cleric), 7"x 7.5"  graphite / paper, 2015',
		'Rkm1-FA15 (Stones I), 15""x 19"  watercolor / corkboard, 2015',
		'Solo exhibition / installation (exterior), LRC Gallery, Ridgecrest CA, 2014/15',
		'Solo exhibition / installation (interior), LRC Gallery, Ridgecrest CA, 2014/15',
		'BSTR-1314 (Natura), 6"x 6"  acrylic / oil / canvas, 2014',
		'AMAN-1314, 6"x 7" oil / birch ply, 2014',
		'BRUG-1314 (Cambria), 6"x 7" oil / birch ply, 2014',
		'MAP1-1314, 6"x 5" oil / canvas, 2014',
		'MEC1-1314, 6"x 7" oil / canvas, 2014',
		'SALM-1314, 4"x 5.5" oil / canvas, 2014',
		'BERK-1314, 6"x 5" oil / birch ply, 2014',
		'CONA-1314 (Conan), 6"x 6" oil / canvas, 2014',
		'MIM1-SP12 (Mimoid Diptych I), 70"x 48"graphite / paper, 2012',
		'MIM1-SP12 (Mimoid Diptych II), 70"x 48"graphite / paper, 2012',
		'LND2-SP12 (Land), 78"x 48" graphite / paper, 2011/12',
		'Group exhibition, Green Gallery, Yale School of Art, 2012 (sculptures by Joyce Kalema)',
		'Group exhibition, Green Gallery, Yale School of Art, 2012 (sculpture by Joyce Kalema)',
		'ISL1-FA11, 32"x 16" graphite / paper, 2011',
		'WAL1-FA11, 24"x 19" graphite / paper, 2011',
		'EGPT-SP11, 24"x 19" graphite / paper, 2011',
		'ISL2-FA11, 24"x 19" graphite / paper, 2011',
		'LND1-SP10, 72"x 48" graphite / stretched paper, 2010/11',
		'SATV-SM09, 24"x 19" graphite / paper, 2010',
		'OBSR-SM09, 24"x 19" graphite / paper, 2010',
		'TEMP-SM10, 24"x 19" graphite / paper, 2010',
		'PURP-FA08, 12"x 9" acrylic / masonite, 2008',
		'CRSH-SM08, 15"x 19" acrylic / masonite, 2008',
		'OREG-WB07, 12"x 19" acrylic / masonite, 2007',
		'SF01-FA07, 12"x 10" acrylic / birch ply, 2007',
		'STV1-FA08 (Steve), 6"x 5.5" acrylic / panel, 2008',
		'SFLT-FA08 (Daly City), 4"x 5" acrylic / panel, 2008',
		'MRK2-FA08 (Mark), 6"x 5" acrylic / panel, 2008'
	],
	cv: [
		"<h5>CONTACT:</h5>",
		"tombetthauser@gmail.com",
		"<h5>EDUCATION:</h5>",
		"Yale University - Master of Fine Arts, 2012",
		"San Francisco Art Institute - Bachelor of Fine Arts, 2010",
		"<h5>TEACHING EXPERIENCE:</h5>",
		"College of Marin, CA - Adjunct Professor, Beginning & Advanced Painting, May 2018 - Present",
		"West Valley College, San Jose CA - Adjunct Professor, Studio Art / Art History, 2017 - Present",
		"University of California San Diego CA - Visiting Artist (lecture / studio visits) - Nov 2017",
		"Wylie & May Louise Jones Gallery, Bakersfield CA - Chief Gallery Director / Curator, 2014 - 2017",
		"Bakersfield College, CA - Adjunct Professor, Studio Art / Art History, 2014 - 2017",
		"Cerro Coso Community College, CA - Adjunct Prof. Studio Art / Art History, 2013 - 2017",
		"Artvoices Magazine, Los Angeles CA - Contributing Writer, 2014 - 2016",
		"San Francisco Art Institute, CA - Teaching Assistant, 2007 - 2010",
		"Exploratorium Museum, CA - Explainer / Tactile Dome / Public Programs, 2006 - 2012",
		"<h5>SELECTED GROUP / SOLO EXHIBITIONS:</h5>",

		"2015​ - PRESENT",
		"<br>",
		"Crocker Museum of Art, CA - Big Names Small Art Benefit Auction - May 2018",
		"WVC Art Gallery, CA - Invitational Faculty Exhibition - Jan 2018",
		"Diego Rivera Gallery, San Francisco CA - SFAI 2017 Alumni Exhibition - Nov 2017",
		"San Francisco Art Institute, CA - Installation produced for 3rd Street Open Studios - Apr 2017",
		"Becky’s Space, Anchorage AK - That’s Not God (with Tom Chung) - Feb 2017",
		"San Francisco Art Institute, CA - Installation Produced for Residency Open Studios - Dec 2017",
		"CB1 Gallery, Los Angeles, CA - New Haven Group Exhibition - Jul 2016",
		"CB1 Gallery, Los Angeles, CA - Labor Intensive Drawing (Curated by Brett Reichman) - Feb 2016",
		"Rema Hort Mann Foundation, New York, NY - Buy What You Love Benefit Auction - Dec 2015",
		"Wylie & May Louise Jones Gallery, CA - 2015 Arts Faculty Show - Oct / Nov 2015",
		"<br>",

		"2010​ - 2015",
		"<br>",
		"LRC Gallery, Ridgecrest CA - Dolman Solo Exhibition / Installation - Oct / Nov 2014",
		"Giuseppe Group Sculpture Park, Mojave CA - Permanent Sculptural Installation - Apr 2014",
		"Mark’s Garage Gallery, Honolulu HI - Hi Tides Group Exhibition - Aug 2013",
		"Water McBeer Gallery, San Francisco CA - Prop-Painting Solo Exhibition - Jul 2013",
		"Gallaria Yusto-Giner, Malaga Spain - Works on Paper Group Exhibition - Sep 2012",
		"FFDG, San Francisco CA - Cigarettes, Phone Cards and Hip Hop Clothing - May 2012",
		"Green Gallery, New Haven CT - Thesis Exhibition with Joyce Kalema - Feb 2012",
		"Green Gallery, New Haven CT - 2nd Year MFA Group Exhibition - Sep 2011",
		"Exploratorium, San Francisco CA - Tactile Geometry Commissioned Mural - Mar 2011",
		"<br>",

		"2005​ - 2010",
		"<br>",
		"Green Gallery, New Haven CT - 1st Year MFA Group Exhibition - Nov 2010",
		"Exploratorium, San Francisco CA - Tactile Representation Commissioned Mural - Jul 2010",
		"San Francisco Art Institute, San Francisco CA - BFA Graduating Exhibition - May 2010",
		"Peanut Gallery, San Francisco CA - When Worlds Collide Group Exhibition - Jan 2010",
		"Kipling Pop-Up Gallery, San Francisco CA - Mini-Residency Group Exhibition - Oct 2009",
		"Live Worms Gallery, San Francisco CA - SFAI Group Exhibition - Jan 2009",
		"The Pheonix, Petaluma CA - Urban Alcove Volunteer Mural - Dec 2008",
		"Live Worms Gallery, San Francisco CA - Singles Night Group Exhibition - Aug 2008",
		"Ar+Space Gallery, San Francisco CA - Living the Dream Group Exhibition - Jan 2008",
		"Luggage Store Gallery, San Francisco CA - SFAI Group Exhibition - Feb 2007",
		"Miller Art & Frame, Mill Valley CA - Salon Group Exhibition Curated by Mark Aubert - May 2006",


		"<h5>SELECTED PRINT / ONLINE PUBLICATIONS:</h5>",

		"93505 Books, Oakland CA - 3rd Street Studios Residency Program Catalogue - Sep 2017",
		"93505 Books, Oakland CA - Small Edition Artist’s Book of Drawings - Sep 2015",
		"FFDC Blog - Exhibition Review, Tom Betthauser at Water Mcbeer - Aug 2013",
		"Pacolli Pacolli Blog - Exhibition Review, Cigarettes Phone Cards & Clothing - Apr 2012",
		"Drawn Blog - Featured Artist Tom Betthauser by David Huyck - Nov 2011",
		"Lost at E Minor Blog - Tom Betthauser’s Detailed Graphite Drawings by Gerry Mak - Nov 2011",
		"IHLET Blog - Tom Betthauser’s Contemporary Architectural Sketches / Urban Art - Nov 2011",
		"Espen Art Blog - Amazingly Detailed Pencil Drawings From Tom Betthauser - Nov. 2011",
		"FFDC Blog - Tom Betthauser Mini Interview - Oct 2011",
		"We Love Art and Design Blog - Featured Artist Tom Betthauser - Oct 2011",
		"New American Paintings Issue #93 - Juried MFA Annual Issue - Apr 2011",
		"Scrapbook Blog - Tom Betthauser, Artist San Francisco - Mar 2010",
		"Design Milk Blog - Featured Artist Tom Betthauser by Warren King - Feb 2010",
		"Jaz Jaz Art Blog - The Stunning Art of Tom Betthauser by Warren King - Jan 2010",
		"Art Business Online - Ar+Space: Living The Dream by Alan Bamburger - May 2008",


		"<h5>HONORS / AWARDS:</h5>",

		"San Francisco Art Institute, CA - 3rd Street Studios Residency Program, Sep 2016 - Aug 2017",
		"LRC Gallery, Ridgecrest CA - Visiting Artist / Lecturer - Oct / Nov 2014",
		"Robert Schoelkopf Memorial Traveling Fellowship (Yale School of Art) - 2011",
		"Exploratorium, CA - Visiting / Commissioned Muralist, Mar 2011",
		"Exploratorium, CA - Visiting / Commissioned Muralist, May 2010",
		"SFAI Juried Honors Studio Awarded Sep 2009 - May 2010",
		"Myasnikov Materials Grant - San Francisco CA, 2009 - 2010",
		"SFAI Juried Honors Studio Awarded Sep 2008 - May 2009",
		"SFAI Juried Wall-Space Awarded Sep 2007 - May 2008",


		"<h5>PORTFOLIO LINKS / WEB DEVELOPMENT PROJECTS:</h5>",

		"Recent Visual Work / Portfolio: www.TomBetthauser.com / portfolio",
		"Examples of Student Work: www.TomBetthauser.com / studentwork",
		"Ongoing Student Resource Web Portal: www.TomBetthauser.com / resources",
		"Non-Profit Artist Web Page Builder / Resource Portal: www.TomBetthauser.com / artpages",


		"<h5>CURATORIAL EXPERIENCE:</h5>",

		"Wylie & May Louise Jones Gallery, Bakersfield College CA - Chief Director / Curator, 2014 - 2017",
		"<br>",
		"Forms in Decay - Solo Exhibition and Guest Lecture by Artist Daniel Herwitt - Mar / Apr 2017",
		"New Works - Exhibition of Student Work, Guest Curator Daniel Herwitt (NYC) - Jan / Feb 2017 *",
		"Panorama Exhibition - Annual Juried Exhibition of New Work by Young Artists - Nov / Dec 2016 2016 / 17",
		"Faculty Exhibition - New Works by KCCD Arts Faculty - Sep / Oct 2016",
		"<br>",
		"New Works - New Student Work, Guest Curator Kyle Coniglio (Montclare Univ.) - Apr / May 2016",
		"CalArts Recent MFA Group Exhibition - Organized with artist Michael Richards - Feb / Mar 2016",
		"It’s Bright in Hell - Installation / Lecture by Artist / Publisher Robey Clark (LA) - Dec / Jan 2016 *",
		"Panorama Exhibition - Annual Juried Exhibition of New Work by Young Artists - Nov 2015",
		"2015 / 16 Faculty Exhibition - New Works by KCCD Arts Faculty - Sep / Oct 2015",
		"<br>",
		"Panorama Exhibition - Annual Juried Exhibition of New Work by Young Artists - Apr / May 2015",
		"Drapetomania - Large-Scale Installation / Lecture by Tom Chung (Univ. of Alaska) - Mar 2015 *",
		"New Works - Student Show, Guest Curator / Lecturer Ivan Bridges (Los Angeles) - Feb 2015 * 2014 / 15",
		"Faculty Exhibition - New Works by KCCD Arts Faculty - Jan 2015",
		"<br>",
		"Greys Pinks & Blues - Works by Roni Shneior & Erin Kaczkowski (Los Angeles) - Dec 2014",
		"Who Sees the Past - Works by Kiki Johnson & Dustin Metz (Los Angeles) - Nov 2014",
		"The Next Level - Exhibition & Guest Lecture by Artists Ivan Bridges & Thack Olsen - Oct 2014",
		"Digital Works - Works by Digital Artist Tom Lundquist (Santa Monica College) - Sep 2014",
		"<br>",
		"* Visiting Artist Lecture Program Independently Proposed / Initiated Feb 2015",


		"<h5>WRITING EXPERIENCE:</h5>",

		"Anchorage Museum - Wall Text for Solo Exhibition by Artist Tom Chung (Univ. of Alaska) - Sep 2018",
		"<br>",
		"3rd Street Studios Residency, Independent Catalogue - Chief Editor / Print Coordinator - Sep 2017",
		"Critical Introduction for Artist Daniel Herwitt Exhibition & Lecture - Jones Gallery, Mar 2017",
		"Catalogue for Exhibition by Erin Kaczkowski - Chief Editor / Print Coordinator - Feb 2017",
		"Reflection on New Student Work Exhibition, Curator Daniel Herwitt - Jones Gallery, Jan 2017",
		"<br>",
		"Brief History / Introduction for Panorama Student Work Exhibition - Jones Gallery, Nov 2016",
		"Background Information for New Works by Arts Faculty Exhibition - Jones Gallery, Sep 2016",
		"Introduction for Student Exhibition Guest Curator Kyle Coniglio - Jones Gallery, Apr 2016",
		"Context / Introduction for CalArts Recent MFA Group Exhibition - Jones Gallery, Feb 2016",
		"Introduction for Exhibition / Lecture by Artist / Publisher Robey Clark (LA) - Dec 2016",
		"Brief History / Introduction for Panorama Student Work Exhibition - Jones Gallery, Nov 2016",
		"Introduction for New Faculty / KCCD Arts Faculty Exhibition - Jones Gallery, Sep 2016",
		"<br>",
		"Art Voices Magazine, Los Angeles CA - Feature Article on Artist Peter Stanick - May 2015",
		"Brief Introduction for Historic Panorama Student Work Exhibition - Jones Gallery, May 2015",
		"Critical Introduction for Artist Tom Chung Exhibition & Lecture - Jones Gallery, Mar 2015",
		"Introduction for Visiting Artist / Lecturer Ivan Bridges, - Jones Gallery, Feb 2015",
		"Visual Break Down of Arts Faculty Exhibition - Jones Gallery, Jan 2015",
		"<br>",
		"Introduction to Works / Exhibition by Roni Shneior & Erin Kaczkowski - Jones Gallery, Dec 2014",
		"Critical Introduction for Artists Kiki Johnson & Dustin Metz - Jones Gallery, Nov 2014",
		"Introduction to Exhibition by Artists Ivan Bridges & Thack Olsen - Jones Gallery, Oct 2014",
		"Background Information / Context for Visiting Artist Tom Lundquist - Jones Gallery, Sep 2014",
		"Art Voices Magazine, Los Angeles CA - Feature Article on Artist Karen Fitzgerald - Sep 2014"
	]
}


// script -


loadNavbar();
loadImages();
loadTitle();
loadCV();


// functions -


function loadTitle() {
	$("head").prepend(
  		'<title>' + artist.name.first + ' ' + artist.name.last + '</title>'
	)
}

function loadNavbar() {
	$("body").prepend(
	  	'<nav class="t-nav2-container navbar navbar-default hidden-lg hidden-md hidden-sm">'
		+  '<div class="container-fluid" id="t-navbar-white">'
		+    '<div class="navbar-header">'
		+      '<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">'
		+         '<span class="sr-only">Toggle navigation</span>'
		+         '<span class="icon-bar"></span>'
		+         '<span class="icon-bar"></span>'
		+         '<span class="icon-bar"></span>'
		+       '</button>'
		+       '<a class="navbar-brand container" href="../../index.html">' + artist.name.first + ' ' + artist.name.last + '</a>'
		+     '</div>'
		+     '<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">'
		+       '<ul class="nav navbar-nav navbar-right">'
		// +       	'<li><a href="../../index.html" id="t-nav-link-mobile">&nbsp; home</a></li>'
		// +      		'<li><a href="images.html" id="t-nav-link-mobile">&nbsp; images</a></li>'
		+      		'<li><a target="_blank" href="https://tombetthauser.bandcamp.com/">&nbsp; sound</a></li>'
		+			'<li><a target="_blank" href="https://www.instagram.com/tombetthauser/">&nbsp; instagram</a></li>'
		+			'<li><a target="_blank" href="https://github.com/tombetthauser">&nbsp; github</a></li>'
		+			'<li><a target="_blank" href="https://www.linkedin.com/in/tombetthauser/">&nbsp; linkedin</a></li>'
		+			'<li><a target="_blank" href="../../assets/pdfs/cv.pdf">&nbsp; info + cv</a></li>'


		+       '</ul>'
		+     '</div>'
		+   '</div>'
		+ '</nav>'
	)
}

function loadImages() {
	for(i = artist.work.length; i > 0 ; i--){
		  $("#container").append(
				"<div class='animation" + randomAnimationNumber + "'><a target='new' href='../../assets/images/portfolio/full/"
				+ (i)
				+ ".jpg'><img src='../../assets/images/portfolio/thumb/"
				+ (i)
				+ ".jpg'></a></div>"
			)
	    if (displayNames === true) {
		  $("#container").append(
				"<p class='t-title-etc animation" + randomAnimationNumber + "'>"
				+ artist.work[artist.work.length-(i)]
				+ "</p>"
	  		)
		} else {
		  $("#container").append(
				"<br><br><br>"
 			)
	    }
	}
}

function loadCV() {
	for(i = artist.cv.length; i > 0 ; i--){
		$("#cvContainer").append(
			"<p class='cv-item'>"
			+ artist.cv[artist.cv.length-(i)]
			+ "</p>"
		)
	}
}