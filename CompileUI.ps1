$root = $(pwd)
cd ui_Files
$loc = $(pwd)
$fileList = (Get-ChildItem $loc)

#### COMPILE LOOP
foreach ($file in $fileList){
    $extn = [System.IO.Path]::GetExtension($file)
    if ($extn -eq ".ui"){
        $currentFile = $file | % {[System.IO.Path]::GetFileNameWithoutExtension($_)}
        $rawFile = $currentFile+".ui"
        #$finalFile = "ui"+$currentFile+".py"
        $TempFile = $currentFile+".py"
        pyside2-uic $rawFile > $TempFile
        $FinalFile = "ui_" + $TempFile
        Get-Content -Encoding Unicode $TempFile | Out-File -Encoding utf8 $FinalFile
        #Get-Content -Encoding Unicode $TempFile | Out-File -Encoding utf8NoBOM $FinalFile
        #$TempFile | % {[System.Io.File]::ReadAllText($TempFile)} | Out-File -FilePath $FinalFile -Encoding utf8
        Remove-Item $TempFile
    }

    if ($extn -eq ".qrc"){
        $currentFile = $file | % {[System.IO.Path]::GetFileNameWithoutExtension($_)}
        $rawFile = $currentFile+".qrc"
        $TempFile1 = $currentFile
        pyside2-rcc $rawFile -o $TempFile1
        TFile = $TempFile1 | % {[System.IO.Path]::GetFileNameWithoutExtension($_)} + "_rc" 
        $FinalFile = $TFile + ".py"
        Get-Content -Encoding Unicode $TempFile | Out-File -Encoding utf8 $FinalFile
        #Get-Content -Encoding Unicode $TempFile | Out-File -Encoding utf8NoBOM $FinalFile
        #$TempFile | % {[System.Io.File]::ReadAllText($TempFile)} | Out-File -FilePath $FinalFile -Encoding utf8
        Remove-Item $TempFile
    }
}
cd ..
#### RE ENCODING LOOP

#### 

#### MOVE LOOP
Move-Item -Path ui_Files\*.py -Destination .\ -Force
####