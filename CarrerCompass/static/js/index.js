import { toggleShow} from "./common.js";

const heading = document.querySelector(".job-offer-heading")
const jobs = document.querySelectorAll(".job");

document.addEventListener("scroll", function()
{
    jobs.forEach(function(job)
    {
        toggleShow(job);
    })

    toggleShow(heading)
})

