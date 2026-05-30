const images = [
{
url: "/static/gallery/image1.jpg",
title: "Mountain Landscape"
},
{
url: "/static/gallery/image2.jpg",
title: "Beach"
},
{
url: "/static/gallery/image3.jpg",
title: "Forest Path"
},
{
url: "/static/gallery/image4.png",
title: "Waterfall"
},
{
url: "/static/gallery/image5.png",
title: "Desert"
},
];

let currentIndex = 0;

const imageElement = document.getElementById("galleryImage");
const titleElement = document.getElementById("imageTitle");

function showImage() {
    imageElement.src = images[currentIndex].url;
    titleElement.textContent = images[currentIndex].title;
}

function nextImage() {
    currentIndex++;

    if (currentIndex >= images.length) {
        currentIndex = 0;
    }

    showImage();
}

function previousImage() {
    currentIndex--;

    if (currentIndex < 0) {
        currentIndex = images.length - 1;
    }

    showImage();
}

showImage();