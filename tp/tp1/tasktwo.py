#methode dictionnaire
Prod = {
    "Prod_cod": "",
    "Prod_name": "",
    "Unit_price": None,
    "Prod_quantity": None,
    "Prod_stock": None,
    "Tax_rate": None
}

#Input: Prod_cod, Prod_name, Prod_price, Prod_quantity, Prod_stock,	Tax_rate using the input function input () note l'ordre differe de l'exercice
Prod["Prod_cod"], Prod["Prod_name"], Prod["Unit_price"], Prod["Prod_quantity"], Prod["Prod_stock"], Prod["Tax_rate"] = input("Donner: code, name, price, quantity, stock, rate en cet ordre separes par ',':\n").split(',')

#Convert Prod_stock from a string to a float.
Prod["Prod_stock"] = float(Prod["Prod_stock"])

#Convert Tax_rate from an integer to a float.
Prod["Tax_rate"] = float(Prod["Tax_rate"]) / 100

#reste des conversions
Prod["Unit_price"], Prod["Prod_quantity"] = float(Prod["Unit_price"]), int(Prod["Prod_quantity"])

#Calculate the subtotal using: Prod_quantity, Unit_price
Subtotal = Prod["Prod_quantity"] * Prod["Unit_price"]

#Calculate Tax Amount: Multiply the subtotal by the tax_rate.
TaxAmount = Subtotal * Prod["Tax_rate"]

#Calculate Total Cost: Add the subtotal and the tax_amount.
TotalCost = Subtotal + TaxAmount

#Calculate the remaining stock (the difference betwwen the old stock and the ordered quantity)
rstock = Prod["Prod_stock"] - Prod["Prod_quantity"]

#Format and Print the Receipt: Create a multi-line output string that looks like a clean receipt summary. It should display:
print("\n******************************* ORDER RECEIPT *******************************")
print(f"{Prod['Prod_name']}\nPrice/Unit: {Prod['Unit_price']:.2f} DA\nQuantity: {Prod['Prod_quantity']}\nSubtotal: {Subtotal:.2f}\nTax ({Prod['Tax_rate']*100:.0f}%): {TaxAmount:.2f}\n******************** Total Cost: {TotalCost:.2f}\n******************** Remaining stock : {rstock:.0f}\n***************************************************************************")
