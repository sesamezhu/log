pyinstaller main.spec --noconfirm
if exist dist\log_flask\main.exe (
    echo "Build Successful"
) else (
    echo "Build Failed"
)