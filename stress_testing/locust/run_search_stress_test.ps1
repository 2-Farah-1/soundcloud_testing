$LocustFile = "locustfile_search_stress_test.py"
$HostUrl = "https://tunify.duckdns.org"
$BaseReportDir = "../reports/search_stress_results"

$Tests = @(
    @{
        Id = "SST-00A"
        Name = "ten_users_2_spawn"
        Users = 10
        SpawnRate = 2
        Runtime = "2m"
    },
    @{
        Id = "SST-00B"
        Name = "fifty_users_10_spawn"
        Users = 50
        SpawnRate = 10
        Runtime = "2m"
    },
    @{
        Id = "SST-00C"
        Name = "hundred_users_20_spawn"
        Users = 100
        SpawnRate = 20
        Runtime = "3m"
    },
    @{
        Id = "SST-00D"
        Name = "five_hundred_users_100_spawn"
        Users = 500
        SpawnRate = 100
        Runtime = "3m"
    },
    @{
        Id = "SST-01"
        Name = "thousand_users_100_spawn"
        Users = 1000
        SpawnRate = 100
        Runtime = "5m"
    },
    @{
        Id = "SST-02"
        Name = "two_thousand_users_200_spawn"
        Users = 2000
        SpawnRate = 200
        Runtime = "3m"
    },
    @{
        Id = "SST-03"
        Name = "two_thousand_users_1k_spawn"
        Users = 2000
        SpawnRate = 1000
        Runtime = "2m"
    },
    @{
        Id = "SST-04"
        Name = "five_thousand_users_1k_spawn"
        Users = 5000
        SpawnRate = 1000
        Runtime = "2m"
    },
    @{
        Id = "SST-05"
        Name = "fifteen_hundred_users_500_spawn"
        Users = 1500
        SpawnRate = 500
        Runtime = "2m"
    },
    @{
        Id = "SST-06"
        Name = "fifteen_hundred_users_150_spawn_LONG"
        Users = 1500
        SpawnRate = 150
        Runtime = "10m"
    },
     @{
        Id = "SST-07"
        Name = "five_thousand_users_2k_spawn"
        Users = 5000
        SpawnRate = 2000
        Runtime = "2m"
    },
    @{
        Id = "SST-08"
        Name = "eight_thousand_users_1k_spawn"
        Users = 8000
        SpawnRate = 1000
        Runtime = "4m"
    },

    @{
        Id = "SST-09"
        Name = "ten_thousand_users_1k_spawn"
        Users = 10000
        SpawnRate = 1000
        Runtime = "5m"
    },

    @{
        Id = "SST-10"
        Name = "five_hundred_users_200_spawn"
        Users = 500
        SpawnRate = 200
        Runtime = "3m"
    },
    @{
        Id = "SST-11"
        Name = "five_hundred_users_500_spawn"
        Users = 500
        SpawnRate = 500
        Runtime = "3m"
    },
    @{
        Id = "SST-12"
        Name = "one_thousand_users_200_spawn"
        Users = 1000
        SpawnRate = 200
        Runtime = "3m"
    },
    @{
        Id = "SST-13"
        Name = "fifteen_hundred_users_200_spawn"
        Users = 1500
        SpawnRate = 200
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