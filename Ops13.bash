# Define user attributes
$firstName = "Franz"
$lastName = "Ferdinand"
$username = "ferdi"
$displayName = "$firstName $lastName"
$office = "Springfield, OR"
$department = "TPS Department"
$email = "ferdi@GlobeXpower.com"

# Create a secure password for the user
$password = ConvertTo-SecureString -String "Password123!" -AsPlainText -Force

# Specify the AD user parameters
$userParams = @{
    SamAccountName = $username
    UserPrincipalName = "$username@YourDomain.com"  # Replace YourDomain.com with your actual domain
    Name = $displayName
    GivenName = $firstName
    Surname = $lastName
    DisplayName = $displayName
    EmailAddress = $email
    Title = "TPS Reporting Lead"
    Office = $office
    Department = $department
    AccountPassword = $password
    Enabled = $true
}

# Create the AD user
New-ADUser @userParams -PassThru

# Verify in ADAC (Active Directory Administrative Center) that the user was created with the correct attributes.
# If anything is missing, delete the user in ADAC and re-attempt from PowerShell ISE.
