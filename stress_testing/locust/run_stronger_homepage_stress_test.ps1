$LocustFile = "locustfile_homepage_stress_test.py"
$HostUrl = "https://tunify.duckdns.org"
$BaseReportDir = "../reports/homepage_stress_results"

$Tests = @(
    @{
    Id = "HSST-01"
    Name = "eight_thousand_users_1k_spawn"
    Users = 8000
    SpawnRate = 1000
    Runtime = "4m"
},
@{
    Id = "HSST-02"
    Name = "eight_thousand_users_2k_spawn"
    Users = 8000
    SpawnRate = 2000
    Runtime = "3m"
},
@{
    Id = "HSST-03"
    Name = "ten_thousand_users_1k_spawn"
    Users = 10000
    SpawnRate = 1000
    Runtime = "4m"
},
@{
    Id = "HSST-04"
    Name = "ten_thousand_users_500_spawn"
    Users = 10000
    SpawnRate = 500
    Runtime = "5m"
},
@{
    Id = "HSST-05"
    Name = "twelve_thousand_users_1k_spawn"
    Users = 12000
    SpawnRate = 1000
    Runtime = "4m"
},
@{
    Id = "HSST-06"
    Name = "fifteen_thousand_users_1k_spawn"
    Users = 15000
    SpawnRate = 1000
    Runtime = "5m"
},
@{
    Id = "HSST-07"
    Name = "fifteen_thousand_users_2k_spawn"
    Users = 15000
    SpawnRate = 2000
    Runtime = "4m"
},
@{
    Id = "HSST-08"
    Name = "twenty_thousand_users_1k_spawn"
    Users = 20000
    SpawnRate = 1000
    Runtime = "5m"
},
@{
    Id = "HSST-09"
    Name = "twenty_thousand_users_2k_spawn"
    Users = 20000
    SpawnRate = 2000
    Runtime = "4m"
},
@{
    Id = "HSST-10"
    Name = "twenty_thousand_users_5k_spawn_flash"
    Users = 20000
    SpawnRate = 5000
    Runtime = "2m"
},
@{
    Id = "HSST-11"
    Name = "twenty_five_thousand_users_2k_spawn"
    Users = 25000
    SpawnRate = 2000
    Runtime = "4m"
},
@{
    Id = "HSST-12"
    Name = "thirty_thousand_users_3k_spawn"
    Users = 30000
    SpawnRate = 3000
    Runtime = "3m"
}
  
)

foreach ($Test in $Tests) {
    $RunName = "$($Test.Id)_$($Test.Name)"
    $ReportDir = "$BaseReportDir/$RunName"

    New-Item -ItemType Directory -Force -Path $ReportDir | Out-Null

    Write-Host ""
    Write-Host "=================================================="
    Write-Host "Starting test: $RunName"
    Write-Host "Users: $($Test.Users)"
    Write-Host "Spawn Rate: $($Test.SpawnRate)"
    Write-Host "Runtime: $($Test.Runtime)"
    Write-Host "Reports folder: $ReportDir"
    Write-Host "=================================================="
    Write-Host ""

    locust `
        -f $LocustFile `
        --headless `
        -H $HostUrl `
        -u $($Test.Users) `
        -r $($Test.SpawnRate) `
        --run-time $($Test.Runtime) `
        --html "$ReportDir/report.html" `
        --csv "$ReportDir/stats" `
        2>&1 | Tee-Object -FilePath "$ReportDir/run.log"

    Write-Host ""
    Write-Host "Finished test: $RunName"
    Write-Host "Waiting 10 seconds before next test..."
    Start-Sleep -Seconds 10
}