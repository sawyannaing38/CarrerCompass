import { toggleShow, getCookie } from "./common.js";

const closeBtns = document.querySelectorAll(".closeBtn");
const headings = document.querySelectorAll("h1");
const closeJobContainer = document.querySelector(".close-jobs");
const openJobContainer = document.querySelector(".open-jobs");

const closeJobs = closeJobContainer?.querySelectorAll(".job");
const openJobs = openJobContainer?.querySelectorAll(".job");


const windowHeight = window.innerHeight;

closeBtns.forEach(function(closeBtn) {
    closeBtn.addEventListener("click", function() {
        // Show Confirm Box

        // Getting Confirm Box
        const confirmBox = closeBtn.parentElement.parentElement.nextElementSibling;

        confirmBox.style.display = "flex";

        // Making Change According to user Choice
        closeJob(confirmBox.firstElementChild.children[1].firstElementChild, confirmBox.firstElementChild.children[1].children[1], confirmBox)
    })
})

// Function for makeing changes according to user choice
function closeJob(yes, no, obj)
{   
    yes.addEventListener("click", async function() {
        const id = Number(this.dataset.id);
        const url = `http://127.0.0.1:8000/api/closeJob/${id}`;
        const data = {
            "type" : "close"
        }

        // Try to fetch
        try 
        {
            let response = await fetch(url, 
                {
                    "method" : "PATCH",
                    "headers" : 
                    {
                        "Content-Type": "application/json",
                        "X-CSRFToken": getCookie("csrftoken")
                    },
                    "body" : JSON.stringify(data)
                }
            );

            if (response.ok)
            {
                // Remove the job from open container
                const job = obj.previousElementSibling;

                // Remove close btn from the job
                job.querySelector(".closeBtn").remove();

                // Add the job to the close container
                closeJobContainer.insertBefore(job, closeJobContainer.firstChild);

                toggleVisible(headings, openJobs, closeJobs);

                // Remove the confirmBox
                obj.remove();

                // Check the openJob container is empty now
                if (openJobContainer.childElementCount === 0)
                {
                    // Hide the title
                    headings[0].style.display = "none";
                }
            }


        }

        catch(error)
        {
            console.log(error);
        }

        // Hide ojb
        obj.style.display = "none";
    })

    no.addEventListener("click", function() {
        obj.style.display = "none";
    })
}

// Adding show class at the start if that element is visible
document.addEventListener("DOMContentLoaded", function() 
{
    toggleVisible(headings, openJobs, closeJobs);
})

// Adding scroll event
document.addEventListener("scroll", function()
{
    if (headings)
    {
        headings.forEach(function(heading)
        {
           toggleShow(heading); 
        })
    }

    if (closeJobs)
    {
        closeJobs.forEach(function(closeJob)
        {
            toggleShow(closeJob)
        })
    }

    if (openJobs)
    {
        openJobs.forEach(function(openJob)
        {
            toggleShow(openJob);
        })
    }
})

// Function for toggling show
function toggleVisible(headings, openJobs, closeJobs)
{
    if (headings)
    {
        headings.forEach(function(heading)
        {
            const height = heading.getBoundingClientRect().top;

            if (height < windowHeight && height > 0)
            {
                heading.classList.add("show");
            }
        })
    }
    
    if (openJobs)
    {   
        openJobs.forEach(function(openJob)
        {
            const height = openJob.getBoundingClientRect().top;

            if (height < windowHeight && height > 0)
            {
                openJob.classList.add("show");
            }
        })
    }
    
    if (closeJobs)
    {
        closeJobs.forEach(function(clsoeJob)
        {
            const height = clsoeJob.getBoundingClientRect().top;

            if (height < windowHeight && height > 0)
            {
                clsoeJob.classList.add("show");
            }
        })
    }
}

