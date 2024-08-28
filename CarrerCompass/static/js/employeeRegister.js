import { moveEffect, isValidPassword, isValidImage } from "./common.js";

const form = document.querySelector("form");

moveEffect();

// Validating form
form.addEventListener("click", function(event)
{
    event.preventDefault();

    // Check Empty value
    let isValid = true;

    if (!document.querySelector("#username").value)
    {
        document.querySelector(".username-error").textContent = "Missing Username";
        isValid = false;
    }

    if (!document.querySelector("#location").value)
    {
        document.querySelector(".location-error").textContent = "Missing Location";
        isValid  = false;
    }

    if (!document.querySelector("#email").value)
    {
        document.querySelector(".email-error").textContent = "Missing Email";
        isValid = false;
    }

    if (!document.querySelector("#age").value)
    {
        document.querySelector(".age-error").textContent = "Missing age";
        isValid = false;
    }

    if (!document.querySelector("#gender").value)
    {
        document.querySelector(".gender-error").textContent = "Missing Gender";
        isValid = false;
    }

    if (!document.querySelector("#eudcation").value)
    {
        document.querySelector(".eudcation-error").textContent = "Missing Education";
        isValid = false;
    }

    if (!document.querySelector("#experience").value)
    {
        document.querySelector(".experience-error").textContent = "Missing Experience";
        isValid = false;
    }

    if (!document.querySelector("#profession").value)
    {
        document.querySelector(".profession-error").textContent = "Missing Profession";
        isValid = false;
    }

    if (!document.querySelector("#currentCompany").value)
    {
        document.querySelector(".currentCompany-error").textContent = "Missing Current Company";
        isValid = false;
    }

    if (!document.querySelector("#image").value)
    {
        document.querySelector(".image-error").textContent = "Missing Image";
        isValid = false;
    }

    if (!document.querySelector("#password").value)
    {
        document.querySelector(".password-error").value = "Missing Password";
        isValid = false;
    }

    if (!document.querySelector("#confirm").value)
    {
        document.querySelector(".confirm-error").textContent = "Missing Confirm Password";
        isValid = false;
    }

    if (!document.querySelector("#skills").value)
    {
        document.querySelector(".skills-error").textContent = "Missing Skills";
        isValid = false;
    }

    if (!document.querySelector("#description").value)
    {
        document.querySelector(".description-error").textContent = "Missing Description";
        isValid = false;
    }

    // Check valid iamge or not
    if (!isValidImage(document.querySelector("#image").value))
    {
        document.querySelector(".image-error").textContent = "Invalid Image";
        isValid = false;
    }

    // Check valid password or not
    if (!isValidPassword(document.querySelector("#password").value))
    {
        document.querySelector(".password-error").textContent = "Invalid Password";
        isValid = false;
    }

    // Check same passwrod or not
    if (document.querySelector("#password").value !== document.querySelector("#confirm").value)
    {
        document.querySelector(".confirm-error").textContent = "Passwords do not match";
        isValid = false;
    }

    // Check valid age or not
    let age = document.querySelector("#age").value;

    age = Number(age);

    if (!age)
    {
        document.querySelector(".age-error").textContent = "Invalid Age";
        isValid = false;
    }

    else
    {
        if (age < 13)
        {
            document.querySelector(".age-error").textContent = "Invalid Age";
            isValid = false;
        }
    }

    if (isValid)
    {
        form.submit();
    }

})