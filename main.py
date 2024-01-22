# Return as an early exit
def format_name(fName, lName):
  """Take a first and last name and format it to return the title case version of the name."""
  if fName == "" or lName == "":
    return "You didn't provide valid value"
  return f"{fName} {lName}".title()

# Already used Function with Outputs
length = len(format_name("naseeb", "khan"))
print(length)
print(format_name("naseeb", "khan"))