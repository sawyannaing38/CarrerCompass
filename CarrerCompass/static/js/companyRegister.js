const information = document.querySelector(".information");
const image = document.querySelector(".image");

const form = document.querySelector("form");
const errorMessage = document.querySelector("#error")

setTimeout(() => {
    information.style.transform = "translateX(0px)";
    image.style.transform = "translateX(0px)";
}, 10)

// Add submit event
form.addEventListener("submit", function(event)
{
    event.preventDefault();

    // Check each field is empty or not
    // If empty (warn the user)
    // check file extension is jpg jpeg or png
    // check password between 6 and 8 character, at least one uppercase, one number and one special character
    // check password == confirm

})