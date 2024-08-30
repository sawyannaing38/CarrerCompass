import { showTypingEffect } from "./common.js";

// Selecting element
const heading = document.querySelector(".heading");
const form = document.querySelector("form");
const inputElements = document.querySelectorAll("input");
const textAreas = document.querySelectorAll("textarea");

const texts = "Explore The best Employees";

setTimeout(() => {
    form.style.opacity = "1";
}, 400);


showTypingEffect(heading, texts);

// Adding focus event
inputElements.forEach(function(inputElement) {
   showAnimation(inputElement);
})

textAreas.forEach(function(textArea) {
    showAnimation(textArea);

    textArea.addEventListener("keyup", function(event)
    {
        if (event.key == "Enter")
        {
            this.rows += 1;
        }

        if (!this.value)
        {
            this.rows = 2;
        }
    })
})

// Function showAnimation
function showAnimation(obj)
{
    // Get its parent element
    const parent = obj.parentElement;

    obj.addEventListener("input", function() 
    {
        if (!obj.value)
        {
            parent.style.setProperty("--after-width", "0%");
        }
        else
        {
            parent.style.setProperty("--after-width", "100%");
        }
        
    })

}

// Validate form
form.addEventListener("submit", function(event) {
    event.preventDefault();

    let isValid = true;

    if (!document.querySelector("#position").value)
    {
        document.querySelector(".position-error").textContent = "Missing Position";
        isValid = false;
    }

    if (!document.querySelector("#salary").value)
    {
        document.querySelector(".salary-eror").textContent = "Missing Salary";
        isValid = false;
    }

    if (!document.querySelector("#location").value)
    {
        document.querySelector(".location-error").textContent = "Missing Location";
        isValid = false;
    }

    if (!document.querySelector("#workingTime").value)
    {
        document.querySelector(".workingTime-error").textContent = "Missing Working Time";
        isValid = false;
    }

    if (!document.querySelector("#description").value)
    {
        document.querySelector(".description-error").textContent = "Missing Description";
        isValid = false;
    }
    
    if (!document.querySelector("#requirement").value)
    {
        document.querySelector(".requirement-error").textContent = "Missing Requirement";
        isValid = false;
    }

    if (!document.querySelector("#benefit").value)
    {
        document.querySelector(".benefit-error").textContent = "Missing Benefit";
        isValid = false;
    }

    if (!document.querySelector("#field").value)
    {
        document.querySelector(".field-error").textContent = "Missing Field";
        isValid = false;
    }

    // Check salary is valid or not
    if (document.querySelector("#salary").value)
    {
        let salary = Number(document.querySelector("#salary").value);

        if (!salary)
        {
            document.querySelector(".salary-error").textContent = "Invalid Salary";
            isValid = false;
        }
    }

    if (document.querySelector("#workingTime").value)
    {
        let workingTime = Number(document.querySelector("#workingTime").value)

        if (!workingTime)
        {
            document.querySelector(".workingTime-error").textContent = "Invalid Working Time";
            isValid = false;
        }
    }

    if (isValid)
    {
        form.submit();
    }
})