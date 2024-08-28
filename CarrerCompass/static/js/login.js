import { moveEffect } from "./common.js";

const form = document.querySelector("form");

moveEffect();

// Validating Form
form.addEventListener("submit", function(event) {

    event.preventDefault();

    let isValid = true;

    if (!document.querySelector("#username").value)
    {
        document.querySelector(".name-error").textContent = "Missing Username";
        isValid = false;
    }

    if (!document.querySelector("#password").value)
    {
        document.querySelector(".password-error").textContent = "Missing Password";
        isValid = false;
    }

    if (isValid)
    {
        form.submit();
    }

})