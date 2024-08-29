import { moveEffect, isValidPassword, isValidImage } from "./common.js";

const form = document.querySelector("form");

moveEffect();

form.addEventListener("submit", function(event) 
{
    event.preventDefault();

    // Validate user form
    let isValid = true;

    if (!document.querySelector("#companyName").value)
    {
        document.querySelector(".name-errror").textContent = "Missing Name";
        isValid = false;
    }

    if (!document.querySelector("#location").value)
    {
        document.querySelector(".location-error").textContent = "Missing Location";
        isValid = false;
    }

    if (!document.querySelector("#email").value)
    {
        document.querySelector(".email-error").textContent = "Missing Email";
        isValid = false;
    }

    if (!document.querySelector("#image").value)
    {
        document.querySelector(".image-error").textContent = "Missing Image";
        isValid = false;
    }

    if (!document.querySelector("#password").value)
    {
        document.querySelector(".password-error").textContent = "Missing Password";
        isValid = false;
    }

    if (!document.querySelector("#confirm").value)
    {
        document.querySelector(".confirm-error").textContent = "Missing Confirm Password";
        isValid = false;
    }

    if (!document.querySelector("#description").value)
    {
        document.querySelector(".description-error").textContent = "Missing Description";
        isValid = false;
    }

    // Check valid password or not
    if ((document.querySelector("#password").value) && (!isValidPassword(document.querySelector("#password").value)))
    {
        console.log(isValidPassword(document.querySelector("#password").value))
        document.querySelector(".password-error").textContent = "Invalid Password";
        isValid = false;
    }

    // Check same passwords 
    if (document.querySelector("#password").value !== document.querySelector("#confirm").value)
    {
        document.querySelector(".confirm-error").textContent = "Passwords do not match";
        isValid = false;
    }

    // Check valid image or not
    if (!isValidImage(document.querySelector("#image").value))
    {
        document.querySelector(".image-error").textContent = "Invalid Image";
        isValid = false;
    }

    if (isValid)
    {
        form.submit();
    }

})
