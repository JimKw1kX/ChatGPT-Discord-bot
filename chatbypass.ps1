Write-Host "░█████╗░██╗░░██╗░█████╗░████████╗░██████╗░██████╗░████████╗  ██████╗░██╗░░░██╗██████╗░░█████╗░░██████╗░██████╗"  -ForegroundColor Green
Write-Host "██╔══██╗██║░░██║██╔══██╗╚══██╔══╝██╔════╝░██╔══██╗╚══██╔══╝  ██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝" -ForegroundColor Green
Write-Host "██║░░╚═╝███████║███████║░░░██║░░░██║░░██╗░██████╔╝░░░██║░░░  ██████╦╝░╚████╔╝░██████╔╝███████║╚█████╗░╚█████╗░" -ForegroundColor Green
Write-Host "██║░░██╗██╔══██║██╔══██║░░░██║░░░██║░░╚██╗██╔═══╝░░░░██║░░░  ██╔══██╗░░╚██╔╝░░██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗" -ForegroundColor Green
Write-Host "╚█████╔╝██║░░██║██║░░██║░░░██║░░░╚██████╔╝██║░░░░░░░░██║░░░  ██████╦╝░░░██║░░░██║░░░░░██║░░██║██████╔╝██████╔╝" -ForegroundColor Green
Write-Host "░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═╝░░░░░░░░╚═╝░░░  ╚═════╝░░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░" -ForegroundColor Green
Write-Host "                                   " -ForegroundColor Green
Write-Host "                                   A project by Jim Solomon" -ForegroundColor Green
while($True)
{
    $input = Read-Host "Please enter your quesion here:$"
    Write-Host "`n[+] Input: $input"
    Write-Host "`n[+] Output:"

    $body = @{
        prompt = $input
        model = "text-davinci-003"
        max_tokens = 4000
        temperature = 1.0
    }

    $headers = @{
        'Content-Type' = 'application/json'
        'Authorization' = "Bearer API-KEY"
    }


        $jsonBody = $body | ConvertTo-Json

        $response = Invoke-WebRequest -Uri "https://api.openai.com/v1/completions" -Method POST -Body $jsonBody -Headers $headers -ContentType 'application/json'
        $response.Content | ConvertFrom-Json | select -ExpandProperty choices | select -ExpandProperty text
}
