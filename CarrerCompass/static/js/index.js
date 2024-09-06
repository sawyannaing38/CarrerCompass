import { toggleShow} from "./common.js";

const heading = document.querySelector(".job-offer-heading")
const jobs = document.querySelectorAll(".job");
const jobLists = document.querySelector(".job-lists");

if (jobs.length == 4)
{
    jobLists.style.justifyContent = "space-between";
}

document.addEventListener("scroll", function()
{
    jobs.forEach(function(job)
    {
        toggleShow(job);
    })

    toggleShow(heading)
})

