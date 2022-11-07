
$domainObj = [System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain()
$PDC = $domainObj.PdcRoleowner.Name
$searchString = "LDAP://" + $PDC + "/"
$distinguishedName = "DC=$($domainObj.Name.Replace('.', ',DC='))"
$searchString += $distinguishedName
$searcher = New-Object System.DirectoryServices.DirectorySearcher([ADSI] $searchString)
$searchRoot = New-Object System.DirectoryServices.DirectoryEntry($searchString)

$searcher.SearchRoot = $searchRoot
$searcher.filter = "(serviceprincipalname=*)"
$result = $searcher.FindAll()

$spnToIP = [System.Collections.Hashtable]::new()  # key: SPN -- value: IP
Foreach($obj in $result)
{
    $SpnArray = $obj.properties.serviceprincipalname.split(' ')
    Foreach ($spn in $SpnArray)
    {
        $searchHost = $spn.split('/')[-1].split(':')[0] # parse out host for nslookup
        try {
	        $nslookup = cmd.exe /c "nslookup $searchHost" 2>&1
            $ip = $nslookup.split(' ')[26]  # parse out IP
            $spnToIP[$spn] = $ip
        }
        catch {
            $ip = "Unknown"
            $spnToIP[$spn] = $ip
        }
    }
}

$spnToIP.GetEnumerator() | Sort Value | Format-Table -HideTableHeaders -Autosize
