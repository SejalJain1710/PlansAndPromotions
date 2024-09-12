Endpoint overview -  
* /partners/create-plan - adds a new plan - planID, planName, amountOptions and tenureOptions, benefitPercentage(for example: 10), benefitType(cashback/voucher)
* /partners/create-promo - each plan can have multiple promotions running - planId, promoId, promoName, validityType (quantity/time), quantity, startTime, endTime, benefitPercentage
* /partners/delete-plan/{planID} - deletes planID

* /users/get-plan - shows all plans along with promos - planID, planName, amountOptions and tenureOptions, benefitPercentage (for example: 10), benefitType

* /users/create-entry - creates a new record for user selected plan - planID, userID, promoId, selectedAmount, selectedTenure, startDate, depositedAmount


Things to do/good to haves - 
* /users/create - expose endpoint to create a new user
* /users/get-plan/{userId} - show selected entry
* /partners/get-plan - shows all active/inactive plans along with promos (introduce active column, delete plan would set active = 0) - planID, planName, active/inactive, amountOptions and tenureOptions, benefitPercentage (for example: 10), benefitType

* /update-plan
* /delete-promo
* /update-promo


Handy requests -
*Create a promo*
{
"planId": 1,
"promoName": "Pay day discount",
"benefitPercentage": 15,
"validityType": "tenure",
"startDate": "2022-01-01",
"endDate": "2022-04-01"
}

*create a user selected plan entry*
{
    "userID": 1,
    "planID": 1,
    "promoID": 1,
    "selectedAmount": 50000,
    "selectedTenure": 24,
    "startDate": "2022-02-01",
    "depositedAmount": 50000
}
