$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
$PDC = $domainObj.PdcRoleowner.Name
$searchString = "LDAP://" + $PDC + "/"
$distinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
$searchString += $distinguishedName

$searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI] $searchString)
$searchRoot = New-Object System.DirectoryServices.DirectoryEntry($searchString)
$searcher.SearchRoot = $searchRoot

$searcher.filter = "(objectCategory=Group)"
$allGroups = $searcher.FindAll() 

$output = ""
Foreach ($group in $allGroups)
{
    if ($group.properties.member.count -gt 0)                  # if a group has any members
    { 
        $groupName = $group.properties.name
        foreach($member in $group.properties.member)           # for each member
        {                 
            if ($output -eq "") { $output += "$groupName`n" }  # Add parent group to output
            $output += "`t -> $member`n"                       # Add member to output
                
        }
        Write-Host $output 
        $output = ""     
    }
  
}
