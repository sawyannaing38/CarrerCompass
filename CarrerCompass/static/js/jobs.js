import {toggleShow} from "./common.js"

// DOM SELECTING
const jobs = document.querySelectorAll(".job");
const location = document.querySelector("#location");
const field = document.querySelector("#type");
const fieldLists = document.querySelectorAll(".fieldlist");

// Showing all the visible jobs
document.addEventListener("DOMContentLoaded", function()
{
    jobs.forEach(function(job)
    {
        toggleShow(job);
    })
})

// Showing and hide when scrolling
document.addEventListener("scroll", function()
{
    jobs.forEach(function(job)
    {
        toggleShow(job);
    })
})

// Add input event on field
field.addEventListener("input", function() 
{
    // Getting field value and location value
    // Get the input value of both field and locatoion
    const fieldValue = field.value.toLowerCase();
    const locationValue = location.value.toLowerCase();

    filter(fieldValue, locationValue);
})

// Add input event on location
location.addEventListener("input", function()
{
    // Getting field value and location value
    // Get the input value of both field and locatoion
    const fieldValue = field.value.toLowerCase();
    const locationValue = location.value.toLowerCase();

    filter(fieldValue, locationValue);
})

fieldLists.forEach(function(fieldList)
{
    fieldList.addEventListener("click", function()
    {
        field.value = this.textContent;
        
        filter(this.textContent.toLowerCase());
    })
})
// Function for filtering
function filter(fieldValue="", locationValue="")
{
    if (!fieldValue && !locationValue)
    {
        // Show all the available jobs
        jobs.forEach(function(job)
        {
            job.style.display = "block";
        })
    }

    else 
    {
        jobs.forEach(function(job)
        {
            // Getting location and field
            const jobLocation = job.querySelector(".location").textContent.toLowerCase();
            const jobField = job.querySelector(".field").textContent.toLowerCase();

            // If both fieldValue and location ValueExists
            if (fieldValue && locationValue)
            {
                // Show the job if fielvalue match jobfield and locationvalue match joblocation
                if ((jobField.includes(fieldValue)) && (jobLocation.includes(locationValue)))
                {
                    job.style.display = "block";
                }

                else 
                {
                    job.style.display = "none";
                }
            }

            // If only fieldValue exist
            else if (fieldValue)
            {
                if (jobField.includes(fieldValue))
                {
                    job.style.display = "block";
                }

                else 
                {
                    job.style.display = "none";
                }
            }

            // if only location value exist
            else 
            {
                if (jobLocation.includes(locationValue))
                {
                    job.style.display = "block";
                }

                else 
                {
                    job.style.display = "none";
                }
            }
        })

    }
}