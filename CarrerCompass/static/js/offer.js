import { toggleShow, getCookie } from "./common.js";

const closeBtns = document.querySelectorAll(".closeBtn");
const closeJobLists = document.querySelector(".close-jobs");
const openJobLists = document.querySelector(".open-jobs");
const body = document.querySelector("body");
const headings = document.querySelectorAll("h1");

const closeJobs = closeJobLists?.querySelectorAll(".job");
const openJobs = openJobLists?.querySelectorAll(".job");


const windowHeight = window.innerHeight;

closeBtns.forEach(function(closeBtn) {
    closeBtn.addEventListener("click", function() {
        // Show Confirm Box

        // Getting Confirm Box
        const confirmBox = closeBtn.parentElement.parentElement.nextElementSibling;

        confirmBox.style.display = "flex";

        // Making Change According to user Choice
        closeJob(confirmBox.firstElementChild.children[1].firstElementChild, confirmBox.firstElementChild.children[1].children[1], confirmBox, closeBtn)
    })
})

// Function for makeing changes according to user choice
function closeJob(yes, no, obj, btn)
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
                // Remove the job from job offer and add to close job
                const job = obj.previousElementSibling;

                openJobLists.remove(job);

                console.log(job);

                // Removing close btn from job
                const buttonLists = job.querySelector(".button-list");
                buttonLists.remove(buttonLists.querySelector(".closeBtn"));

                // Removing confirm Container from opbjobs
                openJobLists.remove(obj);
                
                closeJobLists.insertBefore(job, closeJobLists.firstElementChild);

                // Check there is not more open job
                if (openJobLists.children.length === 0)
                {
                    document.querySelector(".offer-heading").style.display = "none";
                }
                
            }

            return;
        }

        catch(error)
        {
            console.log(error);
        }

        // Hide ojb
        obj.style.display = "none";
        btn.textContent = "Closed";
        btn.disabled = true;
    })

    no.addEventListener("click", function() {
        obj.style.display = "none";
    })
}

// Adding show class at the start if that element is visible
document.addEventListener("DOMContentLoaded", function() 
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


