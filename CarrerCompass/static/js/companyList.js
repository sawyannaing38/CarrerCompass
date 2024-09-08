import {toggleShow} from "./common.js"

const companies = document.querySelectorAll(".company");
const searchBox = document.querySelector("#company");

document.addEventListener("DOMContentLoaded", function()
{
    companies.forEach(function(company)
    {
        toggleShow(company);
    })
})

document.addEventListener("scroll", function()
{
    companies.forEach(function(company)
    {
        toggleShow(company);
    })
})

searchBox.addEventListener("input", function()
{   
    const inputValue = this.value.toLowerCase();

    if (!inputValue)
    {
        companies.forEach(function(company)
        {
            company.style.display = "block";
        })
    }

    else 
    {
        companies.forEach(function(company)
        {
            // Getting company name 
            const companyName = company.querySelector(".company-name").textContent.toLowerCase();

            if (companyName.includes(inputValue))
            {
                company.style.display = "block";
            }

            else 
            {
                company.style.display = "none";
            }
        })
    }
})