# it is a special structure in python that stores values in form of key value pairs
# so if we want to access any values we can access it through key
# suppose jan--> january
#feb -->february

monthconversions={
    "jan":"January",
    "feb":"February",
    "mar":"march",
    "apr":"April",
    "may":"May",
    "jun":"June",
    "jul":"July",
    "aug":"August",
    "sep":"September",
    "oct":"October",
    "nov":"November",
    "dec":"December"
}

print(monthconversions["nov"]) # or
print(monthconversions.get("nov"))

# note instead of jan,feb we can use numbers like 0, 1 ,2 .....etc



