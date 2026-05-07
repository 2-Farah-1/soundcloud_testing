$LocustFile = "locustfile_homepage_stress_test.py"
$HostUrl = "https://tunify.duckdns.org"
$BaseReportDir = "../reports/homepage_stress_results"

$Tests = @(
    @{
        Id = "HST-01"
        Name = "thousand_users_100_spawn"
        Users = 1000
        SpawnRate = 100
        Runtime = "5m"
    },
    @{
        Id = "HST-02"
        Name = "two_thousand_users_200_spawn"
        Users = 2000
        SpawnRate = 200
        Runtime = "3m"
    },
    @{
        Id = "HST-03"
        Name = "two_thousand_users_1k_spawn"
        Users = 2000
        SpawnRate = 1000
        Runtime = "2m"
    },
    @{
        Id = "HST-04"
        Name = "five_thousand_users_1k_spawn"
        Users = 5000
        SpawnRate = 1000
        Runtime = "2m"
    },
    @{
        Id = "HST-05"
        Name = "fifteen_hundred_users_500_spawn"
        Users = 1500
        SpawnRate = 500
        Runtime = "2m"
    },
    @{
        Id = "HST-06"
        Name = "fifteen_hundred_users_150_spawn_LONG"
        Users = 1500
        SpawnRate = 150
        Runtime = "10m"
    },

    # Breaking-point ramp, done as separate clean runs:
    @{
        Id = "HST-07"
        Name = "five_hundred_users_200_spawn"
        Users = 500
        SpawnRate = 200
        Runtime = "3m"
    },
    @{
        Id = "HST-07B"
        Name = "five_hundred_users_500_spawn"
        Users = 500
        SpawnRate = 500
        Runtime = "3m"
    },
    @{
        Id = "HST-08"
        Name = "one_thousand_users_200_spawn"
        Users = 1000
        SpawnRate = 200
        Runtime = "3m"
    },
    @{
        Id = "HST-09"
        Name = "fifteen_hundred_users_200_spawn"
        Users = 1500
        SpawnRate = 200
        Runtime = "3m"
    },

    @{
        Id = "HST-10"
        Name = "three_thousand_users_1k_spawn"
        Users = 3000
        SpawnRate = 1000
        Runtime = "3m"
    },
    @{
        Id = "HST-11"
        Name = "one_thousand_users_1k_spawn"
        Users = 1000
        SpawnRate = 1000
        Runtime = "2m"
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