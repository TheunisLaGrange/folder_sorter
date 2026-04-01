python -m venv .venv
.\.venv\Scripts\Activate
# Define the directory to search
$directory = $PWD.Path
#$directory = "C:\Path\To\Your\Folder"
# Check if requirements.txt is empty
Get-ChildItem -Path $directory requirements.txt | Where-Object { $_.Length -eq 0 } | ForEach-Object {
    Write-Output "Please fill in the requirements.txt file."
    # Ends the script immediately
    exit
}

pip install -r requirements.txt
