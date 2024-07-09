let submit = document.querySelector("#submit")
let title = document.querySelector("#title");
let image = document.querySelector("#image");
let short_desc = document.querySelector("#short_desc");
let description = document.querySelector("#description");

let blogs = document.querySelector(".blogs");
let body = document.querySelector("body");

let anc = document.querySelector(".anc");
let main=document.querySelector(".main")
let homeblg=document.querySelector(".HomeBlogs")

let blogBody=document.querySelector(".blogBody")
let homeBody=document.querySelector(".homeBody")



const imageWel = document.querySelector(".imgWelcome");
const screenWidth = window.innerWidth;

if (screenWidth < 768) {
  imageWel.src = 'welcomMob.jpeg';
} else {
  image.src = 'welcome2.jpeg';
}



Promise.all([
    new Promise(resolve => {
      
        for (i = 1; i <= localStorage.length; i++) {

        
            if (localStorage.getItem(i) != null) {
    
                let gD=JSON.parse(localStorage.getItem(i));
               console.log(gD)
    
            
               console.log(gD[1])
    
                let div = document.createElement("div");
                div.classList.add('blogCard');
                div.innerHTML = `<h2>${gD[0]}</h2>
                        <img src="${gD[1]}" alt="loadi">
            <p>${gD[2]}</p>`;
            
            blogs.prepend(div);
        }
        }
      resolve();
    }),
    new Promise(resolve => {

    
        let j=localStorage.length
        j=j-2
        for (i = 1; i <=3; i++) {

        
            if (localStorage.getItem(j) != null) {
               
                let gD=JSON.parse(localStorage.getItem(j));
               console.log(gD)
    
            
               console.log(gD[1])
    
                let div = document.createElement("div");
                div.classList.add('blogCard');
                div.innerHTML = `<h2>${gD[0]}</h2>
                        <img src="${gD[1]}" alt="loadi">
            <p>${gD[2]}</p>`;
            
            homeblg.prepend(div);
            j++
        }
        }      resolve();
    })
  ]).then(() => {
    console.log('Both functions have completed');
  });




submit.addEventListener("click", () => {
    console.log(title.value);
    console.log(image.value);
    console.log(short_desc.value);

    // const filePath = `${image.value}`;
    // const fileName = filePath.split("\\").pop();

    // console.log(fileName)
    const file = image.files[0];

    const imageUrl = URL.createObjectURL(file);
    console.log(imageUrl)

    let key1 = localStorage.length + 1;
    let titleData = title.value;
    let imageURL = imageUrl;
    let shortData = short_desc.value;
    let descriptData = description.value;
    console.log(descriptData)

    let arr = [titleData, imageURL, shortData, descriptData];
    localStorage.setItem(key1, JSON.stringify(arr));


    let div = document.createElement("div");
    div.classList.add('blogCard');
    div.innerHTML = `<h2>${titleData}</h2>
                <img src= ${imageUrl} alt="">
    <p>${shortData}</p>`;
    blogs.prepend(div);




})


