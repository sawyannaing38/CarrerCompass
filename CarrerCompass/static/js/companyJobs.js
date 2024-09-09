import { toggleShow } from "./common.js";

const fieldInput = document.querySelector("#field");
const locationInput = document.querySelector("#location");
const jobs = document.querySelectorAll(".job");

document.addEventListener("DOMContentLoaded", function()
{
    toggleShow(fieldInput);
    toggleShow(locationInput);
    
    jobs.forEach(function(job)
    {
        toggleShow(job);
    })
})

document.addEventListener("scroll", function()
{
    toggleShow(fieldInput);
    toggleShow(locationInput);
    
    jobs.forEach(function(job)
    {
        toggleShow(job);
    })
})

fieldInput.addEventListener("input", function()
{
    const fieldValue = fieldInput.value.toLowerCase();
    const locationValue = locationInput.value.toLowerCase();

    jobs.forEach(function(job)
    {   
        // Getting filed and location
        const location = job.querySelector(".location").textContent.toLowerCase();
        const field = job.querySelector(".job-field").textContent.toLowerCase();

        if (fieldInput && locationValue)
        {
            if (location.includes(locationValue) && field.includes(fieldValue))
            {
                job.style.display = "flex";
                job.classList.add("show");
            }

            else 
            {
                job.style.display = "none";
            }
        }
    
        else if (fieldValue)
        {

            console.log(field.includes(fieldValue));
            if (field.includes(fieldValue))
            {
                job.style.display = "flex";
                job.classList.add("show");
            }

            else 
            {
                job.style.display = "none";
            }
        }
    
        else if (locationValue)
        {
            if (location.includes(locationValue))
            {
                job.style.display = "flex";
                job.classList.add("show");
            }

            else 
            {
                job.style.display = "none";
            }
        }
    
        else 
        {
            job.style.display = "flex";
            job.classList.add("show");
        }
    })
})

locationInput.addEventListener("input", function()
{
    const fieldValue = fieldInput.value.toLowerCase();
    const locationValue = locationInput.value.toLowerCase();

    jobs.forEach(function(job)
    {   
        // Getting filed and location
        const location = job.querySelector(".location").textContent.toLowerCase();
        const field = job.querySelector(".job-field").textContent.toLowerCase();

        if (fieldInput && locationValue)
        {
            if (location.includes(locationValue) && field.includes(fieldValue))
            {
                job.style.display = "flex";
                job.classList.add("show");
            }

            else 
            {
                job.style.display = "none";
            }
        }
    
        else if (fieldValue)
        {

            console.log(field.includes(fieldValue));
            if (field.includes(fieldValue))
            {
                job.style.display = "flex";
                job.classList.add("show");
            }

            else 
            {
                job.style.display = "none";
            }
        }
    
        else if (locationValue)
        {
            if (location.includes(locationValue))
            {
                job.style.display = "flex";
                job.classList.add("show");
            }

            else 
            {
                job.style.display = "none";
            }
        }
    
        else 
        {
            job.style.display = "flex";
            job.classList.add("show");
        }
    })
})