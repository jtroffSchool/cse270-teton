// This sets today's date in the header
let now = new Date()
let fulldate = new Intl.DateTimeFormat("en-US", { dateStyle: "medium", timeStyle: "short" }).format(  );

document.querySelector(".header-today p").textContent = fulldate;

// Toggle the menu open or closed
function toggleMenu(){
        document.querySelector("nav ul").classList.toggle("menu-active");
        document.querySelector("#hamburger-x").classList.toggle("menu-active");
        document.querySelector("#hamburger-equiv").classList.toggle("menu-active");
}

// Attach click listener to the hamburger menu
document.querySelector("#hamburger-menu").addEventListener('click', toggleMenu);    
