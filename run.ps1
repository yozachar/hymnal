# # check if a command exists
# function command_exists {
#     param([string]$cmd)
#     if (Get-Command $cmd -ErrorAction SilentlyContinue) {
#         return $true
#     }
#     else {
#         return $false
#     }
# }

# cleanup
Remove-Item -Path ./build/ -Recurse -Force

# build
Write-Host "==> Build & Generate"
pnpm install; cargo run; pnpm build

# preview
pnpm preview

# # deploy
# $commands = @("docker", "podman")
# foreach ($cmd in $commands) {
#     if (command_exists $cmd) {
#         Write-Host "`n==> Deploy with '$cmd'`n"
#         & "$cmd-compose" -p hymnal -f ./compose.yaml down
#         & "$cmd-compose" -p hymnal -f ./compose.yaml up -d
#         Write-Host "`n==> Open http://[::1]:8080 in your browser"
#         exit
#     }
#     else {
#         Write-Host "`n==> Warning: Command '$cmd' not found"
#     }
# }
# Write-Host "`n==> Error: Deploymnet failed"
# exit 1
